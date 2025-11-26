Feature: Login
    Scenario: Successful Login with standard credentials
        Given I open the login page
        When I login with "standard_user" and "secret_sauce"
        Then I should see the inventory page