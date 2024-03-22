from openai import OpenAI
import os

class Config:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.system_role = {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
            }
        self.user_role = {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming."
            }

