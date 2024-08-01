## The AirBnB Clone Project

![AirBnB](AirBnB.png)

### Project Goal

The goal of this project is to deploy a simple copy of the AirBnB website on a server.
![Image description of the Clone Project](The_clone_deescription_image.png)

### Project Description

In the first phase of the AirBnB clone project, we developed the backend and integrated it with a console application using Python's `cmd` module. The data generated (Python objects) is stored in a JSON file, which can be accessed and manipulated using Python's `json` module.

### Description of the Command Interpreter

The interface of the application is similar to the Bash shell but with a limited set of commands designed specifically for the AirBnB website. This command line interpreter acts as the frontend, allowing users to interact with the backend, built using Python's object-oriented programming.

#### Available Commands

- `show`
- `create`
- `update`
- `destroy`
- `count`

You can perform the following actions with the command line interpreter:

1. **Create new objects**:
   - Example: `create User name="John Doe" email="johndoe@example.com` creates a new User object with the specified name and email.

2. **Retrieve an object from a file or database**:
   - Example: `show User 1234-5678-9101` retrieves the User object with the ID `1234-5678-9101` from storage.

3. **Perform operations on objects** (e.g., count or compute statistics):
   - Example: `count User` returns the number of User objects stored.

4. **Update object attributes**:
   - Example: `update User 1234-5678-9101 email="newemail@example.com"` updates the email attribute of the User object with the ID `1234-5678-9101`.

5. **Delete an object**:
   - Example: `destroy User 1234-5678-9101` deletes the User object with the ID `1234-5678-9101` from storage.

### How to Start the Project

These instructions will help you get a copy of the project running on your local machine (Linux) for development and testing.

#### Installing

1. **Clone the Repository**: Download the project from GitHub using the following command:
   ```bash
   git clone https://github.com/jzamora5/AirBnB_clone.git
   ```
   This will create a folder called `AirBnB_clone` containing all the necessary files.

2. **Project Structure**: The main files include:
   - `console.py`: The command interpreter.
   - `models/engine/file_storage.py`: Handles serialization to and from a JSON file.
   - `models/__init__.py`: Creates a unique `FileStorage` instance.
   - `models/base_model.py`: Defines common attributes/methods for other classes.
   - `models/user.py`: Defines the `User` class.
   - `models/state.py`: Defines the `State` class.
   - `models/city.py`: Defines the `City` class.
   - `models/amenity.py`: Defines the `Amenity` class.
   - `models/place.py`: Defines the `Place` class.
   - `models/review.py`: Defines the `Review` class.

### How to Use the Command Line Interpreter

The command line interpreter can run in two modes: Interactive and Non-interactive.

#### Interactive Mode

In Interactive mode, you can type commands directly into the prompt (`hbnb`). The prompt waits for commands indefinitely until you exit the program.

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
```

#### Non-interactive Mode

In Non-interactive mode, you can pipe commands into the shell, which runs them immediately without displaying a prompt.

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Command Input Format

In Interactive Mode, type commands when the prompt appears and press Enter. To exit, use `CTRL + D`, `CTRL + C`, or type `quit` or `EOF`.

In Non-interactive Mode, pipe commands using `echo` or from a file.

### Arguments

Commands can have options or arguments separated by spaces.

Example:

```bash
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
```

Or:

```bash
$ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
$
```

### Available Commands

Here are the commands recognized by the interpreter:

| Command        | Description                                                                                   | Usage                                                     |
|----------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| quit or EOF    | Exits the program                                                                              | By itself                                                 |
| help           | Provides information on how to use a command                                                  | By itself or `help <command>`                             |
| create         | Creates a new instance of a valid class, saves it to the JSON file, and prints the ID         | `create <class name>`                                     |
| show           | Prints the string representation of an instance based on the class name and ID                | `show <class name> <id>` or `<class name>.show(<id>)`     |
| destroy        | Deletes an instance based on the class name and ID, saving the change to the JSON file        | `destroy <class name> <id>` or `.destroy()`               |
| all            | Prints string representations of all instances, optionally based on the class name            | By itself, `all <class name>`, or `<class name>.all()`    |
| update         | Updates an instance based on the class name and ID by adding or updating attributes           | `update <class name> <id> <attribute name> "<attribute value>"` or `<class name>.update(<id>, <attribute name>, <attribute value>)` or `<class name>.update(<id>, <dictionary representation>)` |
| count          | Retrieves the number of instances of a class                                                  | `<class name>.count()`                                    |

### Examples of Actions

1. **Create a new object**:
   ```bash
   (hbnb) create User name="John Doe" email="johndoe@example.com"
   ```

2. **Retrieve an object**:
   ```bash
   (hbnb) show User 1234-5678-9101
   ```

3. **Perform operations on objects**:
   ```bash
   (hbnb) count User
   ```

4. **Update object attributes**:
   ```bash
   (hbnb) update User 1234-5678-9101 email="newemail@example.com"
   ```

5. **Delete an object**:
   ```bash
   (hbnb) destroy User 1234-5678-9101
   ```