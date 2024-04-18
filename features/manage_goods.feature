Feature: Managing goods

Scenario: View list of goods (11)
    Given User is logged as an admin
    When User is on the admin dashboard
    And User clicks on the "Products" tab
    Then Page with list of goods is displayed

Scenario: Create a new product (12)
    Given User is logged as an admin
    When User in on the "Products" tab
    And User clicks on the "Add New" button
    And User fills in all neccessary details
    And User clicks on the "Save" button
    Then Product is created and success message is displayed

Scenario: Delete an existing product (13)
    Given User is logged as an admin
    And User in on the "Products" tab
    When User clicks on the checkbox of product to be deleted
    And User clicks on the "Delete" button
    Then The product is deleted and success message is displayed

Scenario: Update an existing product (14)
    Given User is logged as an admin
    And User in on the "Products" tab
    When User clicks on the "Edit" button of the product to be updated
    And User changes the product
    And User clicks on the "Save" button
    Then The product is updated and success message is displayed

Scenario: Change availability of an existing product (15)
    Given User is logged as an admin
    And User is on the "Products" tab
    And Products quantity is not zero
    When User clicks on the "Edit" button of the product to be updated
    And User changes the products quantity
    And User clicks on the "Save" button
    Then The products quantity is updated and success message is displayed




