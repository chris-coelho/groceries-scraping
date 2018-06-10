from src.domain.entity_guard import EntityGuard


class CategoryGuard(EntityGuard):

    def check(self, category):
        if not category:
            super().add_issue('Category not instantiated.')
            return False

        if not category.name:
            super().add_issue('Name is required.')
        else:
            if len(category.name) < 3:
                super().add_issue('Name should have at least 2 characters.')

        return len(super().get_issues()) == 0
