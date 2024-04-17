# Stori-QA-Automation-Challenge
Automation project for mobile emulator Android.

Automated Testing Project README
This project is aimed at automating the testing of various functionalities of the "Automation Practice" page hosted at Rahul Shetty Academy(https://rahulshettyacademy.com/AutomationPractice/). The automated tests are designed to run on emulators using the Appium framework with WebdriverIO and Selenium.

Technologies Used:
WebDriverIO-
Appium-
Python-
Behave (BDD framework)-
Selenium

Table of Contents:
Features-
Setup-
Running Tests-
Test Scenarios-
Page Objects-
Step Definitions-
Reporting-
Features

Test Automation: Automate various scenarios such as entering text, selecting options, interacting with alerts, and more.
Cross-Platform Testing: Run tests on both real mobile devices and emulators.
Detailed Reporting: Capture detailed test reports for analysis and debugging.

Setup:
Install Dependencies: Make sure you have Node.js installed. Then, install dependencies by running:

--- npm install
Appium Installation
--- npm install -g appium

Android Emulator Setup: Set up an Android emulator

WebdriverIO Configuration: Update the wdio.conf.js file with appropriate capabilities for your testing environment.
---- npx wdio

Running Tests
To run the tests, execute the following command:
---- npm test

Test Scenarios
The test scenarios cover various functionalities of the "Automation Practice" page. They include:

Entering text and selecting countries from suggestions.
Selecting options from dropdowns.
Interacting with pop-up alerts and windows.
Taking screenshots and validating content.
Parsing and printing data from web tables.
For detailed descriptions of each scenario, refer to the feature files in the features directory.

Page Objects:
The AutomationPracticePage class in pageObjects/po_practice_page.py encapsulates the elements and actions on the "Automation Practice" page. It provides methods to interact with different elements on the page, making test development and maintenance easier.

Step Definitions:
Step definitions in the step_definitions directory map the Given-When-Then steps defined in feature files to corresponding actions and validations in the page object. They use Selenium WebDriver and Appium to interact with elements on the page and perform test actions.

Reporting:
Test execution results are captured using WebdriverIO's built-in reporters. You can find detailed HTML reports in the reports directory after test execution. These reports provide insights into test execution status, failures, and any errors encountered during testing.
