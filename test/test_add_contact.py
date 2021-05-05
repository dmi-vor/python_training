# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def test_add_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Степан", lastname="Stepanoff")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="Степан", lastname="Stepanoff")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 20),
            address=random_string("address", 50), homephone=random_string("hphone", 10), mobilephone=random_string("mphone", 10),
            workphone=random_string("wphone", 10), fax=random_string("fax", 10), email_1=random_string("email1", 10),
            email_2=random_string("email2", 10), email_3=random_string("email3", 10), homepage=random_string("https://www.", 10),
            address_2=random_string("address", 100), homephone2=random_string("hphone2", 10), notes=random_string("name", 500))
    for i in range(5)
]


@pytest.mark.parametrize("contact",testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="Степан", middlename="Дядя Степа", lastname="Степанов", nickname="Каланча", title="Бывший флотский старшина", company="Застава Ильича", address="Дом 8/1 у заставы Ильича", homephone="+7001001001", mobilephone="+7002002002",
#                      workphone="+7003003003", fax="+7004004004", email_1="e.email1@mail.ma", email_2="e.email2@mail.ma", email_3="e.email3@mail.ma", homepage="https://www.culture.ru/poems/45240/dyadya-stepa", address_2="address", homephone2="home", notes="Знают взрослые и дети, Весь читающий народ, Что, живя на белом свете, Дядя Стёпа не умрёт!")
#    app.contact.create(contact)
#    assert len(old_contacts) + 1 == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)