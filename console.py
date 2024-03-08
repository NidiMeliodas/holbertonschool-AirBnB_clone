#!/usr/bin/python3
"""Module for HBNB command interpreter."""

import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB console."""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            instance_key = f"{class_name}.{args[1]}"
            if instance_key not in instances:
                print("** no instance found **")
                return
            print(instances[instance_key])
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            instance_key = f"{class_name}.{args[1]}"
            if instance_key not in instances:
                print("** no instance found **")
                return
            del instances[instance_key]
            storage.save()
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Print string representation of all instances."""
        args = arg.split()
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return
        try:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in storage.all().items()
                   if key.startswith(class_name)])
        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            instance_key = f"{class_name}.{args[1]}"
            if instance_key not in instances:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            instance = instances[instance_key]
            setattr(instance, attr_name, attr_value)
            instance.save()
        except Exception as e:
            print(e)

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
