import pytest
from pytest_bdd import given, scenarios
from tests.pages.ecommerce_page import ECommercePage

# Register the scenarios
scenarios('../features/profile.feature')

@pytest.fixture
def ecommerce_page(page):
    return ECommercePage(page)

@given("I visit the profile page")
def visit_profile_page(ecommerce_page):
    ecommerce_page.visit("/profile")
