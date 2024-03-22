from openai import OpenAI
import os

class Config:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        self.system_role = {
            "role": "system",
            "content": """
            You are a Stock Market expert experienced in analysing current sentiments in market. 
            Your duty is to look into given inputs and understand the current market sentiments.
            You will summerise and understand what people in market thinks and predict how the
            market will perform for the day.
            """
            }
        self.user_role = {
            "role": "user",
            "content": """
            As a stock market expert you will have to evaluate all the news and tweets, given below and summerise the market sentiments.
            You will mainly have 3 tasks.
            1) give  an overview of what people are felling and 
            how its going to affect the market today. 
            2) create an index named EquityLLMIndex ranging from -1 to 1 to indicate how bearish or bulliesh the market today will be.
            -1 means the market is going to collapse a lot today. 1 means the market is going to be very bullish and reach sky.
            based on the sentiment give a value to EquityLLMIndex. for example, -0.88, -0.9, 0.76 etc
            3) if you are really confident about a stock to go bulliesh or bearish give the name of stock with the EquityLLMIndex for the stock as a list.
            
            when you do the above 3 tasks, it should be purely dependent on the tweets and market sentiments. Don't assume base on any prior knowledge.
            the tweets are given below.
            """
            }

