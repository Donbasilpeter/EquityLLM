from googleapiclient.discovery import build
import requests
from bs4 import BeautifulSoup

class GoogleNewsSearch:
    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        self.service = build("customsearch", "v1", developerKey=self.api_key)
        self.links = []

    def search(self, query):
        result = self.service.cse().list(q=query, cx=self.search_engine_id).execute()
        items = result.get('items', [])
        search_links = []
        for item in items:
            link = item.get('link')
            if link:
                search_links.append(link)
        self.links = search_links

    def get_content(self):
        contents = ""
        for link in self.links:
            try:
                response = requests.get(link, timeout=5)
                if response.status_code ==200 :
                    soup = BeautifulSoup(response.content, 'html.parser')

                    text_content = soup.get_text()
                    contents= contents + text_content
            except Exception as e:
                print(f"Error retrieving content from {link}: {e}")
        return contents
    
    def crawl(self,query):
        self.search(query)
        return self.get_content()
        