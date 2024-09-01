class DataLoader:
    @staticmethod
    def load_recipients(file_path: str) -> list:
        with open(file_path, 'r') as file:
            recipients = [line.strip() for line in file.readlines()]
        return recipients
