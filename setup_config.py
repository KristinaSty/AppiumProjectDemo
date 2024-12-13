from appium.webdriver.webdriver import WebDriver
from appium.options.common import AppiumOptions
from dotenv import load_dotenv
import json
import os

load_dotenv()
CAPS_NAME = os.getenv("CAPS_NAME")
APP_PATH = os.getenv("APP_PATH")
APPIUM_SERVER = os.getenv("APPIUM_SERVER")

def get_json_data(path):
    fh = open(path, 'r')
    text = fh.read()
    return json.loads(text)

class Setup:
    driver: WebDriver = None

    @classmethod
    def start_app(cls):
        caps_data = get_json_data('desired_caps.json')
        caps_data[CAPS_NAME]['app'] = APP_PATH

        options = AppiumOptions()
        options.load_capabilities(caps_data[CAPS_NAME])
        cls.driver = WebDriver(command_executor=APPIUM_SERVER, options=options)

        return cls.driver

    @classmethod
    def quit(cls):
        if cls.driver:
            cls.driver.quit()

