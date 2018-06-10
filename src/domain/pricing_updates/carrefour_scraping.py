from bs4 import BeautifulSoup

from src.domain.pricing_updates.web_scraping import WebScraping


class CarrefourScraping(WebScraping):
    def get_price(self, url):
        content = self._http_request.get(url)
        soup = BeautifulSoup(content, "html.parser")

        # <span class="prince-product-default col-xs-12 col-sm-12 col-md-12 current">R$ 21,99</span>
        element = soup.find('span', {'class': 'prince-product-default col-xs-12 col-sm-12 col-md-12 current'})
        string_price = element.text.strip()[3:]
        if ',' in string_price:
            string_price = string_price.replace(',', '.')

        try:
            return float(string_price)
        except:
            raise ValueError('Price not found.')
