# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Имён", lastname="Фамильярный"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="modСтепан", middlename="modДядя Степа", lastname="modСтепанов", nickname="modКаланча", title="modБывший флотский старшина", company="modЗастава Ильича", address="modДом 8/1 у заставы Ильича", home="mod+7001001001", mobile="mod+7002002002",
                                         work="mod+7003003003", fax="mod+7004004004", email_1="mode.email1@mail.ma", email_2="mode.email2@mail.ma", email_3="mode.email3@mail.ma", homepage="modhttps://www.culture.ru/poems/45240/dyadya-stepa", address_2="modaddress", home_2="modhome", notes="modЗнают взрослые и дети, Весь читающий народ, Что, живя на белом свете, Дядя Стёпа не умрёт!")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
