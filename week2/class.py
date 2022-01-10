# name = input ("Enter your name: ")
# birthPlace = input("Enter you Place of BirthPlace: ")
# print (name.upper())
# print (birthPlace.upper())


class myClass:
    def __init__(self, first_name, last_name, place_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.place_of_birth = place_of_birth

    def _str_(self):
        s = f"First Name : {self.first_name.upper()}, Last_name : {self.last_name.upper()}, Place of Birth : {self.place_of_birth.upper()}"
        return (s)

person = myClass(input ("Enter your First Name: "), input ("Enter your Last Name: "),  input("Enter you Place of BirthPlace: "))
print(person._str_())

    # print ("name.upper()")
    # def method2(BirthPlace = input ("Enter your BirthPlace"))
    # print ("BirthPlace".upper())

    # def main()