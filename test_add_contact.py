# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Степан", middlename="Дядя Степа", lastname="Степанов", nickname="Каланча", title="Бывший флотский старшина", company="Застава Ильича", address="Дом 8/1 у заставы Ильича", home="+7001001001", mobile="+7002002002",
                            work="+7003003003", fax="+7004004004", email_1="e.email1@mail.ma", email_2="e.email2@mail.ma", email_3="e.email3@mail.ma", homepage="https://www.culture.ru/poems/45240/dyadya-stepa", address_2="address", home_2="home", notes="Знают взрослые и дети, Весь читающий народ, Что, живя на белом свете, Дядя Стёпа не умрёт!"))
    app.logout()
