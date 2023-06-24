from src.modules.store import Store
from src.modules.user import User

class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name != None and job != None:
            if type(name) == str and type(job) == str:
                    user_bd = self.check_user(name)
                    if user_bd == None:
                        user = User(name=name, job=job)
                        self.store.bd.append(user)
                        return "Usuario adicionado"
                    else:
                        return "Usuario ja existe"
            else:
                return "Usuario invalido"
        else:
            return "Usuario invalido"

    def check_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def check_user_job(self, job):
        for user in self.store.bd:
            if user.job == job:
                return user
        return None
    def remove_user(self, name):
        user_bd = self.check_user(name)
        if user_bd != None:
            self.store.bd.remove(user_bd)
            return "Usuario removido com sucesso"
        else:
            return "Usuario nao encontrado"

    def update_user(self, name, new_job):
        user_bd = self.check_user(name)
        if user_bd != None:
            index = self.store.bd.index(user_bd)
            self.store.bd[index].job = new_job
            return "Job do usuario atualizado com sucesso"
        else:
            return "Usuario nao encontrado"

    def list_user(self, job):
        user_info = []
        for i, user in enumerate(self.store.bd):
            if user.job == job:
                user_info.append((user.name, user.job))
        if len(user_info) > 0:
            return user_info
        else:
            return "Nenhum usuário encontrado com o job informado"

