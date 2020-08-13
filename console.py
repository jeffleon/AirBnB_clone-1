#!/usr/bin/env python3
'''
Console for Airbnb project
'''
import cmd
import sys
from datetime import datetime, date
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' Class for Airbnb CLI '''
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

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

    def do_quit(self, arg):
        ''' quit command for cmd '''
        return True

    def do_EOF(self, arg):
        ''' EOF command for cmd '''
        print()
        return True

    def emptyline(self):
        ''' Do anything with Enter '''
        pass

    def do_create(self, line):
        ''' Creates a new instance of BaseModel, saves it in JSON file '''
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

    def do_show(self, line):
        ''' Prints the string representation of id instance '''
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

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id '''
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

    def do_all(self, arg):
        ''' Prints all string representation of all instances '''
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

    def do_update(self, line):
        ''' Update an instance based on the class name and id '''
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

    def do_count(self, arg):
        '''Count instances of class passed as arg'''
        cnt = 0
        for key in storage.all().items():
            instance = key.split('.')[0]
            if instance == arg:
                cnt += 1
        print(cnt)

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
