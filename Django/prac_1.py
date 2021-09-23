# *args: positional infinite arguments
# **kwargs : keyword infinite arguments
# method의 first argument는 method를 호출하는 instance 자신


class Car():
    def __init__(self,  **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):  # override
        return f"Car with {self.wheels} wheels"


porche = Car(color="green", price="$40")
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)
