class User:
    def __init__(self, id: int, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self):
        return f"User(name={self.name}, id={self.id}, status={self.status})"

class PetStoreResponse:
    def __init__(self, id: int, name: str, status: str, category: str, photoUrls: str, tags: str):
        self.id = id
        self.name = name
        self.status = status
        self.category = category
        self.photoUrls = photoUrls
        self.tags = tags

    def __repr__(self):
        return f"PetStoreResponse(name={self.name}, id={self.id}, status={self.status})"

class PetStoreRequest:
    def __init__(self, id: int, name: str, status: str, category: str, photoUrls: str, tags: str):
        self.id = id
        self.name = name
        self.status = status
        self.category = category
        self.photoUrls = photoUrls
        self.tags = tags

class CreateUserRequest:
    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str, phone: int, userStatus: int ):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userstatus = userStatus

    def to_dict(self):
        return {
            "name": self.id,
            "age": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userstatus
        }

class RegistrateUsers:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def to_dict(self):
        return {
            "login": self.login,
            "password": self.password,
        }

    #def __repr__(self):
        #return "{" + f"\"login\":\"{self.login}\", \"password\":\"{self.password}\"" + "}"

class TakeABookRequest:
    def __init__(self, book_id: int, user_id: int):
        self.book_id = book_id
        self.user_id = user_id

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "user_id": self.user_id,
        }

class AddANewBookRequest:
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
        }

class Book():
    def __init__(self, id: str, author: str, title: str):
        self.id = id
        self.author = author
        self.title = title

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "id": self.id
        }

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"

class ReturnABook():
    def __init__(self, book_id: str, user_id: int, date_to_return:str):
        self.book_id = book_id
        self.user_id = user_id
        self.date_to_return = date_to_return

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "user_id": self.user_id,
            "date_to_return": self.date_to_return,
        }

class CurrentStatusBook():
    def __init__(self, book_id: str, renter_id: str, date_to: str):
        self.book_id = book_id
        self.renter_id = renter_id
        self.date_to = date_to

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "renter_id": self.renter_id,
            "date_to": self.date_to,
        }

class PayRaise():
    def __init__(self, book_id: str, user_id: str, amount: float):
        self.book_id = book_id
        self.user_id = user_id
        self.amount = amount

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "user_id": self.user_id,
            "amount": self.amount,
        }