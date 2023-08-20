##############  Instance Method  ##############
# 1- is a method that is bound to the instance of the class.
# 2- This method can access or modify the state of the class and instance.
# 3- takes self as the first parameter
# 4- mostly used to access or change the attributes of the object on which they are called.
# 5- can be called only by the objects of the class


##############  Class Method  ##############
# 1- is a method that is bound to the class.
# 2- This method can access or modify the state of the class as it takes a class parameter that points to the class.
# 3- takes cls as the first parameter
# 4- We use @classmethod decorator To define a class method
# 5- We use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
# 6- can be called by the objects of the class as well as by the class itself


##############  Static Method  ##############
# 1- is a method that is bound to the class.
# 2- This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.
# 3- needs no specific parameters.
# 4- we use @staticmethod decorator to define a static method .
# 5- We use static methods to create utility functions.
# 6- can be called by the objects of the class as well as by the class itself


class Person():
    def __init__(self, name, age, can_vote):
        self.name = name
        self.age = age
        self.can_vote = can_vote
	
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False
		
    @classmethod	
    def create(cls, name, age):
        if cls.is_adult(age) == True:
            return cls(name, age, "Yes")
        else:
            return cls(name, age, "No")

person1 = Person.create("A", 15)
person2 = Person.create("B", 20)

print("Can", person1.name, "vote?", person1.can_vote)
print("Can", person2.name, "vote?", person2.can_vote)

