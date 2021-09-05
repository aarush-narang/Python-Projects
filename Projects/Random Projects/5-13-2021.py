import random


def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False


def missingitemfinder(items):
    for i in range(len(items)):
        if search(fruits, items[i])


print("Please enter four names: ")

fruits = ["apple", "orange", "banana", "kiwi"]
vegetables = ["carrot", "kale", "celery", "broccoli"]
basket = ["apple", "orange", "banana", "kiwi", "carrot", "kale", "celery", "broccoli", "milk"]


for i in range(1, 5):
    personName = input(f"Person {i}: ")
    personItems = [basket[random.randrange(0, len(basket) - 1)], basket[random.randrange(0, len(basket) - 1)]]
    missingItems = missingitemfinder(personItems)
    print(personName, personItems, missingItems)
