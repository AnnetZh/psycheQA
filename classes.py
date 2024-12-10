class Cars:
  def __init__(self, model,year,size,price,milage,wheels=4):
      self.model=model
      self.year=year
      self.size=size
      self.price=price
      self.milage=milage
      self.wheels=wheels

  def description(self):
      description = (
          f"Название автомобиля {self.model}, год выпуска {self.year}, размер {self.size}, цена {self.price}, пробег {self.milage}, количество колес {self.wheels}")
      return description
suv=Cars("внедорожник",2009, "small", 50700,253000,4)

class Truck(Cars):
    def __init__(self,model,year,size,price,milage,wheels=8):
        super().__init__(model,year,size,price,milage,wheels)
        self.wheels_truck=8
container_carrier=Truck("Контейнеровоз", 2013, "big",160800,364000,8)


print(suv.description())
print(container_carrier.description())