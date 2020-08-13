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
            my_list = line.split(" ")
            obj = eval("{}()".format(my_list[0]))
            for arg in range(1, len(my_list)):
                my_list[arg] = my_list[arg].replace("=", " ")
                attr = my_list[arg].split()
                attr[1] = attr[1].replace("_", " ")
                try:
                    save = eval(attr[1])
                    attr[1] = save
                except:
                    pass
                if (type(attr[1]) is not tuple):
                    setattr(obj, attr[0], attr[1])
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        ''' Prints the string representation of id instance '''
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.classes:
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

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id '''
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
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

    def do_all(self, line):
        ''' Prints all string representation of all instances '''
        objects = storage.all()
        my_list = []
        if not line:
            for key in objects:
                my_list.append(objects[key])
            print(my_list)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.classes:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    my_list.append(objects[key])
            print(my_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        ''' Update an instance based on the class name and id '''
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

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
