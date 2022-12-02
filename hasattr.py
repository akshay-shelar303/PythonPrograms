class Oracle:
    def commit(self):
        print("commit---Oraclr")
        
    def rollback(self):
        print("rollback---Oraclr")

class Mysql:
    def commit(self):
        print("commit---Mysql")

    def rollback(self):
        print("rollback---Mysql")

    def rollbackMysql(self):
        print("rollbackMysql----Mysql")

def connect(obj):
    obj.commit()
    if hasattr(obj,'rollback'):
        obj.rollback()

    if hasattr(obj,'rollbackMysql'):
        obj.rollbackMysql()

connect(Oracle())
connect(Mysql())
