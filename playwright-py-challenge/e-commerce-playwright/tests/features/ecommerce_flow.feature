Feature: E-commerce testing

    # Happy path scenario
    Scenario: Buy a product on e-commerce
        Given User want to buy a product on the e-commerce platform
        When User clicks on the product
        And The UI redirects to products details
        And User adds the product to the cart
        And The UI redirects to "your cart"
        And User clicks on proceeds to checkout
        And the UI redirects to checkout information
        And User enters the data for the purchase
        And User clicks on "Complete Purchase"
        Then The UI renders the confirmation message
