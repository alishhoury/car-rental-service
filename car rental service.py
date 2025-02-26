class vehicle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental = rental_price_per_day
        
    def dispaly_info(self):
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
        print(f"Rental price per day:{self.rental}")
    

