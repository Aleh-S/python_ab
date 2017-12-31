# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.fill_new_contact_data(Contact(firstname="Aleh", lastname="Shybaila", title="QA", company="BBB",
                               address="123 Main Str, Cupertino, CA 95014", hometel="(408)111-2222",
                               mobile="(408)111-3333", worktel="(408)111-4444", fax="(408)111-5555",
                               email="aleh123@gmail.com", email2="aleh345@gmail.com", email3="aleh789@gmail.com",
                               address2="N/A", phone2="N/A", notes="Some notes."))
    app.open_details_page()
    app.session.logout()

