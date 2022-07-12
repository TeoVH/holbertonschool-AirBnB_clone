#!/usr/bin/python3
""" Program called console.py that
contains the entry point of the command interpreter
"""

import cmd
import sys
from unittest import installHandler
from venv import create
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ Class definition  """
    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_quit(self, arg):
        """ Use quit to exit of the console """
        return True

    def do_EOF(self, arg):
        """ Exit of the console """
        return True

    def do_help(self, arg):
        """ Shows the commands of the console """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """ Empty line does not execute anything """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of
        an instance based on the class name and id """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        tokens = arg.split()
        objectDic = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] + "." + tokens[1] in objectDic.keys():
            del objectDic[tokens[0] + "." + tokens[1]]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all
        instances based or not on the class name"""
        tokens = arg.split()
        if len(tokens) > 0 and tokens[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_list = []
            for obj in storage.all().values():
                if len(tokens) > 0 and tokens[0] == obj.__class__.__name__:
                    new_list.append(obj.__str__())
                elif len(tokens) == 0:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute:
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
