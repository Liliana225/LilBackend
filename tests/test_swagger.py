import json
import time
import requests
import allure

from models.model import PetStoreResponse, CreateUserRequest, PetStoreRequest


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты pets")
@allure.feature("Тесты получения питомца по id")
@allure.description("Тест проверяет корректность работы метода get и кодов ответа")
def test_get_id():
    code = 200
    with allure.step("Получить питомца по id"):
        response = requests.get("https://petstore.swagger.io/v2/pet/1")
    print(response.text)
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты pets")
@allure.feature("Тесты создания питомца по id")
@allure.description("Тест проверяет корректность работы метода post и кодов ответа")
def test_post_id():
    url = 'https://petstore.swagger.io/v2/pet'
    code = 200
    with allure.step("Создать питомца"):
        new_pet = PetStoreResponse(26789, "Lilcat","available", " "," ", " " )
        response = requests.post(url, new_pet)
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты pets")
@allure.feature("Тесты замены одного питомца на другого")
@allure.description("Тест проверяет корректность работы методов post, put, get")
def test_update_id():
    url = 'https://petstore.swagger.io/v2/pet'
    name = "Lildog"
    with allure.step("Создать питомца"):
        new_pet = PetStoreRequest(26791, "Lilcat","available", " "," ", " " )
        requests.post(url, new_pet)
        time.sleep(1)
    with allure.step("Изменить id питомца"):
        update_pet = PetStoreRequest(26791, "Lildog","available", " "," ", " " )
        requests.put(url, update_pet)
        time.sleep(2)
    with allure.step("Получить питомца по id"):
        response = requests.get("https://petstore.swagger.io/v2/pet/26791")
    pet_store_response = PetStoreResponse(**json.loads(response.text))
    assert pet_store_response.name == name

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты users")
@allure.feature("Тесты создания нового пользователя")
@allure.description("Тест проверяет корректность работы методов post, get")
def test_create_user():
    url = 'https://petstore.swagger.io/v2/user'
    id = 1897
    login = "Lil"
    firstName = "Liliana"
    lastName = "Akhatova"
    email = "lil@mail.ru"
    password = "lilo22"
    phone = 89966059445
    userStatus = 1
    create_user_request = CreateUserRequest(id, login, firstName, lastName,
                                            email, password, phone, userStatus)
    with allure.step("Создать пользователя"):
        requests.post(url, json=json.dumps(create_user_request.to_dict(), indent=4))
    with allure.step("Получить пользователя"):
        requests.get("https://petstore.swagger.io/v2/user/Lil")
    assert create_user_request.id == 1897
    assert create_user_request.username == "Lil"
    assert create_user_request.firstName == "Liliana"
    assert create_user_request.lastName == "Akhatova"
    assert create_user_request.email == "lil@mail.ru"
    assert create_user_request.password == "lilo22"
    assert create_user_request.phone == 89966059445
    assert create_user_request.userstatus == 1

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты users")
@allure.feature("Тесты регистрации и создания нового пользователя")
@allure.description("Тест проверяет корректность работы метода get, post и кодов ответа")
def test_user_login_and_create():
    url = 'https://petstore.swagger.io/v2/user'
    id = 1897
    login = "Lil"
    firstName = "Liliana"
    lastName = "Akhatova"
    email = "lil@mail.ru"
    password = "lilo22"
    phone = 89966059445
    userStatus = 1
    code = 200
    create_user_request = CreateUserRequest(id, login, firstName, lastName,
                                            email, password, phone, userStatus)
    requests.post(url, json=json.dumps(create_user_request.to_dict(), indent=4))
    with allure.step("Зарегистировать пользователя"):
        response = requests.get(f"https://petstore.swagger.io/v2/user/login?username={login}&password={password}")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты pets")
@allure.feature("Тесты сосздания питомца и его удаления")
@allure.description("Тест проверяет корректность работы метода get, post, delete и кодов ответа")
def test_create_and_delete_pet():
    url = 'https://petstore.swagger.io/v2/pet'
    code = 404
    with allure.step("Создать пользователя"):
        new_pet = PetStoreRequest(26792, "Lilcat","available", " "," ", " " )
        requests.post(url, new_pet)
    with allure.step("Удалить пользователя"):
        requests.delete("https://petstore.swagger.io/v2/pet/26792")
    time.sleep(4)
    with allure.step("Получить пользователя"):
        response = requests.get("https://petstore.swagger.io/v2/pet/26792")
    assert response.status_code == code

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты swagger ui")
@allure.story("Тесты pets")
@allure.feature("Тесты изменения статуса животного")
@allure.description("Тест проверяет корректность работы метода get, post, put")
def test_change_status_pet():
    url = 'https://petstore.swagger.io/v2/pet'
    id = 26793
    with allure.step("Создать питомца"):
        new_pet = PetStoreRequest(26793, "Lilcat","available", " "," ", " " )
        requests.post(url, new_pet)
    with allure.step("Поменять питомца"):
        update_pet = PetStoreRequest(26793, "Lilcat","sold", " "," ", " ")
        requests.put(url, update_pet)
        time.sleep(2)
    with allure.step("Изменить питомца"):
        response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")
        data = json.loads(response.text)
        pets = [PetStoreResponse(**item) for item in data]

        found = False
        for pet in pets:
            if pet.id == id:
                found = True

    assert found == True








