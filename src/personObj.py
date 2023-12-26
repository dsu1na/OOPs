import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, today.month, self.birthdate.day):
            age -= 1
        
        return age
    
def main():
    person = Person(
        name = 'Jane',
        surname = 'Doe',
        birthdate= datetime.date(1992, 3, 12),
        address= "No 12 Short street",
        telephone= '222 555',
        email= 'xyz@gmail.com'
    )

    print(person.name)
    print(person.email)
    print(person.age())

if __name__ == '__main__':
    main()