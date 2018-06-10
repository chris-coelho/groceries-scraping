from src.domain.entity_guard import EntityGuard


class ProductSupermarketGuard(EntityGuard):
    def check(self, product_supermarket):
        if not product_supermarket:
            super().add_issue('ProductSupermarket not instantiated.')
            return False

        if not product_supermarket.product or not product_supermarket.product.id:
            super().add_issue('Invalid Product.')

        if not product_supermarket.supermarket or not product_supermarket.supermarket.id:
            super().add_issue('Invalid Supermarket.')

        if not product_supermarket.price_update_url:
            super().add_issue('Pricing URL for update is required.')

        return len(super().get_issues()) == 0
