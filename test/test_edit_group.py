# -*- coding: utf-8 -*-
from model.group import Group


#def test_edit_group(app):
#        app.session.login(username="admin", password="secret")
#        app.group.edit_first_group(Group(name="modA", header="modB", footer="modC"))
#        app.session.logout()


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="modA")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
