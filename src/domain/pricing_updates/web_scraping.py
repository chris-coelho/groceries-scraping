from abc import ABCMeta, abstractmethod


class WebScraping(metaclass=ABCMeta):
    def __init__(self, http_request):
        self._http_request = http_request

    @abstractmethod
    def get_price(self, url):
        pass

