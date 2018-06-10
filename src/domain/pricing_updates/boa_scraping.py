from bs4 import BeautifulSoup

from src.domain.pricing_updates.web_scraping import WebScraping


class BoaScraping(WebScraping):
    def get_price(self, url):
        content = self._http_request.get(url)
        soup = BeautifulSoup(content, "html.parser")

        # <span class="price">R$ 5,29</span>
        element = soup.find('span', {'class': 'price'})
        string_price = element.text.strip()[3:]
        if ',' in string_price:
            string_price = string_price.replace(',', '.')

        try:
            return float(string_price)
        except:
            raise ValueError('Price not found.')
