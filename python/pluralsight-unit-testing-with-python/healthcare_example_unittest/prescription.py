from datetime import date, timedelta

class Prescription:
    
    def __init__(self, name, dispense_date, days_supply):
        self.name = name
        self.dispense_date = dispense_date
        self.days_supply = days_supply
        
    def days_taken(self):
        all_days = [self.dispense_date + timedelta(days=i) for i in range(self.days_supply)]
        # BUGBUG: The following change will cause a regression.
        return all_days #[day for day in all_days if day < date.today()]
