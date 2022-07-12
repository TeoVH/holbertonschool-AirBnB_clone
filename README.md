![image](https://user-images.githubusercontent.com/98335124/177196137-35b5a657-1f9d-45b3-8e96-45a0fd659660.png)
***

# holbertonschool-AirBnB_clone
***
This project is about creating a clone of the AirBnB application, creating classes with their respective attributes and managing data storage in such a way that it is more interactive.
This first step is very important because we will use what is built during this project with all the other projects below: HTML/CSS templates, database storage, APIs, front-end integration.

Each task will be linked so it will help you:
* Establish a main class called (`BaseModel`) to take care of the initialization, serialization and deserialization of its future instances
* Create a simple serialize/deserialize flow: Instance <-> Dictionary <-> JSON String <-> file
* Create all classes used for AirBnB (`User`, `State`, `City`, `Place`...) that inherit from `BaseModel`
* Create the project's first abstract storage engine: file storage.
* Create all the unit tests to validate all our classes and storage engine
***

## Folders and Files

| Folders and Files  | Description |
| ------------- |:-------------:|
| [Models](https://github.com/David-VargasV/holbertonschool-AirBnB_clone/tree/main/models)      | Contains the classes     |
| [tests](https://github.com/David-VargasV/holbertonschool-AirBnB_clone/tree/main/tests)      | Files containing unittest     |
| [console.py](https://github.com/David-VargasV/holbertonschool-AirBnB_clone/blob/main/console.py)      | Interpreter that allows executing all classes     |
| [AUTHORS](https://github.com/David-VargasV/holbertonschool-AirBnB_clone/blob/main/AUTHORS) | Authors of this project |
***

## Interpreter command description
***
### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

| Command  | Description |
| ------------- |:-------------:|
| `quit` | Command to exit the program  |
| `EOF` | Command to exit the program  |
| `help` | Displays a description of the command  |
| `create` | Create a new instance, save it and print the id  |
| `show` | Prints the string representation of an instance based on the class name and id  |
| `destroy` | Deletes an instance based on the class name and id  |
| `all` | Prints all string representation of all instances based or not on the class name  |
| `update` | Updates an instance based on the class name and id by adding or updating attribute  |

### How to start it?

* Clone this repository
```
https://github.com/David-VargasV/holbertonschool-AirBnB_clone.git
```
* Run console `console.py`

`holbertonschool-AirBnB_clone$ ./console.py`

### How to use it?
* run console
```
./console.py
```
* The console is ready to receive commands

![image](https://user-images.githubusercontent.com/98335124/177201580-8b8007e2-27f4-47f0-8d78-127d51d7ca5b.png)

### Examples
* Run the console
```
./console.py
```

```
holbertonschool-AirBnB_clone$ ./console.py 
(hbnb)
```

```
holbertonschool-AirBnB_clone$ ./console.py 
(hbnb) EOF
holbertonschool-AirBnB_clone$ 
```

```
holbertonschool-AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

```
holbertonschool-AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help destroy
 Deletes an instance based on the class name and id 
(hbnb) 
```
***

## Authors
***
[David Vargas](https://github.com/David-VargasV) :computer: :grin: :evergreen_tree:

[Mateo Villada](https://github.com/TeoVH) :computer: :smile: :leaves:
***

![image](https://user-images.githubusercontent.com/98335124/177203775-a34f7339-1f05-4ccb-af1e-0f3854ff98cd.png)
***

# **Enjoy life !!!** :v: 

