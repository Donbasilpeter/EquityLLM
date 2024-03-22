from config import Config
from transformers import BertTokenizer, BertModel
import torch

class EquityLLM:
    def __init__(self):
        config = Config()
        self.client = config.client
        self.system_role = config.system_role
        self.user_role = config.user_role
        self.google = config.GoogleNewsSearch
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.bert_model = BertModel.from_pretrained('bert-base-uncased')
    
    def start(self):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[self.system_role, self.user_role]
        )
        print(completion.choices[0].message.content)
        
        
    def google_news_search(self):
        results = self.google.crawl("Nse market news today")
        summarized_content = self.extract_keywords(results)
        self.user_role['content'] = self.user_role['content'] + summarized_content
        
    def extract_keywords(self, text):
        # Tokenize input text
        inputs = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
        
        # Obtain BERT embeddings
        with torch.no_grad():
            outputs = self.bert_model(**inputs)
            embeddings = outputs.last_hidden_state
        
        # Summarize embeddings (you can implement your summarization logic here)
        summarized_content = " ".join(text.split()[:100])  # Example: Taking first 100 tokens
        
        return summarized_content

if __name__ == "__main__":
    app = EquityLLM()
    app.google_news_search()
    app.start()
