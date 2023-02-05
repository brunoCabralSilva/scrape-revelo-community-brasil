import requests
from rich import print
from parsel import Selector
from requests.exceptions import ConnectTimeout, HTTPError

class ListOfPosts():
    @staticmethod
    def listOfPosts():
        try:
            request = requests.get("https://community.revelo.com/author/bruno/", timeout=120)
            objectPage = {
                "status": request.status_code,
                "headers": request.headers,
                "attributes": request.__attrs__,
                "history": request.history,
                "content": request.text,
            }
            selector = Selector(objectPage["content"])
            listOfArticles = []
            for item in selector.css("body > div.viewport > div > section > div > div > article"):
                post = {
                    "title": item.css("div > a > header > h2::text").get(),
                    "link": "https://community.revelo.com" + item.css("a::attr(href)").get(),
                    "technology": item.css("div > a > header > div::text").get(),
                    "resume": item.css("div > a > div > p::text").get() + "...",
                    "date" : item.css("div > footer > div > span.post-card-byline-date > time::text").get(),
                    "readingTime": item.css("div > footer > div > span.post-card-byline-date::text").get(),
                    "image": "https://community.revelo.com" + item.css("a > img::attr(src)").get(),
                }
                listOfArticles.append(post)
            return listOfArticles
        except(ConnectTimeout, HTTPError):
            return "Error (Timeout)"
    