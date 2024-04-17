from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutomationPracticePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_word_and_select_country(self, word, country):
        input_fieldme_xpath = f"//android.widget.EditText[@resource-id="autocomplete"]"
        input_fieldme = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, input_fieldme_xpath)))
        input_fieldme.click()
        input_fieldme.send_keys('me')

        countryNameme= "Mexico"
        country_optionme_xpath = f"//android.widget.TextView[contains(@text, '{countryNameme}')]"
        country_optionme = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, country_optionme_xpath)))
        country_optionme.click()

        input_fielduni = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, input_fieldme_xpath)))
        input_fielduni.click()
        input_fielduni.clear()
        input_fielduni.send_keys('uni')

        countryNameuni= "United States USA"
        country_optionuni_xpath = f"//android.widget.TextView[contains(@text, '{countryNameuni}')]"
        country_optionuni = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, country_optionuni_xpath)))
        country_optionuni.click()

        input_fielduni2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, input_fieldme_xpath)))
        input_fielduni2.click()
        input_fielduni2.clear()
        input_fielduni2.send_keys('uni')

        countryNameuni2= "United Arab Emirates"
        country_optionuni2_xpath = f"//android.widget.TextView[contains(@text, '{countryNameuni2}')]"
        country_optionuni2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, country_optionuni2_xpath)))
        country_optionuni2.click()


    def select_dropdown_option(self, option):
        dropdown_xpath = f"//android.view.View[@resource-id="dropdown-class-example"]"
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, dropdown_xpath)))
        dropdown.click()

        option2_xpath = f"//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Option2"]']"
        dropdown_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option2_xpath)))
        dropdown_option.click()

        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, dropdown_xpath)))
        dropdown.click()

        option3_xpath = f"//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Option3"]']"
        dropdown_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option3_xpath)))
        dropdown_option.click()

    def click_open_window_button(self):
        window_button_xpath = f"//android.widget.Button[@resource-id="openwindow"]"
        window_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, window_button_xpath)))
        window_button.click()

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    def switch_to_main_window(self):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def click_open_tab_button(self):
        tab_button_xpath = f"//android.view.View[@content-desc="Open Tab"]"
        tab_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, tab_button_xpath)))
        tab_button.click()

    def scroll_to_button_in_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
    
    def take_screenshot(self):
        try:
            filename = "switchTabExample.png"
            self.driver.save_screenshot(filename)
            print(f"Screenshot saved as: '{filename}'")
        except Exception as e:
            print(f"Error taking screenshot: {e}")

    def select_alert_options_alert(self):
        alert_example_xpath = f"//android.widget.EditText[@resource-id="name"]"
        alert_example = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, alert_example_xpath)))
        alert_example.click()
        alert_example.send_keys('Stori Card')

        button_alert_xpath = f"//android.widget.Button[@resource-id="alertbtn"]" 
        alert_example = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, button_alert_xpath)))
        alert_example.click()

        aceptar_xpath = f"//android.widget.Button[@resource-id="com.android.chrome:id/positive_button"]"
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        print("Text in the pop-up:", alert_text)
        
        aceptar_alert = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, aceptar_xpath)))
        aceptar_alert.click()

    def select_alert_options_confirm(self):
        alert_example2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, alert_example_xpath)))
        alert_example2.click()
        alert_example2.send_keys('Stori Card')

        button_confirm_xpath = f"//android.widget.Button[@resource-id="confirmbtn"]" 
        button_confirm = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, button_confirm_xpath)))
        button_confirm.click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        print("Text in the pop-up: ", alert_text)
        
        aceptar_alert = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, aceptar_xpath)))
        aceptar_alert.click()


    def print_price_table(self):
        table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.GridView[@resource-id="product"]")))
        rows = table.find_elements(By.TAG_NAME, "tr") 
        count_25 = 0
        count_15 = 0
    for row in rows[1:]:  
        cells = row.find_elements(By.TAG_NAME, "td")
        instructor = cells[0].text
        course = cells[1].text
        price = int(cells[2].text)
    
    print(f"Instructor: {instructor}, Course: {course}, Price: ${price}")
    
        if price == 25:
           count_25 += 1
        elif price == 15:
           count_15 += 1

    print(f"Number of courses costing $25: {count_25}")
    print(f"Number of courses costing $15: {count_15}")

    def print_engineers_names (self):
       table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.GridView[@resource-id="product"]")))
       engineers_names = driver.find_elements(By.XPATH, "//android.widget.GridView[@resource-id="product"][contains(text(), 'Engineer')]/preceding-sibling::td[1]")
       print("Name of the engineers: ")
       for name in engineers_names:
       print(name.text)

    def print_businessmans_names (self):
       businessmans_names = driver.find_elements(By.XPATH, "//android.widget.GridView[@resource-id="product"][contains(text(), 'Businessman')]/preceding-sibling::td[1]")
       print("Name of the businessmans:")
       for name in businessmans_names:
       print(name.text)
    
    def search_text_iframe (self):
       select_iframe = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f"(//android.view.View[@text="iFrame Example"])[2]")))
       select_iframe.click()
       
       text_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f"//android.view.View[@text="Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy"]/android.view.View/android.view.View/android.view.View[3][contains(text(), 'His mentorship program is most after in the software testing community with long waiting period.')]")))
    
       for element in text_elements:
          print(element.text)
    
        text_to_find = "His mentorship program is most after in the software testing community with long waiting period."