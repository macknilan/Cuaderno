from app.models.user import User

class UserRepository:
    def open(self,)->None:
        pass
    def store(self,user:User)->None:
        pass
    def close(self)->None:
        pass
