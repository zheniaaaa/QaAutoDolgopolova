import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""


@pytest.mark.change
def test_name(user):
    assert user.name == 'Yevheniia'


@pytest.mark.change
def test_second_name(user):
    assert user.second_name == "Dolhopolova"