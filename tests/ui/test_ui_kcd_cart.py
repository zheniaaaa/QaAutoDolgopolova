from modules.ui.page_objects.work_with_kcd_cart import KcdCart
import pytest

@pytest.mark.my_ui
def test_correct_work_with_kcd_cart():
    work_with_kcd_cart = KcdCart()
    work_with_kcd_cart.go_to()
    work_with_kcd_cart.look_for_ineresting_section()
    work_with_kcd_cart.add_ineresting_book_to_cart()
    work_with_kcd_cart.try_to_open_cart()
    work_with_kcd_cart.delete_book_from_cart()
    work_with_kcd_cart.go_to_another_section()
    work_with_kcd_cart.add_another_book_to_cart()
    work_with_kcd_cart.add_one_more_book_to_cart()
    work_with_kcd_cart.try_to_open_cart()
    work_with_kcd_cart.try_to_increase_qnt_of_books_to_10("0")
    work_with_kcd_cart.click_to_save_changes()
    work_with_kcd_cart.enter_wrong_promocod("1234")
    work_with_kcd_cart.close()