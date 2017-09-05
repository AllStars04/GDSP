Feature: Provisionning Profiles - Operation Group User

    @TC_EditAPNForAnyPP
    Scenario: Edit Provisitiong Profiles with Valid Data And exist APN - Operator group User

        given start test case
        given open browser
        when login into portal
        #Search For PP
        then click on link "Administration"
        then click on link "Provisioning profiles"
        when text "Provisioning profiles" is visible
        then enter text for "Provisioning profile" with value "autotest2"
        then click on button "Search"
        when text "matching result" is visible
        #Open the PP Details
        then click on link "Autotest2"
        when text "Configuration" is visible
        then click on button "ConfigEdit"
        #Edit APN for PP
        then select drop down "APN" with option "apn1"
        then click on button "Save"
        when text "Settings successfully updated" is visible
        then report info "SUCCESS : Operator is able to edit the APN for Provisitiong Profiles"
        #Revert the Changes
        then click on button "ConfigEdit"
        then select drop down "APN" with option "centraltest"
        then click on button "Save"
        when text "Settings successfully updated" is visible
        then logout and close the browser



