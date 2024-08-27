import datetime
import os

import holidays
from botocore.exceptions import ClientError
from jinja2 import Environment, FileSystemLoader

from bedrock_auth import BedrockAuth


class HolidayChecker:
    def __init__(self) -> None:
        self.model_id = os.getenv('CLAUDE_MODEL')
        self.bedrock_client = BedrockAuth()
        self.client = self.bedrock_client.load_client()

    def _check_global_holiday(self, date_today: datetime.date) -> dict:
        countries = holidays.list_supported_countries()
        holiday_info = {}

        for country in countries:
            try:
                country_holidays = getattr(holidays, country)()
                if date_today in country_holidays:
                    holiday_name = country_holidays.get(date_today)
                    if country not in holiday_info:
                        holiday_info[country] = []
                    holiday_info[country].append(holiday_name)
            except AttributeError:
                continue 

        # if holiday_info:
        #     for country, holiday_names in holiday_info.items():
        #         for holiday_name in holiday_names:
        #             print(f"{date_today.strftime('%Y-%m-%d')} is a holiday in {country}: {holiday_name}.")
        # else:
        #     print(f"{date_today.strftime('%Y-%m-%d')} is not a holiday in any country in the world.")

        return holiday_info

    def get_holiday_explanation(self, query:str) -> str:
        today = datetime.date.today()
        # today_str = "2024-07-10"
        # today = datetime.datetime.strptime(today_str, "%Y-%m-%d").date()
        world_holidays = self._check_global_holiday(today)
        # print(world_holidays)
        if not world_holidays:
            no_holidays_template = f"{today.strftime('%Y-%m-%d')} is not a holiday in any country in the world."
            return no_holidays_template

        env = Environment(loader=FileSystemLoader("prompts"))
        template = env.get_template("system_prompts.txt")
        output = template.render({"today": today, "world_holidays": world_holidays})
        # print(output)

        system_prompt = [
            {
                "text": output
            }
        ]
        conversation = [
            {
                "role": "user",
                "content": [{"text": "Tell me about today's holiday."}],
            }
        ]
        try:
            response = self.client.converse(
                modelId=self.model_id,
                messages=conversation,
                system=system_prompt,
                inferenceConfig={"maxTokens": 1000, "temperature": 0, "topP": 0},
            )
            response_text = response["output"]["message"]["content"][0]["text"]
            return response_text
        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{self.model_id}'. Reason: {e}")
            exit(1)

if __name__ == "__main__":
    date_today = datetime.date.today()
    # today_str = "2024-07-10"
    # date_today = datetime.datetime.strptime(today_str, "%Y-%m-%d").date()
    holiday_checker = HolidayChecker()
    world_holidays = holiday_checker._check_global_holiday(date_today)
    print(world_holidays)

    explanation = holiday_checker.get_holiday_explanation("Tell me about today's holiday.")
    print(explanation)