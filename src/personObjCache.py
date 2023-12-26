import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

        self._age = None
        self._age_last_calculated = None

        self._calculate_age()

    def _calculate_age(self):

        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, today.month, self.birthdate.day):
            age -= 1
        
        self._age = age
        self._age_last_calculated = today

        return age
    
    def age(self):

        today = datetime.date.today()

        if (today > self._age_last_calculated):
            self._calculate_age()
        
        return self._age
    
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