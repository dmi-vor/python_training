from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.goto_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.goto_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.goto_home_page()
        # select contact by index for editing
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.goto_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.edit_field_value("firstname", contact.firstname)
        self.edit_field_value("middlename", contact.middlename)
        self.edit_field_value("lastname", contact.lastname)
        self.edit_field_value("nickname", contact.nickname)
        self.edit_field_value("title", contact.title)
        self.edit_field_value("company", contact.company)
        self.edit_field_value("address", contact.address)
        self.edit_field_value("home", contact.homephone)
        self.edit_field_value("mobile", contact.mobilephone)
        self.edit_field_value("work", contact.workphone)
        self.edit_field_value("fax", contact.fax)
        self.edit_field_value("email", contact.email_1)
        self.edit_field_value("email2", contact.email_2)
        self.edit_field_value("email3", contact.email_3)
        self.edit_field_value("homepage", contact.homepage)
        self.edit_field_value("address2", contact.address_2)
        self.edit_field_value("phone2", contact.homephone2)
        self.edit_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.goto_home_page()
        # select contact by index
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.goto_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def goto_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.goto_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def edit_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.goto_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.goto_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.goto_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        homephone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       email_1=email_1, email_2=email_2, email_3=email_3,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, homephone2=homephone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text). group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        homephone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, homephone2=homephone2)



