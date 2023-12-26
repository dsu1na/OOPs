"""
This script is for understanding class attributes.
Class attributes are different from instance attributes
In the below example TITLES is a class attribute
and all self...... are instance attributes
"""

import datetime

class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in TITLES:
            raise ValueError(f"{title} is not a valid title")

        self.title = title
        self.name = name
        self.surname = surname
    
def main():
    person = Person(
        title = 'Mr'
        name = 'Jane',
        surname = 'Doe'
    )

    print(person.name)

if __name__ == '__main__':
    main()