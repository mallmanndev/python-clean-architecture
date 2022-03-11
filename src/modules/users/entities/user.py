from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str
    name: str
    email: str
    birthday: datetime

    def __init__(
        self,
        id: str,
        name: str,
        email: str,
        birthday: datetime
    ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.birthday = birthday
        pass
