Feature: E-commerce Testing Negative

    # Negative scenario
    Scenario: Invalid email in checkout information
        Given User want to buy a product on the e-commerce platform with invalid email
        When User clicks on the product
        And The UI redirects to products details
        And User adds the product to the cart
        And The UI redirects to "your cart"
        And User clicks on proceeds to checkout
        And the UI redirects to checkout information
        And User enters the data for the purchase invalid
        And User clicks on "Complete Purchase"
        Then The UI renders an error message
