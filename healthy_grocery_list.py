class HealthyGroceryList:
    def __init__(self):
        self.protein_sources = []
        self.vegetables = []
        self.fruits = []
        self.healthy_fats = []
        self.legumes = []
        self.carbohydrates = []
        self.drinks = []

    def check_healthiness(self):
        protein_condition = len(self.protein_sources) >= 4 and len(
            [source for source in self.protein_sources if "plant" in source.lower()]) >= 2
        vegetable_condition = len(self.vegetables) >= 7
        fruit_condition = len(self.fruits) >= 4
        healthy_fats_condition = len(self.healthy_fats) >= 3
        legumes_condition = len(self.legumes) >= 2
        carbohydrates_condition = all("sugar" not in carb.lower() for carb in self.carbohydrates) and len(
            self.carbohydrates) >= 3
        drinks_condition = all("sugar" not in drink.lower() for drink in self.drinks) and len(self.drinks) <= 2

        conditions_met = (
                protein_condition
                and vegetable_condition
                and fruit_condition
                and healthy_fats_condition
                and legumes_condition
                and carbohydrates_condition
                and drinks_condition
        )
        return conditions_met

    def add_to_list(self, category, item):
        if category.lower() == "protein":
            self.protein_sources.append(item)
        elif category.lower() == "vegetable":
            self.vegetables.append(item)
        elif category.lower() == "fruit":
            self.fruits.append(item)
        elif category.lower() == "healthy fat":
            self.healthy_fats.append(item)
        elif category.lower() == "legume":
            self.legumes.append(item)
        elif category.lower() == "carbohydrate":
            self.carbohydrates.append(item)
        elif category.lower() == "drink":
            self.drinks.append(item)
        else:
            print(f"Unknown category: {category}. Item '{item}' not added.")
