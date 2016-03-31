@createnewuser
Feature: Opco user can create new Users
  Scenario: create New user page
  Given I am on homepage
  When  I go to ManageAccount page
  And go to user account section
  And I go to create new user
  Then I show see a page for create new user