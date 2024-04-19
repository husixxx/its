Feature: Searching and buying goods

Scenario: Search for a product (1)
    Given User is on any page
    When User types macbook in the search bar 
    And User presses the search button
    Then Page with results of MacBooks is displayed

Scenario: Browse "Camera" categorie (2)
    Given User is on any page
    When User clicks on a categories "Cameras" button
    Then Page with results of Cameras is displayed

Scenario: Open a product page (3)
    Given User is on the page of "Camera" products
    When User clicks on resulted product "Canon EOS 5D"
    Then Page with resulted product is displayed

Scenario: Open a related product page (4)
    Given User is on "iPhone" product page
    When User clicks on the related product
    Then Page of related product is displayed

Scenario: Add a product to the cart (5)
    Given User is on the product page
    When User clicks on the "Add to cart" button
    Then Product is added to the cart
    

Scenario: Add bad quantity of product to the cart (6)
    Given User is on the product page
    When User clicks on the "Add to cart" button
    And quantity of product is 0
    Then Product is not added to the cart
    

Scenario: Remove a product from the cart (7)
    Given User is on the cart page
    And Product is in the cart
    When User clicks on the "Remove" button
    Then Product is removed from the cart

Scenario: View cart (8)
    Given User is on any page
    And Any product is in the cart
    When User click on the cart icon
    Then All the products in the cart are displayed
    
Scenario: Show checkout page (9)
    Given User is on the cart page
    And Cart is not empty
    When User clicks on the checkout button
    Then Checkout page with all the products from the cart is displayed

Scenario: Checkout the items from the cart (10)
    Given User is on the checkout page with the products
    And Cart is not empty
    And User fills in all the neccessary informations
    When User clicks on the "Confirm order" button
    Then Success message is displayed