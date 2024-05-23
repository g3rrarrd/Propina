from Calculate import data

class main:

    def __init__(self):
        self.data = data.data()
        self.bride = {1: 0.18, 2: 0.20, 3: 0.25}

    def set_bill(self):
        while True:
            try:
                print("\nCual es la factura total de hoy?")
                bill = float(input("$"))
                self.data.set_bill(bill)
                return
            except ValueError:
                print("Valor no numerico ingresado")

    def set_bride(self):
        while True:
            try:
                print("\nIngrese la cantidad de propina que desea dar: \n1. 18% \n2. 20% \n3. 25%")
                total = int(input())
                self.data.set_bride(self.bride.get(total))
                return
            except ValueError:
                print("Valor no numerico ingresado")
            except KeyError:
                print("Fuera del rango") 

    def set_names(self, quantity):
        person_name = []       
        print("\ningrese su/sus nombres")
                
        for i in range(quantity):
            person_name.append(input("Nombre: "))

        self.data.set_person_name(person_name)

    def run(self):
        try:
            print("Cantidad de personas a facturar")
            person_quantity = int(input())
            self.data.set_person_quantity(person_quantity)

            self.set_names(person_quantity)
                        
            self.set_bride()
            self.set_bill()
            self.data.calculate_values()
        except ValueError:
            print("Valor numerico no ingresado")
            