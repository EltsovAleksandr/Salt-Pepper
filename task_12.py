class Dessert:

    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if not self.calories:
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
        if hasattr(self, "flavor"):
            if self.flavor == "black licorice":
                return False
        return True


class JellyBean(Dessert):

    def __init__(self, flavor=None, name=None, calories=None):
        super().__init__(name, calories)
        self.flavor = flavor

