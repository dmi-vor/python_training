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

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.goto_home_page()
        # select first contact for editing
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.goto_home_page()

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
        wd = self.app.wd
        self.goto_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.goto_home_page()

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