Feature: Test Automation Practice Page
  Scenario: Enter words and select country in suggestion Class Example
    Given: User opens the desired browser in the mobile device or emulator
    When: User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And: User enters the word "Me" in the suggestion class input field
    And: User selects "Mexico" from the suggestion dropdown
    And: User enters the word "Uni" in the suggestion class input field again
    And: User selects "United States (USA)" from the suggestion dropdown
    And: User writes "Uni" in the suggestion class input field again
    And: User selects "United Arab Emirates" from the suggestion dropdown
    Then: The suggestions should be selected successfully

  Scenario: Select options in Dropdown Example
    Given: User opens the desired browser in the mobile device or emulator
    When: User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And: User selects "Option 2" from the dropdown example
    And: User selects "Option 3" from the dropdown example
    Then: The dropdown options should be changed successfully

  Scenario: Select switch Window Example and validate text
    Given: User opens the desired browser in the mobile device or emulator
    When: User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And: User clicks the "Open Window" button in the Switch Window Example section
    Then: The 30 day money back guarantee text should be shown
    And: If the text is not shown, fail the test and close the opened window

  Scenario: Select switch Tab Example and take a screenshot
    Given: User opens the desired browser in the mobile device or emulator
    When: User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And: User clicks the "Open Tab" button in the Switch Tab Example section
    And: User switches to the new tab
    And: User scrolls until the button below is visible
    Then: Take a screenshot including the button and save it with the name of the test case
    And: User does not close the window and returns to the first window

  Scenario: Select buttons Switch Alert Example
    Given:User opens the desired browser in the mobile device or emulator
    When:User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And:User locates the Switch To Alert Example section
    And:User types the text 'Stori Card'
    And:User clicks the "Alert" button in the the Switch To Alert Example section
    And:User prints the text on the pop-up and clicks the "Aceptar" button
    And:User clicks the "confirm" button in the the Switch To Alert Example section
    And:User clicks the "Aceptar" button
    Then:User selects buttons in the the Switch To Alert Example section
    And:User selects buttons in the pop-up

  Scenario: Print information the Web Table Example
    Given:User opens the desired browser in the mobile device or emulator
    When:User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And:User locates the Web Table Example section
    And:User prints how many courses cost $25 and $15 and their names
    Then:The required information should be printed successfully

  Scenario: Print names in web table with fixed header
    Given: The user opens the web page
    When:User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And: The user finds the web table with fixed header
    Then: The user prints the names of all engineers
    And: The user prints the names of all businessmen
  
  Scenario: Extract blue highlighted text from iFrame
    Given: The user navigates to the iFrame example
    When:User navigates to the "https://rahulshettyacademy.com/AutomationPractice/" page
    And: The user switches to the iFrame
    Then: The user extracts and prints the text highlighted in blue
    And: Only the text from odd indexes should be printed