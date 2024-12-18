from setup_config import Setup
from test_actions import Actions


if __name__ == "__main__":
    driver = Setup.start_app()
    action = Actions(driver)

    #action.click_by_accessibility_id()
    #action.click_element_by_xpath()
    #action.send_text("Location")
    #action.click_by_ui_selector()
    #action.find_elements_in_the_list()
    #action.create_contact("First", "Name", "Test", "1234567")
    #action.scroll_into_view('Downloads')
    #action.scroll_up("Gboard", "Chrome")
    #action.horizontal_scroll()
    #action.swipe_element()
    #action.drag_and_drop_element()
    #action.long_press_element_w3c("First Name")
    #action.long_press_execute_script("First Name")
    #action.tap_execute_script("First Name")
    #action.drag_element_exercise()
    #action.open_mobile_web_application('22')

    Setup.quit()

