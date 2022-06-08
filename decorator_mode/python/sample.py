from Product_type import *

def main():
    beverage = BlackTea()
    beverage = Milk(beverage)
    beverage = Bubble(beverage)

    print(beverage.get_description())
    print(beverage.cost())

if __name__ == "__main__":
    main()
