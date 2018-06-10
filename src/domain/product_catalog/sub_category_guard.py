from src.domain.entity_guard import EntityGuard


class SubCategoryGuard(EntityGuard):

    def check(self, sub_category):
        if not sub_category:
            super().add_issue('Subcategory not instantiated.')
            return False

        if not sub_category.name:
            super().add_issue('Name is required.')
        else:
            if len(sub_category.name) < 3:
                super().add_issue('Name should have at least 2 characters.')

        if not sub_category.category or not sub_category.category.id:
            super().add_issue('Invalid Category.')

        return len(super().get_issues()) == 0
