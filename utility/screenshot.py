import os
from datetime import datetime
from utility.logging_log import Log_store

class ScreenshotCapture:
    @staticmethod
    def screenshot_capture(driver,screenshot_name):

        folder_path = os.path.abspath(os.getcwd() + "/" + "screenshots")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = folder_path + "/" + screenshot_name + "_" + timestamp + ".png"

        #store log
        log= Log_store.get_log(__name__)
        log.debug("start capturing failure screenshot")

        driver.save_screenshot(filepath)

        log.debug("screenshot taken successfully")
        log.debug(f"Screenshot saved at: {filepath}")
        print(f" Screenshot path: {filepath}")
