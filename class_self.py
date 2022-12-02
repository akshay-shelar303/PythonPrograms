class Student:
    def display(self):
        print(self.rollno)
        print(self.name)

akshay=Student()
akshay.rollno=1
akshay.name="Akshay Shelar"
print(akshay.rollno)
print(akshay.name)

shelar=Student()
shelar.rollno=2
shelar.name="Shelar Akshay"
print(shelar.rollno)
print(shelar.name)

akshay.display()
shelar.display()
