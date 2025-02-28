import pytest
from pytest_bdd import given, when, then, scenarios
from ..pages.ecommerce_page import ECommercePage
from ..utils.constants import Selectors

# Register the scenarios
scenarios('../features/invalid_checkout.feature')

@pytest.fixture
def ecommerce_page(page):
    return ECommercePage(page)

@given("User want to buy a product on the e-commerce platform with invalid email")
def user_wants_to_buy_product_invalid(ecommerce_page):
    ecommerce_page.visit("/")
    ecommerce_page.verify_page_url("/")
    ecommerce_page.verify_message_visible(Selectors.HOME_TITLE)

@when("User clicks on the product")
def user_clicks_on_product(ecommerce_page):
    ecommerce_page.click_element(
        Selectors.get_selector_link(f"/product/{Selectors.RANDOM_NUMBER}")
    )

@when("The UI redirects to products details")
def ui_redirects_to_product_details(ecommerce_page):
    ecommerce_page.verify_page_url(Selectors.get_url_product(Selectors.RANDOM_NUMBER))
    ecommerce_page.verify_message_visible(
        f"{Selectors.PRODUCT_TITLE} {Selectors.RANDOM_NUMBER}"
    )
    ecommerce_page.verify_message_visible(
        f"{Selectors.DETAILS_PRODUCT_TITLE} {Selectors.RANDOM_NUMBER}"
    )

@when("User adds the product to the cart")
def user_adds_product_to_cart(ecommerce_page):
    ecommerce_page.click_element_by_text(Selectors.ADD_TO_CART_BUTTON)

@when('The UI redirects to "your cart"')
def ui_redirects_to_cart(ecommerce_page):
    ecommerce_page.verify_page_url(Selectors.URL_CART)
    ecommerce_page.verify_message_visible(Selectors.CART_TITLE)
    ecommerce_page.verify_message_visible(Selectors.PRODUCT_TITLE)

@when("User clicks on proceeds to checkout")
def user_clicks_proceed_to_checkout(ecommerce_page):
    ecommerce_page.click_element_by_text(Selectors.PROCEED_TO_CHECKOUT_BUTTON)

@when("the UI redirects to checkout information")
def ui_redirects_to_checkout(ecommerce_page):
    ecommerce_page.verify_page_url(Selectors.URL_CHECKOUT)
    ecommerce_page.verify_message_visible(Selectors.CHECKOUT_TITLE)

@when("User enters the data for the purchase invalid")
def user_enters_invalid_purchase_data(ecommerce_page):
    ecommerce_page.enter_text(Selectors.NAME_INPUT, Selectors.NAME)
    ecommerce_page.enter_text(Selectors.EMAIL_INPUT, "jesus")

@when('User clicks on "Complete Purchase"')
def user_clicks_complete_purchase(ecommerce_page):
    ecommerce_page.click_element_by_text(Selectors.COMPLETE_PURCHASE_BUTTON)

@then("The UI renders an error message")
def ui_renders_error_message(ecommerce_page):
    ecommerce_page.verify_message_not_visible(Selectors.CONFIRMATION_MESSAGE)