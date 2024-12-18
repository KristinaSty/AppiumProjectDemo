from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Actions:
    def __init__(self, driver: WebDriver):
        self.driver = driver

# Define actions

    # Find element by accessibility id -> "api_demos_debug_caps"
    def click_by_accessibility_id(self):
        element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App')
        element.click()


    # Find element by XPATH using content-desc -> "api_demos_debug_caps"
    def click_element_by_xpath(self):
        element = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Views"]')
        element.click()


    # Send key -> "settings_caps"
    def send_text(self, text):
        search = self.driver.find_element(AppiumBy.ID, 'com.android.settings:id/search_action_bar_title')
        search.click()
        self.driver.implicitly_wait(2)
        search_field = self.driver.find_element(AppiumBy.ID, 'com.google.android.settings.intelligence:id/open_search_view_edit_text')
        search_field.send_keys(text)


    # Dismiss "Drag and drop" dialogs:
    def dismiss_alerts_drag_and_drop(self):
        if self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/continue_button').is_displayed():
            self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/continue_button').click()
            self.driver.implicitly_wait(2)
        if self.driver.find_element(AppiumBy.ID, 'android:id/button1').is_displayed():
            self.driver.find_element(AppiumBy.ID, 'android:id/button1').click()


    # Find element by ANDROID UIAUTOMATOR -> "drag_and_drop"
    def click_by_ui_selector(self):
        Actions.dismiss_alerts_drag_and_drop(self)
        single_choice_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                        'new UiSelector().text("Single-choice mode")')
        single_choice_button.click()
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Wayne Shorter")').is_displayed(), 'Wayne Shorter is not displayed in the list.'


    # Find element/s by className -> "drag_and_drop"
    def find_elements_in_the_list(self):
        Actions.dismiss_alerts_drag_and_drop(self)
        warp = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Warp")')
        warp.click()
        warp_elements = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        for element in warp_elements:
            if element.get_attribute('text') == "Warp":
                continue
            else:
                element_text = element.get_attribute('text')
                print(element_text)


    # For exercise -> "contacts_caps"
    def create_contact(self, first_name, surname, company, phone):
        self.driver.implicitly_wait(5)
        add_contact_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Create contact')
        add_contact_btn.click()

        first_name_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                        'new UiSelector().text("First name")')
        surname_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Last name")')
        company_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Company")')
        phone_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone")')
        save_button = self.driver.find_element(AppiumBy.ID, 'com.google.android.contacts:id/toolbar_button')

        first_name_input.send_keys(first_name)
        surname_input.send_keys(surname)
        company_input.send_keys(company)
        phone_input.send_keys(phone)
        save_button.click()

        self.driver.implicitly_wait(2)
        # Assert
        close_pop_up = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close Popup Window')
        close_pop_up.click()

        contact_name = self.driver.find_element(AppiumBy.ID, 'com.google.android.contacts:id/large_title')
        text = contact_name.get_attribute('text')
        names = first_name + " " + surname
        if text == names:
            print("Successful creation!")

        # Delete the contact
        more_options = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
        more_options.click()

        delete_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete")')
        delete_btn.click()

        delete_dialog_ok = self.driver.find_element(AppiumBy.ID, 'android:id/button1')
        delete_dialog_ok.click()

#------------------------------------------------------------------------

    # Dismiss "Scroll demo" dialogs
    def dismiss_alerts_scroll(self):
        if self.driver.find_element(AppiumBy.ID, 'android:id/button1').is_displayed():
            self.driver.find_element(AppiumBy.ID, 'android:id/button1').click()
        self.driver.implicitly_wait(2)
        if self.driver.find_element(AppiumBy.ID, 'android:id/button1').is_displayed():
            self.driver.find_element(AppiumBy.ID, 'android:id/button1').click()


    # Scroll (scrollIntoView) -> "scroll_demo"
    def scroll_into_view(self, text):
        Actions.dismiss_alerts_scroll(self)

        scrollable_ui_selector =(
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )
        downloads_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui_selector)


    # Vertical scroll up (setAsVerticalList) -> "apk_demos_caps" / change the APP_PATH to Swipe
    def scroll_up(self, down, up):
        Actions.dismiss_alerts_scroll(self)

        scrollable_ui_selector = (
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.setAsVerticalList().scrollIntoView(new UiSelector().text("{down}"))'
        )

        down_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui_selector)

        scrollable_ui_selector_up =(
            f'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollBackward()'
            f'.scrollIntoView(new UiSelector().text("{up}"))'
        )

        up_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui_selector_up)


    # Horizontal scroll -> "apk_demos_caps"
    def horizontal_scroll(self):
        views_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views')
        views_button.click()

        gallery_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Gallery')
        gallery_button.click()

        photos_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1. Photos')
        photos_button.click()

        scrollable_ui_selector_right = (
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.setAsHorizontalList().scrollIntoView(new UiSelector()'
            f'.className("android.widget.ImageView").instance(4))'
        )
        right_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui_selector_right)

        scrollable_ui_selector_left = (
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.setAsHorizontalList().scrollBackward().scrollIntoView(new UiSelector()'
            f'.className("android.widget.ImageView").instance(0))'
        )
        left_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui_selector_left)


    def scroll_to_the_bottom(self):
        scrollable_list = self.driver.find_element(AppiumBy.ID, 'android:id/list')
        while True:
            previous_page_source = self.driver.page_source
            self.driver.execute_script("mobile: scrollGesture", {
                "elementId": scrollable_list.id,
                "direction": "down",
                "percent": 0.8
            })
            if previous_page_source == self.driver.page_source:
                break


    # Swipe -> "apk_demos_caps" / change the APP_PATH to Swipe
    def swipe_element(self):
        Actions.dismiss_alerts_scroll(self)

        element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Android Setup")')

        location = element.location
        size = element.size

        start_x = location['x'] + size['width'] - 10
        start_y = location['y'] + size['height'] // 2
        end_x = location['x'] + 10

        # Create and instance of ActionChains
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, start_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        self.driver.implicitly_wait(2)


    # Drag and drop -> "drag_and_drop"
    def drag_and_drop_element(self):
        Actions.dismiss_alerts_drag_and_drop(self)
        single_choice_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Single-choice mode")')
        single_choice_button.click()

        element_to_drag = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.mobeta.android.demodslv:id/drag_handle").instance(1)')
        element_to_drop = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.mobeta.android.demodslv:id/drag_handle").instance(6)')

        actions = ActionChains(self.driver)
        # actions.drag_and_drop(element_to_drag, element_to_drop).perform()
        actions.click_and_hold(element_to_drag)
        actions.move_to_element(element_to_drop)
        actions.release()
        actions.perform()

        title = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Single-choice list")')
        assert title.is_displayed()


    # Tap and Long press -> "contacts_caps"

    def long_press_execute_script(self, contact):
        element_to_press = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, contact)
        self.driver.execute_script("mobile: longClickGesture",{
            "elementId": element_to_press.id
        })
        selections = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1 selected")')
        assert selections.is_displayed()


    def tap_execute_script(self, contact):
        element_to_tap = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, contact)
        self.driver.execute_script("mobile: clickGesture", {
            "elementId": element_to_tap.id
        })
        self.driver.implicitly_wait(2)
        close_pop_up = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close Popup Window')
        close_pop_up.click()

        contact_name = self.driver.find_element(AppiumBy.ID, 'com.google.android.contacts:id/large_title')
        text = contact_name.get_attribute('text')
        names = contact
        if text == names:
            print("Successful creation!")


    # For exercise -> "drag_and_drop_caps"
    def drag_element_exercise(self):
        Actions.dismiss_alerts_drag_and_drop(self)
        multiple_choice_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                        'new UiSelector().text("Multiple-choice mode")')
        multiple_choice_button.click()

        #Actions.scroll_to_the_bottom(self) -> scroll to the bottom
        scrollable_ui_selector = (
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.setAsVerticalList().scrollIntoView(new UiSelector().text("McCoy Tyner"))'
        )
        scroll_to_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui_selector)


        element_to_tap = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("McCoy Tyner")')
        self.driver.execute_script("mobile: clickGesture", {
            "elementId": element_to_tap.id
        })

        element_to_drag = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   'new UiSelector().resourceId("com.mobeta.android.demodslv:id/drag_handle").instance(7)')
        element_to_drop = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   'new UiSelector().resourceId("com.mobeta.android.demodslv:id/drag_handle").instance(2)')
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_to_drag, element_to_drop).perform()

        check_if_selected = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("McCoy Tyner")')
        checked_attr = check_if_selected.get_attribute('checked')
        if checked_attr == 'true':
            print("The correct button is checked.")
        else:
            print("The correct button is not checked!")


#------------------------------------------------------------------------

    # Wait web page to load
    def wait_for_page_load(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.driver.execute_script("return document.readyState") == "complete"
        )

    # Mobile browser - "chrome_browser"
    def open_mobile_web_application(self, expected_price):
        self.driver.get("https://amazon.com/")
        self.driver.switch_to.context('CHROMIUM')

        search_field = self.driver.find_element(AppiumBy.XPATH, '//input[@name="k"]')
        search_field.send_keys("puzzle")
        go_btn = self.driver.find_element(AppiumBy.XPATH, '//input[@value="Go"]')
        go_btn.click()

        self.wait_for_page_load()
        target_element_xpath = '//span[contains(text(), "Big Rock City • 1000-Piece Jigsaw Puzzle from The Magic Puzzle Company • Series Four")]'
        WebDriverWait(self.driver, 20).until(
            lambda driver: self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'}); return true;",
                self.driver.find_element(AppiumBy.XPATH, target_element_xpath)
            )
        )
        target_element = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((AppiumBy.XPATH, target_element_xpath))
        )
        target_element.click()

        self.wait_for_page_load()
        dismiss_dialog = self.driver.find_element(AppiumBy.XPATH, '//input[@data-action-type="DISMISS"]')
        dismiss_dialog.click()


        price_xpath = self.driver.find_element(AppiumBy.XPATH, '//span[@class="a-price-whole"]')
        price_text = price_xpath.text

        assert price_text == expected_price, "The price is incorrect!"


