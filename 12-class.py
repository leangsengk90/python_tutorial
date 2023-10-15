# class People():
class People:
    def __init__(self, username, password, type="user"):
        self.username = username
        self.password = password
        self.type = type

    def register(self, username, password):
        self.username = f"Mr./Mrs. {username}"
        self.password = password
        print(f"Register! {self.username} {self.password} {self.type}")
    
    def login(self):
         print(f"Login! {self.username} {self.password} {self.type}")
    
    def add_to_chart(self, username):
        self.username = username
        print("Add to Chart", self.username)

class Customer(People):
    pass # Empty class is not lonely, just added "pass"

class Staff(People):
    def __init__(self, username, password, type="user"):
        super().__init__(username, password, type)

    def generateReport(self):
        print("I can generate report!")

staff1 = Staff()
staff1.generateReport()

customer1 = People("Dara", "123")
customer1.login()
customer1.register("Nita", "123")
customer1.login()
customer1.add_to_chart("Bora")
customer1.login()
customer1 = People(password="123", username="Dara2", type="Admin")
customer1.login()