from datetime import datetime
class person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth= datetime.strptime(date_of_birth, "%Y-%m-%d").date()


        def calculate_age(self):
            today=datetime.today().date()
            age=