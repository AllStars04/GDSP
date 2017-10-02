Feature: GHRL Templates

    @TC_SearchGHRLTemp
    Scenario: GHRL Template _ Platform User_Overview Page - Search GHRL Template

        given start test case
        given open browser
        when login into portal
        then click on link "Username as Operator Administrator"
        then click on link "Platform as Platform Support & IITC"
        #Goto GHLR Template
        then click on link "Administration"
        then click on link "GHLR templates"
        when text "GHLR templates" is visible
        then click on link "Clear fields"
        #Search with Default Values
        then click on button "Search"
        when text "matching result" is visible
        then report info "SUCCESS: GHLR Template results are displayed"
        #Search with Invalid Values
        then enter text for "GHLRtemp" with value "+**+"
        then click on button "Search"
        when text "Please enter only alphabetical characters, numbers and/or _-" is visible
        then report info "SUCCESS: Not possible to search for GHLR Template with invalid values "
        then logout and close the browser

