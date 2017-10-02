
  @SIMGRP_ADD_DEVICE
  Scenario: Add device to a SIM Group - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then click on link "111117500000013"
    when click on tab "Operations"
    then click on link "Configure"
    then click on link "Set groups"
    then click on input "Groups"
    then select from list "Group3"
    then click on button "Set"
    when text "The device groups for device 111117500000013 were successfully set." is visible

   @SIMGRP_REMOVE_DEVICE
   Scenario: Remove device from a SIM Group - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then click on link "111117500000013"
    when click on tab "Operations"
    then click on link "Configure"
    then click "close"
    then click on button "Set"
    when text "The device groups for device 111117500000013 were successfully set." is visible


   @SIMDetails_SET_COUNTRY
   Scenario:  Set home country for SIM - OPCO User
    given start test case
    given open browser
    when login into Portal
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "Operations"
    then click on link "Configure"
    then click on link "Set Home Country"
    select option "India" of dropdown "New home country"
    then click on button "Set"
    when text "The home country for the device 111117500000013 was successfully set to India."

   @SIMDetails_View_SIM_Details
   Scenario: View SIM details - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "Details"
    when text "SIM" is visible
    when text "Connectivity services" is visible
    when text "Profiles and groups" is visible
    when text "Contract" is visible
    when text "Recent data usage" is visible
    when text "Mobility" is visible


   @SIMDetails_View_SIM_Details_OPCO
   Scenario: View SIM details - OPCO User
    given start test case
    given open browser
    when login into Portal
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "Details"
    when text "SIM" is visible
    when text "Connectivity services" is visible
    when text "Profiles and groups" is visible
    when text "Contract" is visible
    when text "Recent data usage" is visible
    when text "Mobility" is visible

   @SIMHistory_View_SIM_History_OPCO
   Scenario: View SIM history - OPCO User
    given start test case
    given open browser
    when login into Portal
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "History"
    when click on radio "Activity List"
    select option "Administrative operations" of dropdown "Type"
    then click on button "Search"
    when text "Change state" is visible
    when text "Change service profile" is visible
    when text "Set home country" is visible
    when text "Set IMEI" is visible
    when text "New SIM record" is visible

   @SIMHistory_View_SIM_State_change_values_History_OPCO
   Scenario: View SIM state change values history - OPCO User
    given start test case
    given open browser
    when login into Portal
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "History"
    when click on radio "Activity List"
    select option "Administrative operations" of dropdown "Type"
    then click on button "Search"
    when text "Change state" is visible
    then click on link "Change state"
    when text "New state" is visible
    when text "Previous state" is visible


   @SIMHistory_View_SIM_History_Customer
   Scenario: View SIM history - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "History"
    when click on radio "Activity List"
    select option "Administrative operations" of dropdown "Type"
    then click on button "Search"
    when text "Change state" is visible
    when text "Change service profile" is visible
    when text "Set home country" is visible
    when text "Set IMEI" is visible
    when text "New SIM record" is visible

  @SIMHistory_View_SIM_History_Country_change_Customer
   Scenario: View SIM history country change values - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "History"
    when click on radio "Activity List"
    select option "Administrative operations" of dropdown "Type"
    then click on button "Search"
    when text "Set home country" is visible
    then click on link "Set home country"
    when text "New home country" is visible
    when text "Previous home country" is visible


@SIMHistory_View_SIM_History_IMEI_change_Customer
   Scenario: View SIM history imei change values - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "History"
    when click on radio "Activity List"
    select option "Administrative operations" of dropdown "Type"
    then click on button "Search"
    when text "Set IMEI" is visible
    then click on link "Set IMEI"
    when text "New IMEI" is visible
    when text "Previous IMEI" is visible

   @SIMHistory_View_SIM_History_CSP_change_Customer
   Scenario: View SIM history CSP change values - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when click on tab "History"
    when click on radio "Activity List"
    select option "Administrative operations" of dropdown "Type"
    then click on button "Search"
    when text "Change service profile" is visible
    then click on link "Change service profile"
    when text "New service profile" is visible
    when text "Previous service profile" is visible



   @SIMCustomAttributes_enable_custom_attr
   Scenario: Enable Custom attributes and make available for customer - OPCO User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    when click on menu "Administration"
    then click on submenu "Customers"
    then enter text for "Organisation" with value "Automation3"
    then click on button "Search"
    when link "Automation3" is visible
    then click on link "Automation3"
    then click on tab "Details"
    then click on button "Edit1"
    then enter text for "Custom attributes" with value "Attribute1"
    then click on button "Save"
    when text "Custom attributes Attribute1" is visible

   @SIMCustomAttributes_add_custom_attr_report
   Scenario: Add Custom attributes to report - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Administration"
    then click on submenu "My organisation"
    then click on tab "Details"
    then click on button "Edit1"
    then click on checkbox "checkbox1"
    then click on button "Save"

    @SIMCustomAttributes_edit_custom_attr
   Scenario: Edit Custom attributes - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Administration"
    then click on submenu "My organisation"
    then click on tab "Details"
    then click on button "Edit1"
    then enter text for "Custom attributes" with value "Attribute2"
    then click on button "Save"
    when text "Custom attributes Attribute2" is visible



  @SIMCustomAttributes_ADD_ATTR_TO_SIM
  Scenario: Add custom attributes to a SIM - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    then click on button "Edit"
    then enter text for "Attribute2" with value "SIM1"
    then click on button "Save"
    when text "SIM1" is visible

  @SIMCustomAttributes_ATTR_SEARCH_SIM
  Scenario: Search SIM using custom attributes - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "Attribute2" with value "SIM1"
    then click on button "Search"
    when link "111117500000013" is visible


  @SIMCustomAttributes_CONFIGURE_ATTR_TO_SIM
  Scenario: Configure custom attributes for search a SIM - Customer User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    then click on link "Automation3 as Customer Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    then click on button "Edit"
    then enter text for "Attribute2" with value "SIM1"
    then click on button "Save"
    when text "SIM1" is visible
    when click on menu "Devices"
    then click on link "All devices"
    when text "Attribute2" is visible

   @SIMCustomAttributes_view_custom_attr_for_SIM
   Scenario: View Custom attributes for SIM - OPCO User
    given start test case
    given open browser
    when login into Portal
    then click on link "PPVGE as Operator Administrator"
    when click on menu "Devices"
    then click on link "All devices"
    then enter text for "IMSI" with value "111117500000013"
    then click on button "Search"
    then click on link "111117500000013"
    when text "Attribute2" and "SIM1" is visible
