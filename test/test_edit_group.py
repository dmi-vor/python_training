# -*- coding: utf-8 -*-
from model.group import Group


#def test_edit_group(app):
#        app.session.login(username="admin", password="secret")
#        app.group.edit_first_group(Group(name="modA", header="modB", footer="modC"))
#        app.session.logout()


def test_edit_group_name(app):
        app.session.login(username="admin", password="secret")
        app.group.edit_first_group(Group(name="modA"))
        app.session.logout()