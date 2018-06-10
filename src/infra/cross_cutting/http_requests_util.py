import requests


class HttpRequestsUtil:
    def get(self, url):
        return requests.get(url).content
