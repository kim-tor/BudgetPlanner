class ExpenseCategoryNode:
    def __init__(self, name):
        self.name = name #category's name
        self.children = [] #empty list to hold subcategories

    def add_child(self, child):
        self.children.append(child) #adds the node to the current category's children list

    def find_category(self, name):
        if self.name == name:
            return self
        for child in self.children:
            result = child.find_category(name) #recursively searches the child's Tree

            if result:
                return result
        return None
#create the root category
expenses = ExpenseCategoryNode('Expenses')

#create the first level categories
housing = ExpenseCategoryNode('Housing')

#create the second level categories
rent = ExpenseCategoryNode('Rent')
utilities = ExpenseCategoryNode('Utilities')

#connect the nodes
expenses.add_child(housing)

housing.add_child(rent)
housing.add_child(utilities)

print(expenses.name)

for category in expenses.children:
    print(category.name)

    for subcategory in category.children:
        print("  ", subcategory.name)

result = expenses.find_category("Rent")
if result:
    print("Category found:", result.name)
else:
    print("Category not found")

result = expenses.find_category("Groceries")
print(result)