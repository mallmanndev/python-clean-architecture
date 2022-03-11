from src.modules.users.entities.user import User
from src.modules.users.repositories.users_repo import UsersRepo


def print_list(list: list):
    for user in list:
        print(user.name)


def init():
    user_repo = UsersRepo()

    print("List of Users:")
    users = user_repo.list()
    print_list(users)

    print("Add in List:")
    user = user_repo.create(User(
        None,
        "Matheus Mallmann",
        "matheusvmallmann@gmail.com",
        None
    ))
    print("User id: ", user.id)

    print("List of Users:")
    users = user_repo.list()
    print_list(users)


init()
