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

