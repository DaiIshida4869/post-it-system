import csv


class DataLoader:
    @staticmethod
    def load_recipients(file_path: str) -> list:
        recipients = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            recipients = []
            for row in reader:
                for email in row:
                    recipients.append(email.strip())
        return recipients
