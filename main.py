class Car:
    def __init__(self, mpg, tank_size):
        self.mpg = mpg
        self.tank_size = tank_size
        self.fuel_level = 0

    def drive(self, miles):
        max_miles = self.fuel_level * self.mpg
        if miles <= max_miles:
            self.fuel_level -= miles / self.mpg
            print(f"You drove {miles} miles. You can drive another {max_miles - miles} miles on this gas.")
            self.log_activity(f"Drive: {miles} miles")
        else:
            print("Not enough fuel to drive that far.")

    def getGasLevel(self):
        return self.fuel_level

    def addGas(self, gallons):
        if self.fuel_level + gallons <= self.tank_size:
            self.fuel_level += gallons
            print(f"Added {gallons} gallons of gas.")
            self.log_activity(f"Added {gallons} gallons of gas.")
        else:
            print("Tank is full, cannot add more gas.")

    def log_activity(self, activity):
        with open('LogFuel.txt', 'a') as file:
            file.write(activity + '\n')


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        mpg = int(lines[0].split(':')[1].strip())
        tank_size = int(lines[1].split(':')[1].strip())
        return mpg, tank_size


def main():
    mpg, tank_size = read_data_from_file('FuelEffic.txt')
    myHybrid = Car(mpg, tank_size)
    print(f"Miles per gallon: {mpg}")
    print(f"Tank Size (in gallons): {tank_size}")

    while True:
        print("\nMAIN MENU")
        print("What would you like to do:")
        print("1. See Current Fuel Level")
        print("2. Drive")
        print("3. Add Gas")
        print("4. Exit")

        choice = input("Enter your choice:\n")

        if choice == '1':
            print(f"Current Fuel Level: {myHybrid.getGasLevel()} gallons")
        elif choice == '2':
            miles_to_drive = int(input("How many miles to Drive: "))
            myHybrid.drive(miles_to_drive)
        elif choice == '3':
            gallons_to_add = int(input("How much gas to Add: "))
            myHybrid.addGas(gallons_to_add)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
