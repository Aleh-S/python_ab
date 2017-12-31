# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary=
                            "C:/Program Files/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)

    def test_test_add_contact(self):
        self.login(username="admin", password="secret")
        self.fill_new_contact_data(Contact(firstname="Aleh", lastname="Shybaila", title="QA", company="BBB",
                                   address="123 Main Str, Cupertino, CA 95014", hometel="(408)111-2222",
                                   mobile="(408)111-3333", worktel="(408)111-4444", fax="(408)111-5555",
                                   email="aleh123@gmail.com", email2="aleh345@gmail.com", email3="aleh789@gmail.com",
                                   address2="N/A", phone2="N/A", notes="Some notes."))
        self.open_details_page()
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def open_details_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def submit_new_contact_creation(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_contact_anniversary(self):
        wd = self.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2005")

    def add_new_contact_birthday(self):
        wd = self.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2004")

    def add_new_contact_photo(self, pathtojpg):
        wd = self.wd
        photo = wd.find_element_by_name("photo")
        photo.send_keys(pathtojpg)

    def fill_new_contact_data(self, contact):
        wd = self.wd
        self.open_new_contact_page()
        # fill text fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.hometel)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.worktel)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # fill not text fields
        self.add_new_contact_photo(pathtojpg="C:\QA\ABarancev\python_ab\\files\\foto1.jpg")
        self.add_new_contact_birthday()
        self.add_new_contact_anniversary()
        self.submit_new_contact_creation()
        self.return_to_homepage()

    def open_new_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
