from __future__ import annotations

class Category:
    def __init__(self, category: str):
        self.category = category
        self.ledger: list[dict] = []

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        total = 0.00
        for transaction in self.ledger:
            total += transaction["amount"]
        return total

    def transfer(self, amount: float, payee: Category) -> bool:
        if self.withdraw(amount, f"Transfer to {payee.category}"):
            payee.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        return self.get_balance() >= amount

    def __str__(self) -> str:
        message: list[str] = []
        total: float = 0.00
        message.append(self.category.center(30, "*"))
        for value in self.ledger:
            total += value["amount"]
            description = value["description"][:23].ljust(23)
            amount = f"{value["amount"]:>7.2f}"
            entry = f'{description}{amount}'
            message.append(entry)
        message.append(f"Total: {total:.2f}")
        return "\n".join(message)

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category("Clothing")
food.transfer(50, clothing)

category: list[Category] = [food, clothing]

# Incremental string concatenation is an expensive operation O(n²), yet I have no choice but to use it for this absurd bar chart requirement
def create_spend_chart(categories: list[Category]):
    message: list = ["Percentage spent by category"]
    total_spend = 0
    category_spend: dict = {}

    # Calculating percentage for each spend
    for category in categories:
        current_category = category.category
        category_spend[current_category] = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                category_spend[current_category] += abs(entry["amount"])
        total_spend += category_spend[current_category]
    for entry in category_spend:
        category_spend[entry] = round((category_spend[entry] / total_spend) * 100)

    # printing the contents of the bar chart
    for number in range(10, -1, -1):
        new_line: list = [f"{str(number * 10).rjust(3)}| "]
        for entry in category_spend:
            if category_spend[entry] >= number * 10:
                new_line.append("o".ljust(3))
            else:
                new_line.append("   ")
        message.append("".join(new_line))

    # printing end of bar chart horizontal line
    message.append(f"    {'-' * (3 * len(category_spend))}-")

    # print names of category in horizontal
    longest_category = 0
    for value in category_spend.keys():
        longest_category = len(value) if len(value) > longest_category else longest_category
    for i in range(longest_category):
        new_line: list = [" ", " ", " ", " ", " "]
        for value in category_spend.keys():
            try:
                new_line.append(value[i])
            except IndexError:
                new_line.append(" ")
            finally:
                new_line.append("  ")
        message.append("".join(new_line))
    return "\n".join(message)





print(create_spend_chart(category))
