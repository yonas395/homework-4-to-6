# Created by Yonas at 5/18/2022
Feature: Amazon sign in page


  Scenario: sign in page can be opened from signin popup
    Given open amazon page
    When click on button from signin popup
    Then verify sign in page is opened


  Scenario: signin popup is visible for few seconds in the main page
    Given open amazon page
    Then SignIn popup is present
    When Wait for 5 seconds
    Then SignIn popup disappears