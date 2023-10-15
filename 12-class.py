class Customer:
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


customer1 = Customer("Dara", "123")
customer1.login()
customer1.register("Nita", "123")
customer1.login()
customer1.add_to_chart("Bora")
customer1.login()
customer1 = Customer(password="123", username="Dara2", type="Admin")
customer1.login()