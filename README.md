AirBnB Command Interpreter

This project is a command-line interface (CLI) tool developed as the first step towards building an AirBnB clone. The purpose of this tool is to manage AirBnB objects such as users, states, cities, places, etc., through various commands executed in the terminal.

Command Interpreter
The command interpreter allows users to perform the following actions:

Create a new object (e.g., User, Place)
Retrieve an object from a file, database, etc.
Perform operations on objects (e.g., count, compute stats)
Update attributes of an object
Destroy an object
How to Start
To start the command interpreter, follow these steps:

Clone the repository to your local machine.
Navigate to the project directory.
Run the command ./console.py to start the command interpreter.
How to Use
Once the command interpreter is running, you can enter commands to interact with AirBnB objects. The general syntax for commands is as follows:
create User: Creates a new instance of the User class.
show Place 123: Displays information about the place with ID 123.
update Place 456 price 100: Updates the price attribute of the place with ID 456 to 100.
destroy User 789: Deletes the user with ID 789.
all City: Displays all instances of the City class.
quit or EOF: Exits the command interpreter.
Examples
Create a new user:
Examples
1:Create a new user:

2:Show information about a specific place with ID 123:

3:Update the price attribute of a place with ID 456:

4:Destroy a user with ID 789:

5:Display all cities:
Next Steps
This command interpreter serves as the foundation for building the complete AirBnB clone. In future steps, additional features such as HTML/CSS templating, database storage, API integration, and front-end development will be implemented.

For more information and detailed usage instructions, refer to the documentation and project resources.
Note: This project is part of a series of projects aimed at building a full-fledged AirBnB clone. Each subsequent project will build upon the functionalities implemented in this command interpreter.
