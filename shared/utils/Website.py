import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = url
        res = requests.get(url, headers=headers)
        self.raw_html = res.content
        soup = BeautifulSoup(self.raw_html, 'html.parser')

        self.title = soup.title.string if soup.title else "No title found"

        if soup.body:
            for tag in soup.body.find_all(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

        all_links = [a.get("href") for a in soup.find_all("a")] # type: ignore
        self.links = [link for link in all_links if link]

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n"