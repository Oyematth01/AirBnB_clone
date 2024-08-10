#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project.
"""
import cmd
from models.base_model import BaseModel
import sys

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB clone project.
    """
    prompt = '(hbnb) '

    def do_create(self, args):
        """
        Create a new instance of BaseModel, save it, and print the id.
        Usage: create <ClassName>
        """
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Show the string representation of an instance based on the class name and id.
        Usage: show <ClassName> <id>
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            instance = eval(args[0])()
            instance_id = args[1]
            print(instance)
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty line input.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
