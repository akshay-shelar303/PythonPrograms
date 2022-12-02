class Customer:
    def setFirstname(self,firstname):
        self.firstname=firstname
    def getFirstname(self):
        return self.firstname

    def setMiddlename(self,middlename):
        self.middlename=middlename
    def getMiddlename(self):
        return self.middlename

    def setLastname(self,lastname):
        self.lastname=lastname
    def getLastname(self):
        return self.lastname
    
    def setEmail(self,email):
        self.email=email
    def getEmail(self):
        return self.email

    def setGender(self,gender):
        self.gender=gender
    def getGender(self):
        return self.gender

    def setCity(self,city):
        self.city=city
    def getCity(self):
        return self.city


c=Customer()
c.setFirstname('Akshay')
c.setMiddlename('Bhanudas')
c.setLastname('Shelar')
c.setEmail('xyz@gmail.com')
c.setGender('Male')
c.setCity('Pune')

print(c.getFirstname())
print(c.getMiddlename())
print(c.getLastname())
print(c.getEmail())
print(c.getGender())
print(c.getCity())
