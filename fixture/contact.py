from model.contact import Contact


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
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
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
        self.edit_field_value("home", contact.home)
        self.edit_field_value("mobile", contact.mobile)
        self.edit_field_value("work", contact.work)
        self.edit_field_value("fax", contact.fax)
        self.edit_field_value("email", contact.email_1)
        self.edit_field_value("email2", contact.email_2)
        self.edit_field_value("email3", contact.email_3)
        self.edit_field_value("homepage", contact.homepage)
        self.edit_field_value("address2", contact.address_2)
        self.edit_field_value("phone2", contact.home_2)
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
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
