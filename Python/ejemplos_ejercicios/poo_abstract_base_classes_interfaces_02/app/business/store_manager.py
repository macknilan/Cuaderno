
from app.models.user import User
from app.repository.user_repository import UserRepository


class StoreManager:

    @staticmethod
    def storeUser(user: User, userRepository: UserRepository) -> None:
        print("--->Storing user...\n")
        userRepository.open()
        userRepository.store(user)
        userRepository.close()
