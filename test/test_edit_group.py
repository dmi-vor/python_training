# -*- coding: utf-8 -*-
from model.group import Group
import random


#def test_edit_group(app):
#        app.session.login(username="admin", password="secret")
#        app.group.edit_first_group(Group(name="modA", header="modB", footer="modC"))
#        app.session.logout()


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = Group(name="modA")
    group.id = random.choice(old_groups).id
    app.group.edit_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
