from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None,
                 nickname=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, fax=None,
                 email_1=None, email_2=None, email_3=None, homepage=None,
                 address_2=None, homephone2=None, notes=None, all_emails_from_homepage=None, all_phones_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.address_2 = address_2
        self.homephone2 = homephone2
        self.notes = notes
        self.all_emails_from_homepage = all_emails_from_homepage
        self.all_phones_from_homepage = all_phones_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
