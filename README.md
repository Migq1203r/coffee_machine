# Coffee Machine Program

This is a Python-based Coffee Machine program that simulates a coffee shop experience. Users can interact with the machine to order various types of coffee, view ingredients, check available resources, and more.

## Features

- **Espresso**, **Latte**, and **Cappuccino** are available in the menu.
- Users can input coins (quarters, dimes, nickels, pennies) to pay for coffee.
- The program checks if there are enough resources (water, milk, coffee) to prepare the selected coffee.
- Users can view available resources and check how much money the machine has earned.
- Ingredients for each coffee are listed for reference.

## Coffee Menu

### 1. Espresso
- **Ingredients:**
  - Water: 50 ml
  - Coffee: 18 g
- **Cost:** $1.50

### 2. Latte
- **Ingredients:**
  - Water: 200 ml
  - Milk: 150 ml
  - Coffee: 24 g
- **Cost:** $2.50

### 3. Cappuccino
- **Ingredients:**
  - Water: 250 ml
  - Milk: 100 ml
  - Coffee: 24 g
- **Cost:** $3.00

## Functionality

### `make_coffee(type_coffee)`
This function checks whether there are enough resources to make the requested coffee. If sufficient resources and funds are available, it prepares the coffee and deducts the resources. The user receives any remaining change.

### `change_account(type_coffee)`
This function is responsible for handling the user's payment. It prompts the user to insert coins if they haven't inserted enough money. After payment is received, the `make_coffee()` function is called to prepare the coffee.

### `home()`
The main menu of the coffee machine. Users can choose from the following options:
- **Order a coffee**: Choose from Espresso, Latte, or Cappuccino.
- **Check report**: View the current resource status and total profit.
- **View ingredients**: Get a list of ingredients for a specific coffee type.
- **Turn off the machine**: Exit the program.

### `resources`
The available resources are stored in a dictionary:
- **Water**: 300 ml
- **Milk**: 200 ml
- **Coffee**: 100 g

### `account` and `profit`
- **Account** tracks the amount of money the user inserts.
- **Profit** tracks the total money earned by the machine.

## How to Use

1. Run the script.
2. Select a coffee (espresso, latte, or cappuccino).
3. Insert coins when prompted.
4. The machine will either serve your coffee or ask you to insert more coins if there isn't enough money.
5. You can also check the available resources and total profit by typing `report`.

## Example Usage

```
What would you like? (espresso/latte/cappuccino): latte
How many quarters?: 2
How many dimes?: 1
How many nickles?: 0
How many pennies?: 3
Here is $0.85 in change.
Here is your latte ☕️. Enjoy!
```

## Note
If the resources run low or money is insufficient, the program will notify the user and ask them to either insert more money or choose another option.

