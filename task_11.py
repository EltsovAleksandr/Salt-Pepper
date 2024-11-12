class Dessert:

    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if self.calories == None:
            return None
        try:
            isinstance(self.calories, (int, float)) or isinstance(
                int(self.calories), (int, float)
            )
        except ValueError:
            return "Ошибка ввода калорий"
        else:
            if int(self.calories) < 200:
                return True
            else:
                return False

    def is_delicious(self):
        return True


