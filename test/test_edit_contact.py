# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_group(Contact(firstname="modСтепан", middlename="modДядя Степа", lastname="modСтепанов", nickname="modКаланча", title="modБывший флотский старшина", company="modЗастава Ильича", address="modДом 8/1 у заставы Ильича", home="mod+7001001001", mobile="mod+7002002002",
                                         work="mod+7003003003", fax="mod+7004004004", email_1="mode.email1@mail.ma", email_2="mode.email2@mail.ma", email_3="mode.email3@mail.ma", homepage="modhttps://www.culture.ru/poems/45240/dyadya-stepa", address_2="modaddress", home_2="modhome", notes="modЗнают взрослые и дети, Весь читающий народ, Что, живя на белом свете, Дядя Стёпа не умрёт!"))
    app.session.logout()