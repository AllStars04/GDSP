@f1
Feature: test
  This is test feature

  @t1
  Scenario: testcase
    given start test case
    given open browser
    when login into portal
    when click on menu "Devices"
    then click on submenu "All devices"
    when text "Devices" is visible
    when text "Search" is visible
    then click on input "Organisation"
    then click on list "PPTOMTOM"
    then select from list "aricent_55"
   # then click on button "Search"
    #when text "No results were found" is visible
    ####Saurabh

  @createcustomer
  Scenario: Create Customer
    given start test case
    given open browser
    when login into portal
    when click on menu "Administration"
    then click on submenu "Customers"
    when text "Organisations" is visible
    when text "matching" is visible
    then click on link "Create organisation"
    then click on button "Create customer"

    when text "Basic information" is visible
    then enter text for "* Customer name" with value "AUTO1212"
    then enter text for "* Customer description" with value "autotest"

    then select option "ICCID" of dropdown "* Primary SIM identifier"
    then select option "ICCID" of dropdown "* Display name source"

