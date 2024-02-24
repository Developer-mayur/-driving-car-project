Program Behavior
When the program starts User should see
Miles per gallon: 20
Tank Size (in gallons): 25
(Note: these values are read from the file and are NOT hard-coded)
Then the program should show the MAIN MENU and ask the user what to do
What would you like to do:
1. See Current Fuel Level
2. Drive
3. Add Gas
4. Exit
If user inputs 1, program displays Current Fuel Level and returns to MAIN MENU
The program also writes/appends the user input and associated result to a log file called
LogFuel.txt
If the user inputs 2, the program asks
How many miles to Drive:
Let’s say the user inputs 100.
Program displays
You drove 100 miles. You can drive another 400 miles on this gas.
The program also writes/appends the user input and associated result to a log file called
LogFuel.txt
If the user inputs 3, the program asks
How much gas to Add:
Give the appropriate message, i.e. whether gas was added and how much.
The program also writes/appends the user input and associated result to a log file called
LogFuel.txt
If the user inputs 4, the program exits
LogFuel.txt may look like the following
User Input: 1 - See Current Fuel Level
Fuel level shown: 25 gallons
User Input: 2 – Drive
Miles to Drive: 100
User Input: 1 - See Current Fuel Level
Fuel level shown: 20 gallons
User Input: 4 – Exit
Final Note: Do all Error Handling, e.g. not allowing to drive more miles than the current
maximum, not allowing to fill in more gas, etc.
