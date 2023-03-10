# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

class TestTEST1():
    def setup_method(self, method):
      self.driver = webdriver.Chrome()
      self.vars = {}

    def teardown_method(self, method):
      self.driver.quit()

    def check(self):
        try:
            self.driver.find_element(By.XPATH, "//div[contains(.,\'Required\')]")
        except NoSuchElementException:
            print("fail")
            return False
        print("success")
        return True

    def test_tEST1(self):
        # Test name: TEST1
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | click | id=id_generalcontainer |
        self.driver.find_element(By.ID, "id_generalcontainer").click()
        # 5 | type | id=id_externalurl | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1
        self.driver.find_element(By.ID, "id_externalurl").send_keys(
            "http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 6 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 7 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">A</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">A</p>")
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">AB</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">AB</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ABC</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>")
        # 10 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">ABC</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>'}",
            element)
        # 11 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST2(self):
        # Test name: TEST2
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | Quang
        self.driver.find_element(By.ID, "id_name").send_keys("ABC")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 7 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">a</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">a</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ab</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">ab</p>")
        # 10 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">abc</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">abc</p>")
        # 11 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">abc</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">abc</p>'}",
            element)
        # 12 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST3(self):
        # Test name: TEST3
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | quang
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | type | id=id_externalurl | abc
        self.driver.find_element(By.ID, "id_externalurl").send_keys("abc")
        # 7 | click | css=#id_introeditoreditable > p |
        self.driver.find_element(By.CSS_SELECTOR, "#id_introeditoreditable > p").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">a</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">a</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ab</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">ab</p>")
        # 10 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">abc</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">abc</p>")
        # 11 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;" id="yui_3_17_2_1_1671284619332_818">abc</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\" id=\"yui_3_17_2_1_1671284619332_818\">abc</p>'}",
            element)
        # 12 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST4(self):
        # Test name: TEST4
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | quang
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | type | id=id_externalurl | 123
        self.driver.find_element(By.ID, "id_externalurl").send_keys("123")
        # 7 | click | css=#id_introeditoreditable > p |
        self.driver.find_element(By.CSS_SELECTOR, "#id_introeditoreditable > p").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">a</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">a</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ab</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">ab</p>")
        # 10 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">abc</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">abc</p>")
        # 11 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;" id="yui_3_17_2_1_1671284649867_814">abc</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\" id=\"yui_3_17_2_1_1671284649867_814\">abc</p>'}",
            element)
        # 12 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST5(self):
        # Test name: TEST5
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 908x824 |
        self.driver.set_window_size(908, 824)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | click | id=id_generalcontainer |
        self.driver.find_element(By.ID, "id_generalcontainer").click()
        # 5 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 6 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 7 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">a</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">a</p>")
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ab</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">ab</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">abc</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">abc</p>")
        # 10 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">abc</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">abc</p>'}",
            element)
        # 11 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST6(self):
        # Test name: TEST6
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 908x824 |
        self.driver.set_window_size(908, 824)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | quang
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | type | id=id_externalurl | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1
        self.driver.find_element(By.ID, "id_externalurl").send_keys(
            "http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 7 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">a</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">a</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ab</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">ab</p>")
        # 10 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">abc</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">abc</p>")
        # 11 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">abc</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">abc</p>'}",
            element)
        # 12 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST7(self):
        # Test name: TEST7
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | QUANG
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | type | id=id_externalurl | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1
        self.driver.find_element(By.ID, "id_externalurl").send_keys(
            "http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 7 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">A</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">A</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">AB</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">AB</p>")
        # 10 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ABC</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>")
        # 11 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">ABC</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>'}",
            element)
        # 12 | click | id=collapseElement-1 |
        self.driver.find_element(By.ID, "collapseElement-1").click()
        # 13 | click | id=id_display |
        self.driver.find_element(By.ID, "id_display").click()
        # 14 | select | id=id_display | label=Embed
        dropdown = self.driver.find_element(By.ID, "id_display")
        dropdown.find_element(By.XPATH, "//option[. = 'Embed']").click()
        # 15 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST8(self):
        # Test name: TEST8
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | QUANG
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | type | id=id_externalurl | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1
        self.driver.find_element(By.ID, "id_externalurl").send_keys(
            "http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 7 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">AB</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">AB</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ABC</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>")
        # 10 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">ABC</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>'}",
            element)
        # 11 | click | id=collapseElement-1 |
        self.driver.find_element(By.ID, "collapseElement-1").click()
        # 12 | click | id=id_display |
        self.driver.find_element(By.ID, "id_display").click()
        # 13 | select | id=id_display | label=Open
        dropdown = self.driver.find_element(By.ID, "id_display")
        dropdown.find_element(By.XPATH, "//option[. = 'Open']").click()
        # 14 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST9(self):
        # Test name: TEST9
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | QUANG
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | type | id=id_externalurl | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1
        self.driver.find_element(By.ID, "id_externalurl").send_keys(
            "http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 7 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 8 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">A</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">A</p>")
        # 9 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">AB</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">AB</p>")
        # 10 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ABC</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>")
        # 11 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">ABC</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">ABC</p>'}",
            element)
        # 12 | click | id=collapseElement-1 |
        self.driver.find_element(By.ID, "collapseElement-1").click()
        # 13 | click | id=id_display |
        self.driver.find_element(By.ID, "id_display").click()
        # 14 | select | id=id_display | label=In pop-up
        dropdown = self.driver.find_element(By.ID, "id_display")
        dropdown.find_element(By.XPATH, "//option[. = 'In pop-up']").click()
        # 15 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

    def test_tEST10(self):
        # Test name: TEST10
        # Step # | name | target | value
        # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
        self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 2 | setWindowSize | 906x822 |
        self.driver.set_window_size(906, 822)
        # 3 | click | id=id_name |
        self.driver.find_element(By.ID, "id_name").click()
        # 4 | type | id=id_name | quang
        self.driver.find_element(By.ID, "id_name").send_keys("abcd")
        # 5 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 6 | click | id=yui_3_17_2_1_1671285087331_805 |
        self.driver.find_element(By.ID, "yui_3_17_2_1_1671285087331_805").click()
        # 7 | type | id=id_externalurl | 7. Apearance ->
        self.driver.find_element(By.ID, "id_externalurl").send_keys("7. Apearance ->")
        # 8 | click | id=id_externalurl |
        self.driver.find_element(By.ID, "id_externalurl").click()
        # 9 | type | id=id_externalurl | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1
        self.driver.find_element(By.ID, "id_externalurl").send_keys(
            "http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
        # 10 | click | id=id_introeditoreditable |
        self.driver.find_element(By.ID, "id_introeditoreditable").click()
        # 11 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">a</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">a</p>")
        # 12 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">ab</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys("<p dir=\"ltr\" style=\"text-align: left;\">ab</p>")
        # 13 | type | id=id_introeditor | <p dir="ltr" style="text-align: left;">abc</p>
        self.driver.find_element(By.ID, "id_introeditor").send_keys(
            "<p dir=\"ltr\" style=\"text-align: left;\">abc</p>")
        # 14 | editContent | id=id_introeditoreditable | <p dir="ltr" style="text-align: left;">abc</p>
        element = self.driver.find_element(By.ID, "id_introeditoreditable")
        self.driver.execute_script(
            "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p dir=\"ltr\" style=\"text-align: left;\">abc</p>'}",
            element)
        # 15 | click | id=collapseElement-1 |
        self.driver.find_element(By.ID, "collapseElement-1").click()
        # 16 | click | id=id_display |
        self.driver.find_element(By.ID, "id_display").click()
        # 17 | select | id=id_display | label=In pop-up
        dropdown = self.driver.find_element(By.ID, "id_display")
        dropdown.find_element(By.XPATH, "//option[. = 'In pop-up']").click()
        # 18 | click | id=id_popupwidth |
        self.driver.find_element(By.ID, "id_popupwidth").click()
        # 19 | type | id=id_popupwidth | 600
        self.driver.find_element(By.ID, "id_popupwidth").send_keys("600")
        # 20 | click | id=id_popupheight |
        self.driver.find_element(By.ID, "id_popupheight").click()
        # 21 | type | id=id_popupheight | 400
        self.driver.find_element(By.ID, "id_popupheight").send_keys("400")
        # 22 | click | id=id_submitbutton2 |
        self.driver.find_element(By.ID, "id_submitbutton2").click()

  def test_tEST11(self):
    # Test name: TEST11
    # Step # | name | target | value
    # 1 | open | http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1 |
    self.driver.get("http://localhost/moodle/course/modedit.php?sr=1&add=url&section=1&course=1")
    # 2 | setWindowSize | 906x822 |
    self.driver.set_window_size(906, 822)
    # 3 | click | id=id_submitbutton2 |
    self.driver.find_element(By.ID, "id_submitbutton2").click()

def Test(method):
    tester.setup_method(None)
    method()
    tester.teardown_method(None)

print("Test 1: ")
tester = TestTEST1()
Test(tester.test_tEST1)
print("Test 2: ")
Test(tester.test_tEST2)
print("Test 3: ")
Test(tester.test_tEST3)
print("Test 4: ")
Test(tester.test_tEST4)
print("Test 5: ")
Test(tester.test_tEST5)
print("Test 6: ")
Test(tester.test_tEST6)
print("Test 7: ")
Test(tester.test_tEST7)
print("Test 8: ")
Test(tester.test_tEST8)
print("Test 9: ")
Test(tester.test_tEST9)
print("Test 10: ")
Test(tester.test_tEST10)
print("Test 11: ")
Test(tester.test_tEST11)