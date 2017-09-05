Feature: Login

  @TC_OpGrpUserLogin
  Scenario: Login - Make remember last user role persistent

        given start test case
        given open browser
        when login into portal
        then click on link "PPVGE as Operator Administrator"
        then click on link "Platform as Platform Support & IITC"
        when text "Platform as Platform Support & IITC" is visible
        then logout and close the browser
        given open browser
        when login into portal
        when text "PPVGE as Operator Administrator" is visible
        then logout and close the browser