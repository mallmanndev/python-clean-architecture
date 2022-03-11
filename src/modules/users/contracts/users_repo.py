from abc import ABCMeta, abstractmethod

from src.modules.users.entities.user import User


class UsersRepoContract(metaclass=ABCMeta):

    @abstractmethod
    def create(self, data: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def list(self) -> list[User]:
        pass
