
class Meal :

    def __init__(self, id,  Name, Description, Price, photo_URL ):
        self.id = id
        self.Name = Name
        self.Description = Description
        self.Price = Price
        self.photo_URL = photo_URL

Meal1 = Meal(id=1, Name= 'Burgar', Description= 'With Slices Of Meat & Cheese' , Price= '15 $' ,
          photo_URL= 'https://cdn.fbsbx.com/v/t59.2708-21/60436548_291106211770888_690792738773270528_n.gif?_nc_cat=103&_nc_ht=cdn.fbsbx.com&oh=37521a63b719ffdbc46810413151298c&oe=5CF063F8' )
Meal2 = Meal(id=2, Name= 'Grilled chicken', Description= 'With Avocado & Lettuce' , Price= '30 $' ,
          photo_URL= 'https://academy-discorce-s3.s3.dualstack.us-east-2.amazonaws.com/upload/original/2X/f/f3c39987ea00d4d186f6f0d41d9aa5f274190fd9.jpeg')
Meal3 = Meal(id=3, Name= 'Steak', Description= 'With Fresh Vegetables & Juice' , Price= '35 $' ,
          photo_URL='https://academy-discorce-s3.s3.dualstack.us-east-2.amazonaws.com/upload/original/2X/3/31b44ea15e8a14895fd9383e7845fd7a1bc96838.jpeg' )
Meal4 = Meal(id=4, Name= 'Potato With Bechamel', Description= 'With Spices & Herbs' , Price= '20 $' ,
           photo_URL='https://academy-discorce-s3.s3.dualstack.us-east-2.amazonaws.com/upload/original/2X/0/04274034174fb71006e950b05292abc3934f9f1e.jpeg' )
Meals = [Meal1, Meal2,Meal3,Meal4]


class MealStore:
    def get_all(self):
        return Meals

    def add(self, Meal):

        return Meals


    def get_by_id(self, id):
        result = None
        for Meal in Meals:
            if Meal.id == id:
                result = Meal
                break
        return result

    def update(self,id,fields):
        Meal = self.get_by_id(id)
        Meal.name = fields["name"]
        Meal.Description = fields["Description"]
        Meal.photo_URL =fields["photo_URL"]
        Meal.Price =fields["Price"]
        return Meal

    def delete(self,id):
        Meal = self.get_by_id(id)
        Meals.remove(Meal)
        return Meals

store = MealStore()
store.add(Meal1)
store.add(Meal2)
store.add(Meal3)
store.add(Meal4)

print(store.get_all())
