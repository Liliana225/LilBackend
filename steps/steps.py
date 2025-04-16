import allure
import requests
from requests import Response

from constants import urls
from models.model import RegistrateUsers, TakeABookRequest, AddANewBookRequest, Book, ReturnABook, CurrentStatusBook, \
    PayRaise


def registgrateUser(login: str, password: str) -> Response:
    with allure.step("Зарегистрировать пользователя"):
        new_user = RegistrateUsers(login, password)
        return requests.post(urls.REGISTER_USER, json=new_user.to_dict())

def takeABook(book_id: int, user_id: int):
    with allure.step("Взять книгу"):
        taken_book = TakeABookRequest(book_id, user_id)
        response = requests.post(urls.TAKE_A_BOOK, json=taken_book.to_dict())
        print(response)
        return response

def addABook(author: str, title: str):
    with allure.step("Добавить книгу"):
        added_book = AddANewBookRequest(author, title)
        return requests.post(urls.LOAD_NEW_BOOK, json=added_book.to_dict())

def getAvailableBook():
    with allure.step("Получение списка доступных книг"):
        data = requests.get(urls.GET_AVAILABLE_BOOKS).json()
        return [Book(book["id"], book["author"], book["title"]) for book in data["books"]]

def rerurnABook(book_id: str, user_id:int, date_to_return:str):
    with allure.step("Вернуть книгу"):
        returned_book = ReturnABook(book_id, user_id, date_to_return)
        return requests.post(urls.RETURN_BOOK, json=returned_book.to_dict())

def currentABook():
    with allure.step("Получение статуса книг"):
        data = requests.get(urls.GET_CURRENT_STATUSES).json()
        return [CurrentStatusBook(statuses["book_id"], statuses.get("renter_id"), statuses.get("date_to")) for statuses in data["statuses"]]

def payFaise(book_id: str, user_id: str, amount: float):
    paid_book = PayRaise(book_id, user_id, amount)
    return requests.post(urls.PAY_FIASE, json=paid_book.to_dict())

