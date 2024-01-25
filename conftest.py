import pytest

from modules.api.clients.github import GitHub
from modules.common.database import Database


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Yevheniia"
        self.second_name = "Dolhopolova"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

import pytest

class User: 

    def __init__(self) -> None:
        self.name = "Yevheniia"
        self.second_name = "Dolhopolova"

@pytest.fixture
def user():
    yield User()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def db():
    db = Database()
    yield db