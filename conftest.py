import pytest
from addressbook_api import AddressBook
from models.group import Group


@pytest.fixture(scope="session")
def app():
    app = AddressBook()
    app.open_main_page()
    yield app
    app.destroy()


@pytest.fixture()
def init_login(app):
    if not app.is_logged():
        app.login(username="admin", password="secret")
    yield
    app.logout()


@pytest.fixture()
def init_group(app, init_login):
    if not app.is_groups_present():
        app.create_group(Group(name="Test"))
