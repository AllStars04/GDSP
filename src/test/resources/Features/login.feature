@login

Feature: As an Opco Admin
  I want to login to GDSP
  So that i manage the customers.

  Scenario Outline: Login to GDSP as Opco Admin
    Given I am on login page
    When I provide "<username>", "<password>"
    And do login
    Then I successfully login to GDSP Portal
    Examples:
      | username        | password   |
      | E2Eopco_aricent | Vodafone1! |
      | E2Eopco_aricent | Vodafone1! |


