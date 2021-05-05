# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Степан", lastname="Stepanoff")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Степан", middlename="Дядя Степа", lastname="Степанов", nickname="Каланча", title="Бывший флотский старшина", company="Застава Ильича", address="Дом 8/1 у заставы Ильича", homephone="+7001001001", mobilephone="+7002002002",
                      workphone="+7003003003", fax="+7004004004", email_1="e.email1@mail.ma", email_2="e.email2@mail.ma", email_3="e.email3@mail.ma", homepage="https://www.culture.ru/poems/45240/dyadya-stepa", address_2="address", homephone2="home", notes="Знают взрослые и дети, Весь читающий народ, Что, живя на белом свете, Дядя Стёпа не умрёт!")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
