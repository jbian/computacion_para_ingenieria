
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 08:37:11 2022

@author: portaticomps
"""
class Address:
    def __init__(self, Street, City, State, PostalCode, Country):
        self.Street=Street
        self.City=City
        self.PostalCode=PostalCode
        self.Country=Country
    def Validate():
        print("Validate")
    def OutputAsLabel(self):
        print(f"the address is {self.Street}")

class Person:
    def __init__(self, Name, PhoneNumber, EmailAddress, Address):
        self.Name=Name
        self.PhoneNumber=PhoneNumber
        self.EmailAddress=EmailAddress
        self.Address=Address
    def PurchasePakingPass():
        print("purchase!!!")
        

class Student(Person):
    def __init__(self, Name, PhoneNumber, EmailAddress, Adress, studentNumber, AvgMark):
        # llama al metodo constructor de la clase padre
        super().__init__(Name, PhoneNumber, EmailAddress, Address)
        self.studentNumber=studentNumber
        self.AvgMark=AvgMark
    def isEligibleToEnroll():
        print("is Ilegible to enroll")
    def getSeminarsTOken():
        print("token")
        
class Profesor(Person):
    def __init__(self,Name, PhoneNumber, EmailAddress, Salary):
        super().__init__(Name, PhoneNumber, EmailAddress)
        self.Salary=Salary
# usar las clases
adress_heroinas = Address("calle 10 de junio", "Cochabamba", "Texas", 0000, "Bolivia")

estudiante_jhonny = Student("jhonn", 7777, "jvm.corp@gmmgm.com", adress_heroinas, 1232, 50)

estudiante_jose = Student("Jose", 7777, "jvm.corp@gmmgm.com", adress_heroinas, 1232, 50)


        