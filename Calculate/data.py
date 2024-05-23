from Calculate import management

mana = management.management()

class data:

    def __init__(self):
        self.person_quantity = 0
        self.person_name = []
        self.bill = 0.0
        self.bride = 0.0

    def set_person_quantity(self, quantity):
        self.person_quantity = quantity

    def set_person_name(self, names):
        self.person_name = names

    def set_bill(self, bill):
        self.bill = bill

    def set_bride(self, bride):
        self.bride = bride

    def calculate_values(self):
        print("\nFactura a calcular: $%.2f" % self.bill)
        propina = mana.calculate_total(self.bill, self.bride)
        print("La propina aplicando el %d%% es $%.2f, que contabiliza un total de $%.2f" % ((self.bride * 100), propina, (self.bill + propina)))
        print("Porcentaje pagado: ")
        persons = mana.not_equitable_distribution(self.person_quantity, self.person_name)
        for person in persons.keys():
            print("%s : Porcentaje a pagar %d%% contabiliza un total de %.2f" % (person, persons.get(person), ((self.bill + propina) * (persons.get(person)/100))))

        

    