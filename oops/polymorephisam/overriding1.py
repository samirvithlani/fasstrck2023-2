#parent class function create in child class called overriding

class Parent:
    
    def phone(self):
        print("have nokia 5310")

class Child(Parent):
    
    def phone(self):
        super().phone()
        print("have iphone 12 pro max")



c = Child()
c.phone()                