class Mysql:
    def commit(self):
        print('commit---Mysql')

    def rollback(self):
        print('rollback---Mysql')

class Oracle:
    def commit(self):
        print('commit--Oracle')

    def rollback(self):
        print('rollback---Oracle')

def interface(obj):
    obj.commit()
    obj.rollback()

m=Mysql()
o=Oracle()
interface(m)
interface(o)
