Feature: Serving Networks

    @TC_OPGrpUserViewServiceNetworksDetail
    Scenario:  Operator Group User - Serving networks detail

        given start test case
        given open browser
        when login into portal
        #Goto Service Network
        then click on link "Administration"
        then click on link "Serving networks"
        when text "Serving networks" is visible
        #Search And Click on Service Network
        then enter text for "ServingNetworkCode" with value "100"
        then click on button "Search"
        then click on link "100"
        #Validate Information Panel
        when text "Information" is visible
        when text "Code" is visible
        when text "Network name" is visible
        when text "Country" is visible
        when text "See related portal interactions" is visible
        then report info "SUCCESS: The Information Panel Content is Displayed Correctly"
        #Validate Network Panel
        when text "Network" is visible
        when text "MCC-MNC" is visible
        when text "TADIG Code" is visible
        then report info "SUCCESS: The Network Panel Content is Displayed Correctly"
        then logout and close the browser
