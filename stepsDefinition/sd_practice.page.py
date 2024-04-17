from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from pageObjects.po_practice_page import AutomationPracticePage
import pytest

@given('User opens the desired browser in the mobile device or emulator')
def open_browser(context):
    pass

@when('User navigates to the "{url}" page')
def navigate_to_page(context, url):
    context.page.open_page('https://rahulshettyacademy.com/AutomationPractice/')

@when('User enters the word "{word}" and selects "{country}" in the Suggestion Class Example')
def enter_word_and_select_country(context, word, country):
    context.page.enter_word_and_select_country(word, country)

@when('User selects option "{option}" in the Dropdown Example')
def select_dropdown_option(context, option):
    context.page.select_dropdown_option(option)

@when('User clicks the Open Window button in the Switch Window Example')
def click_open_window_button(context):
    context.page.click_open_window_button()
    context.page.switch_to_new_window()
    context.page.switch_to_main_window()

@then('User verifies the 30 day money back guarantee text is shown')
def verify_guarantee_text(context):
    context.page.click_open_window_button()
    context.page.switch_to_new_window()
    expected_text = "30 day money back guarantee text"
        actual_text_xpath = "//android.widget.TextView[@text="Welcome to QAClick Academy"]"
        actual_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, ))).text
        assert expected_text in actual_text, f"The expected text '{expected_text}' not found in the new window"
    context.page.switch_to_main_window()

@when('User clicks the Open Tab button in the Switch Tab Example')
def click_open_tab_button(context):
    context.page.click_open_tab_button()

@when('User scrolls until the button is visible in the new tab')
def scroll_to_button_in_new_tab(context):
    context.page.scroll_to_button_in_new_tab()

@then('User takes a screenshot including the button and saves it with the test case name')
def take_screenshot_with_button(context):
    context.page.switch_to_new_window()
    context.page.take_screenshot()
    context.page.switch_to_main_window()

@then('User selects buttons in the the Switch To Alert Example section')
def select_buttons_alerts(context):
    context.page.select_alert_options_alert()
    context.page.select_alert_options_confirm()

@then('User prints how many courses cost $25 and $15 and their names')
def print_courses_cost_25_15(context):
    context.page.print_price_table()
    
@then('User prints the names of all the Engineers in the Web Table Fixed header')
def print_engineers_names(context):
    context.page.print_engineers_names()

@then('User prints the names of all the Businessmans in the Web Table Fixed header')
def print_businessmans_names(context):
    context.page.print_businessmans_names()

@then('User search the text in iframe')
def print_search_text_iframe(context):
    context.page.search_text_iframe()

@then('Generate Test Resport')
def pytest_html_report_title(report):
    report.title = "Report of Automation Test"

@then('Generate Test Resport')
def pytest_configure(config):
    config.option.htmlpath = "Reports/test_report.html"