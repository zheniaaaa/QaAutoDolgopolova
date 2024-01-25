import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(db):
    db.test_connection()


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(db):
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update(db):
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(db):
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(db):
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_ordersdb(db):
    orders = db.get_detailed_orders()
    print ("Замовлення", orders) # Not necessary 
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

# My individual part starts here. I also made a fixture db, check it out :)

@pytest.mark.database
def test_valid_data_types(db):
    db.add_valid_data(3, "Yevheniia", "Litakova", "Odesa", "65085", "Ukraine")
    get_customer = db.select_customer_by_id(3)
    print(get_customer) # Just for checking

    assert len(get_customer) == 1


@pytest.mark.database
def test_adding_invalid_types_of_data(db):
    
    # Trying to use try-except construction

    try:
        db.insert_product(6, 12, "with lime flavour", 10)

    except TypeError as e:
        assert str(e) == "Invalid data type for name: expected str, got int"


@pytest.mark.database
def test_get_data_with_non_existent_id(db):
    r = db.get_data_by_non_existent_id(44)

    assert len(r) == 0


@pytest.mark.database
def test_add_unsupported_data_type(db):
    with pytest.raises(TypeError):
        db.insert_product_for_adding_unsupported_types_of_data("сім", 12, ["with lime flavour"], "10")

# And I'll finish with an easy test, those above it were a little more difficult :) 

@pytest.mark.database
def test_right_quantity_of_product(db):
    qnt = db.select_product_qnt_by_id(2)

    assert qnt[0][0] == 10

