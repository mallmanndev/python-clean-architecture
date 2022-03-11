from uuid import uuid4
from src.modules.users.contracts.users_repo import UsersRepoContract
from src.modules.users.entities.user import User


class UsersRepo(UsersRepoContract):
    users: list[User] = [
        User(uuid4(), 'Fulano De Tal', 'fulano@email.com', None),
        User(uuid4(), 'Ciclano De Tal', 'ciclano@email.com', None),
        User(uuid4(), 'Beltrano De Tal', 'beltrano@email.com', None)
    ]

    def create(self, data: User) -> User:
        user_to_add = User(uuid4(), data.name, data.email, data.birthday)
        self.users.append(user_to_add)
        return user_to_add

    def find_by_id(self, id: str) -> User:
        print(id)

    def find_by_email(self, email: str) -> User:
        print(email)

    def list(self) -> list[User]:
        return self.users
