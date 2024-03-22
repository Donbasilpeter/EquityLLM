from config import Config

    
class EquityLLM:
    def __init__(self):
        config = Config()
        self.client = config.client
        self.system_role = config.system_role
        self.user_role = config.user_role
    
    def start(self):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[self.system_role, self.user_role]
        )
        print(completion.choices[0].message)


if __name__ == "__main__":
    app = EquityLLM()
    app.start()
