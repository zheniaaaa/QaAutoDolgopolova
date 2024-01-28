from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Створення об'єкту сторінки для взаємодії з нею
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub 
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # перевіпяємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # закриваємо браузер
    sign_in_page.close()