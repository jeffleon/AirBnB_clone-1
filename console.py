#!/usr/bin/python3
"""Console for Airbnb"""
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def precmd(self, line):
        ''' Non-interactive mode & process line before execute commands '''
        if '.' in line and '(' in line and ')' in line:
            splited = line.split('.')
            arg_class = splited[0]
            cmd = splited[1].split('(')[0]
            args_list = splited[1].split('(')[1].split(')')[0].split(', ')
            line = cmd + ' ' + arg_class + ' ' + args_list[0]
            if len(args_list) > 1:
                line = line + ' ' + args_list[1] + ' ' + args_list[2]
        return line

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        try:
            if not line:
                raise SyntaxError()
            args = line.split(" ")
            obj = eval("{}()".format(args[0]))
            for param in args[1:]:
                lists = param.split("=")
                lists[1] = lists[1].strip('"')
                lists[1] = lists[1].replace('_', ' ')
                setattr(obj, lists[0], lists[1])
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        args = line.split()
        print(args)
        if not args:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                print(storage.all()[key])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                storage.all().pop(key)
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, arg):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
        """
        if not arg:
            my_list = [str(value) for key, value in storage.all().items()]
            if len(my_list) != 0:
                print(my_list)
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            my_list = [str(value) for key,
                       value in storage.all().items() if arg in key]
            if len(my_list) != 0:
                print(my_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (args[0] not in self.classes):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                storage.all()[key]
            except KeyError:
                print('** no instance found **')
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                key = args[0] + '.' + args[1]
                try:
                    if '.' in args[3]:
                        value = float(args[3])
                    else:
                        value = int(args[3])
                except ValueError:
                    value = str(args[3]).strip("\"':")
                    value = str(value)
                    setattr(storage.all()[key], args[2].strip("\"':"), value)
                    storage.save()

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def do_count(self, arg):
        '''Count instances of class passed as arg'''
        cnt = 0
        for key in storage.all().items():
            instance = key.split('.')[0]
            if instance == arg:
                cnt += 1
        print(cnt)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
