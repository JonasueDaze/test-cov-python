from threading import Thread
import unittest

from app import create_app
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPeopleCrud(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        app = create_app()
        app.config["TESTING"] = True

        def start_flask_server():
            app.run()

        # Start the Flask server in a separate thread
        thread = Thread(target=start_flask_server)
        thread.daemon = True
        thread.start()

        # Wait for the server to start
        # Add any necessary additional wait time or checks here
        # For simplicity, we'll use a static wait time in this example
        import time
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_people_crud(self):
        url = "http://localhost:5000/"
        self.driver.get(url)
        self.driver.set_window_size(1050, 708)
        self.driver.find_element(By.LINK_TEXT, "+ Add").click()
        self.driver.find_element(By.ID, "personName").click()
        self.driver.find_element(By.ID, "personName").send_keys("test")
        self.driver.find_element(By.ID, "personAge").send_keys("20")
        self.driver.find_element(By.ID, "submitBtn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
        self.driver.find_element(By.ID, "personAge").click()
        self.driver.find_element(By.ID, "personAge").send_keys("30")
        self.driver.find_element(By.ID, "submitBtn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
