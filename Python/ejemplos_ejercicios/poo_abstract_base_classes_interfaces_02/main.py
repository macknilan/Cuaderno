# https://www.youtube.com/watch?v=68te_vD2Fe8

from app.repository.user_repository import UserRepository
from app.business.store_manager import StoreManager
from app.repository.database import Database
from app.repository.s3 import S3
from app.repository.file_system import FileSystem
from app.models.user import User


user = User("Roberto", "Jimenez", 18)

s3Repository = S3("321312321", "sdf32423", "MyBucket")
StoreManager.storeUser(user, s3Repository)

print("\n")

fileSystemRepository = FileSystem("/home/users")
StoreManager.storeUser(user, fileSystemRepository)

print("\n\n")

databaseRepository = Database("localhost", "admin", "admin123")
StoreManager.storeUser(user, databaseRepository)
