import allure
import pytest
import requests

import steps.steps as steps
from constants import urls

from helpers.helpers import generate_random_string, return_random_book
from models.model import AddANewBookRequest, RegistrateUsers
from datetime import datetime, timedelta


@pytest.fixture(scope="function")
def AddABook():
    random_book = return_random_book()
    added_book = AddANewBookRequest(random_book[0], random_book[1])
    return requests.post(urls.LOAD_NEW_BOOK, json=added_book.to_dict())

@pytest.fixture(scope="session")
def UserId():
    password = "testtest"
    new_user = RegistrateUsers(generate_random_string(), password)
    return requests.post(urls.REGISTER_USER, json=new_user.to_dict()).json()["id"]

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты регистрации пользователя")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_sign_up1():
    code = 200
    response = steps.registgrateUser(generate_random_string(), "iloveyou")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты регистрации пользователя")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_sign_up2():
    code = 400
    response = steps.registgrateUser("", "123")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты регистрации пользователя")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_sign_up3():
    code = 400
    response = steps.registgrateUser("Katya", "")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты регистрации пользователя")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_sign_up4():
    code = 400
    response = steps.registgrateUser("Lili", "123")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты взятия книги")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_take_a_book1(AddABook, UserId):
    code = 200
    book_id = AddABook.json()["id"]
    response = steps.takeABook(book_id, UserId)
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты взятия книги")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_take_a_book2(UserId):
    code = 400
    response = steps.takeABook(7, UserId)
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты взятия книги")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_take_a_book3(UserId):
    code = 400
    response = steps.takeABook(65, UserId)
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты взятия книги")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_take_a_book4(UserId):
    code = 400
    response = steps.takeABook(65, UserId)
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты добавления книги")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_add_a_new_book():
    code = 200
    response = steps.addABook("Сергей Довлатов", "Чемодан")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка доступных книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_available_book1(AddABook):
    book_id = AddABook.json()["id"]

    books = steps.getAvailableBook()

    found = False
    for book in books:
        if book.id == book_id:
            found = True

    assert found

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка доступных книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_available_book2(AddABook, UserId):
    added_book_id = AddABook.json()["id"]

    taken_book_id = steps.takeABook(added_book_id, UserId)
    book_id = taken_book_id.json()["book"]["id"]

    books = steps.getAvailableBook()

    found = False
    for book in books:
        if book.id == book_id:
            found = True

    assert not found

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка доступных книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_available_book3(AddABook, UserId):
    added_book_id = AddABook.json()["id"]

    steps.takeABook(added_book_id, UserId)

    steps.rerurnABook(added_book_id, UserId, "2025-05-01")

    books = steps.getAvailableBook()

    found = False
    for book in books:
        if book.id == added_book_id:
            found = True

    assert found

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка статуса книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_current_status1(AddABook):
    book_id = AddABook.json()["id"]

    books = steps.currentABook()

    found = False
    for statuses in books:
        if statuses.book_id == book_id:
            found = True

    assert found

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка статуса книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_current_status2(AddABook, UserId):
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    books = steps.currentABook()
    for statuses in books:
        if statuses.book_id == book_id:
            assert statuses.renter_id == UserId

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка статуса книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_current_status3(AddABook, UserId):
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    steps.rerurnABook(book_id, UserId, "2025-04-20")

    books = steps.currentABook()
    for statuses in books:
        if statuses.book_id == book_id:
            assert statuses.renter_id is None


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты получения списка статуса книг")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_current_status4(AddABook, UserId):
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    current_data = datetime.now()
    day_plus_30_days = current_data + timedelta(days=30)
    formatted_date = day_plus_30_days.strftime("%Y-%m-%d")

    books = steps.currentABook()
    for statuses in books:
        if statuses.book_id == book_id:
            assert statuses.date_to == formatted_date

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты сдачи книги")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_return_book1(AddABook, UserId):
    code = 200
    book_id = AddABook.json()["id"]

    response = steps.takeABook(book_id, UserId)

    current_data = datetime.now()
    day_plus_30_days = current_data + timedelta(days=30)
    formatted_date = day_plus_30_days.strftime("%Y-%m-%d")
    steps.rerurnABook(AddABook.json()["id"], UserId, formatted_date)

    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты сдачи книги")
@allure.description("Тест проверяет корректность работы метода post, get и кодов ответа")
def test_return_book2(AddABook, UserId):
    code = 400
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    current_data = datetime.now()
    day_plus_30_days = current_data + timedelta(days=35)
    formatted_date = day_plus_30_days.strftime("%Y-%m-%d")
    response = steps.rerurnABook(AddABook.json()["id"], UserId, formatted_date)

    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты оплаты штрафа")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_pay_fiase1(AddABook, UserId):
    code = 200
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    current_data = datetime.now()
    day_plus_30_days = current_data + timedelta(days=33)
    formatted_date = day_plus_30_days.strftime("%Y-%m-%d")
    steps.rerurnABook(AddABook.json()["id"], UserId, formatted_date)

    paid_book = steps.payFaise(book_id, UserId, 30)

    assert paid_book.status_code == code


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты оплатф штрафа")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_pay_fiase2(AddABook, UserId):
    code = 200
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    current_data = datetime.now()
    day_plus_30_days = current_data + timedelta(days=36)
    formatted_date = day_plus_30_days.strftime("%Y-%m-%d")
    steps.rerurnABook(AddABook.json()["id"], UserId, formatted_date)

    paid_book = steps.payFaise(book_id, UserId, 100)

    assert paid_book.status_code == code


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты library")
@allure.feature("Тесты оплаты штрафа")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_pay_fiase3(AddABook, UserId):
    code = 400
    book_id = AddABook.json()["id"]

    steps.takeABook(book_id, UserId)

    current_data = datetime.now()
    day_plus_30_days = current_data + timedelta(days=36)
    formatted_date = day_plus_30_days.strftime("%Y-%m-%d")
    steps.rerurnABook(AddABook.json()["id"], UserId, formatted_date)

    paid_book = steps.payFaise(book_id, UserId, 10)

    assert paid_book.status_code == code
