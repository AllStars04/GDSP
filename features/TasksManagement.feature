Feature: Tasks Management

  @t1
  Scenario: testcase

        given start test case
        given open browser
        when login into portal
        then click on link "PPVGE as Operator Administrator"
        then click on link "Platform as Platform Support & IITC"
        then click on link "Tools"
        then click on link "All tasks"
        when text "Tasks" is visible
        then click on button "Create task"
        when text "Task detail" is visible
        then enter text area for "Description" with value "Test Task"
        then click on button "Create"
        when text "The task was successfully created!" is visible
        then click on link "See task detail"
        when text "Details" is visible
        then logout and close the browser
