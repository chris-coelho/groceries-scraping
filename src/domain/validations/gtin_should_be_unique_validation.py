

def gtin_should_be_unique_validation(product_repo, gtin):
    gtin_already_exists = product_repo.get_by_gtin(gtin) is not None
    if gtin_already_exists:
        return False
    return True
