from src.domain.entity_guard import EntityGuard


class ProductGuard(EntityGuard):

    def check(self, product):
        if not product:
            super().add_issue('Product not instantiated.')
            return False

        if not product.name:
            super().add_issue('Name is required.')
        else:
            if len(product.name) < 3:
                super().add_issue('Name should have at least 3 characters.')

        if not product.gtin:
            super().add_issue('GTIN is required')
        else:
            if len(product.gtin) != 13:
                super().add_issue('GTIN should have 13 numbers.')

        if product.price < 0.01 or product.price > 1000000:
            super().add_issue('Price should be greater then 0.')

        if not product.sub_category or not product.sub_category.id:
            super().add_issue('Invalid subcategory.')

        return len(super().get_issues()) == 0
