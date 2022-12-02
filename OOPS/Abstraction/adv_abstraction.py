from abc import ABC,abstractmethod

class Db(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

class Oracle(Db):
    def commit(self):
        print("commit----Oracle")

    def rollback(self):
        print("rollback----Oracle")

class Mysql(Db):
    def commit(self):
        print("commit----Mysql")

    def rollback(self):
        print("rollback----Mysql")
    


o=Oracle()
o.commit()
o.rollback()

m=Mysql()
m.commit()
m.rollback()

