# Created by yonas at 6/12/2022
Feature: handling multiple windows


 # Scenario: Users is able to navigate to amazon blog from 404
  #  Given open Amazon product BB4NG522222 page
   # And Store original window
    # When Click on the dog image
   # And Switch to new window
   # Then verify blog is opened
   # And close blog
   # And Return to original window



  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    Then Click on Amazon Privacy Notice link
    Then Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    Then User can close new window
    Then switch back to original window

   # git remote add origin https://github.com/yonas395/homework-4-to-6.git
   # git branch -M main
   # git push -u origin main





  Scenario: new release links can be opened
    Given open amazon new release
    Then user can click through the links in side

