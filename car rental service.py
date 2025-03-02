class vehicle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental = rental_price_per_day

    def dispaly_info(self):
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
        print(f"Rental price per day:{self.rental}")
    
    def calculate_rental_cost(self,days):
        return self.rental*days

    def get_rental_price(self):
       return self.__rental
    
    def set_rental_price(self,new_price):
         self.__rental = new_price

class car(vehicle):
    def __init__(self, brand, model, year, rental_price_per_day,seats):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seats

    def dispaly_info(self):
        super().dispaly_info()
        print(f"seats:{self.seats}")
    
class Bike(vehicle):
    def __init__(self, brand, model, year, rental_price_per_day,engine):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine
    def dispaly_info(self):
        super().dispaly_info()
        print(f"Engine:{self.engine_capacity}cc")
     