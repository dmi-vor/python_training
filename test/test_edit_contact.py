# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Имён", lastname="Фамильярный"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="modСтепан", middlename="modДядя Степа", lastname="modСтепанов", nickname="modКаланча", title="modБывший флотский старшина", company="modЗастава Ильича", address="modДом 8/1 у заставы Ильича", homephone="mod+7001001001", mobilephone="mod+7002002002",
                      workphone="mod+7003003003", fax="mod+7004004004", email_1="mode.email1@mail.ma", email_2="mode.email2@mail.ma", email_3="mode.email3@mail.ma", homepage="modhttps://www.culture.ru/poems/45240/dyadya-stepa", address_2="modaddress", homephone2="modhome", notes="modЗнают взрослые и дети, Весь читающий народ, Что, живя на белом свете, Дядя Стёпа не умрёт!")
    contact.id = random.choice(old_contacts).id
    app.contact.edit_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)