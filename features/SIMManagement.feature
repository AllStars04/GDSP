@SIM
Feature: SIM Management
  This feature covers complete SIM management functionality.

  @SIMGRP_CREATE
  Scenario: Create New SIM Group - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Administration"
    then click on submenu "My organisation"
    when click on tab "Details"
    then click on link "Profile and groups"
    when Button "Edit" is visible
    then click on button "Edit"
    then click on link "+ Add group"
    then enter text for "* Name" with value "GROUP4"
    then enter text for "Description" with value "test group"
    then click on button "Save"
    when text "GROUP4" is visible
