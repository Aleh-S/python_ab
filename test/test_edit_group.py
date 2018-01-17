from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group2", header="group2_header", footer="group2_footer"))
    app.session.logout()
    