import random as r

class management:

    def __init__(self):
        self.total = None
        self.distribution_person = {}

    def calculate_total(self, bill, bride):
        self.total = (bill * bride)
        return self.total
    
    def not_equitable_distribution(self, quantity, person_name):
        extremo = 100
        for i in range(quantity):
            if(i == quantity-1):
                self.distribution_person[person_name[i]] = extremo
            else:
                radon_number = r.randint(0, extremo)
                self.distribution_person[person_name[i]] = radon_number
                extremo = extremo - radon_number
        return self.distribution_person
    
    def person_pay(self):
        for person in self.distribution_person.keys():
            self.distribution_person[person] = (self.distribution_person[person] * self.total)
        return self.distribution_person
