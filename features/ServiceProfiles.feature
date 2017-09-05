Feature: Service Profile

    @TC_ValidateSerivceProfPageContents
    Scenario: Check Service Profile Page Access and Contents Validation-Operator User

        given start test case
        given open browser
        when login into portal
        then click on link "Administration"
        then click on link "Service profiles"
        when text "service profiles" is visible
        when text "Organisation" is visible
        when text "Service Profile" is visible
        then validate table headers "Service profile,Description,Organisation,Parent organisation,Number of SIMs" for table "ServiceProf"
        then logout and close the browser

    @TC_OperatorSearchServiceProfile
    Scenario: Search For Service Profiles - Operator  User

        given start test case
        given open browser
        when login into portal
        #Goto Service profile
        then click on link "Administration"
        then click on link "Service profiles"
        when text "Service profiles" is visible
        then get value from label "Service Profile" and store it in "value1"
        #Search Service Profile
        then enter text for "Service Profile" with value "BMW_IT"
        then click on button "Search"
        when text "matching result" is visible
        then report info "SUCCESS : Operator is able to search service profile for organization"
        #Clear Fields And Validate
        then click on link "Clear fields"
        then get value from label "Service Profile" and store it in "value2"
        then check if values "value1" and "value2" are "equal"
        then report info "SUCCESS : Clear Fields set the Searchable fields to default values"
        then logout and close the browser
