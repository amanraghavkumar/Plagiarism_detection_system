import requests
from bs4 import BeautifulSoup

def check_online_plagiarism(text):
    query = "+".join(text.split()[:10])
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("h3")
    
    return len(results) * 5 
