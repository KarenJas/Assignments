'''2. The Recipe Ratio Adjuster'''

#Task 1: Start
try:
    original_servings= float(input("Number of servings in original recipe: "))
    desired_servings = float(input("How many servings do you wish to make: "))
except ValueError:
    print("Please input a proper value")

#Task 2: Quantity Calculation
try:
    adjustment_factor = desired_servings / original_servings
    print(f"Adjusted recipe quantities: {adjustment_factor}")
except ZeroDivisionError:
    print("Cant devide by zero. Please input a proper value")
finally:
    print("Enjoy Your Cooking! :)")




'''class unit_converter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    
    def tablespoon_to_teacpoons(self, target_unit):
        conversion_factors = {'tablespoon': 1, 'teaspoon': 3} 
        return self.value * conversion_factors[self.unit] / conversion_factors[target_unit]

'''



