import random

class Selectors:
    HOME_TITLE = "Welcome to E-Commerce"
    PRODUCT_TITLE = "Product"
    DETAILS_PRODUCT_TITLE = "Details about Product"
    ADD_TO_CART_BUTTON = "Add to Cart"
    CART_TITLE = "Your Cart"
    URL_CART = "/cart"
    PROCEED_TO_CHECKOUT_BUTTON = "Proceed to Checkout"
    CHECKOUT_TITLE = "Checkout"
    URL_CHECKOUT = "/checkout"
    NAME_INPUT = '[placeholder="Your Name"]'
    EMAIL_INPUT = '[placeholder="Your Email"]'
    COMPLETE_PURCHASE_BUTTON = "Complete Purchase"
    CONFIRMATION_MESSAGE = "Thank you for your purchase"
    NAME = "test"
    EMAIL = f"test_{random.randint(1, 10000)}@prueba.com"
    INVALID_EMAIL = "test_123.com"
    RANDOM_NUMBER = random.randint(1, 3)

    @staticmethod
    def get_selector_link(link):
        return f'a[href="{link}"]'

    @staticmethod
    def get_url_product(product_id):
        return f"/product/{product_id}"
