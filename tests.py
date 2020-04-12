from IPython.display import clear_output

class Task():
    
    def __init__(self,description,status):
        self.description = description
        self.status = status
        
    def __str__(self):
        return f"{self.description} - Status: {self.status}"

class Todo_list():
    
    def __init__(self):
        self.task_list = []
    
    def add_task(self,task):
        self.task_list.append(task)
        
    def remove_task(self,index):
        self.task_list.pop(index)
            
    def show_list(self):
        for index, task in enumerate(self.task_list):
            print(index, task)

def create_task(list_inst):
    
    task = ''
    # Can be assumed if adding new thing status is incomplete
    status = False
    
    while task == '':
        task = input("What would you like to add to your list: ")
    
    new_task = Task(task, status)
    list_inst.add_task(new_task)
    print(f"'{new_task.description}' successfully created.")

def delete_task(list_inst):
    
    index = -1
    
    while index == -1:
        list_inst.show_list()
        try:
            index = int(input("Please specify the task index to delete it from the list: "))
        except:
            print("Please enter an integer value for the index.")
    try: 
        list_inst.remove_task(index)
        print("Task deleted.")
    except:
        print('Please enter an existing index value')

def exit():
    
    exit = ''
    
    while exit.upper() != 'Y' and exit.upper() != 'N':
        exit = input("Would you like to exit the program?(Y/N): ")
    
        if exit.upper() == 'Y':
            return True
            break
        else:
            return False
            break

def main_menu():
    clear_output()
    print('╔═══════════════════╗')
    print('║     MAIN MENU     ║')
    print('╠═══════════════════╣')
    print('║   CREATE TASK: C  ║')
    print('║   DELETE TASK: D  ║')
    print('║   SHOW LIST: S    ║')
    print('║   EXIT: E         ║')
    print('╚═══════════════════╝')

def navigate_menu(list_inst):

    # Add menu colors perhaps?
    
    argument = ''
    options = ['c','d','s','e']
    
    while argument.lower() not in options:
        argument = input("Please select an option from the main menu: ")
        
    if argument == 'c':
        create_task(list_inst)
    elif argument == 'd':
        delete_task(list_inst)
    elif argument == 's':
        list_inst.show_list()
    elif argument == 'e':
        return exit()
        
#---------------[ V1.1 ]---------------

import os

class Task():
    def __init__(self,description,status):
        self.description = description
        self.status = status
        
    def __str__(self):
        return f"{self.description} - Status: {self.status}"
        
class Todo_list():
    def __init__(self):
        self.task_list = []
        
    def add_task(self,task):
        self.write_file = open("list.txt", "a+")
            
        with self.write_file as wf:
            wf.write(str(task)+"\n")
            print(f"'{task.description}' successfully created.")
    
    def remove_task(self,index):
        if os.path.exists("list.txt"):
            self.read_file = open("list.txt", "r")
            self.write_list = []
            
            with self.read_file as rf:
                for line in rf:
                    self.write_list.append(line.replace("\n", ""))
            
            if index in range(0, len(self.write_list)):
                rem_task = self.write_list.pop(index)
                print(f"'{rem_task}' successfully deleted")

                self.write_file = open("list.txt", "w")

                with self.write_file as wf:
                    for task in self.write_list:
                        wf.write(str(task)+"\n")
            else:
                print("Please enter a valid index position!")
        else:
            print("There are currently no tasks to remove!")
        
    def read_list(self):
        if os.path.exists("list.txt"):  
            self.read_file = open("list.txt", "r+")

            with self.read_file as rf:
                self.line = rf.readline()
                self.cnt = 0
                while self.line:
                    print(f"{self.cnt}) {self.line.strip()}")
                    self.line = rf.readline()
                    self.cnt += 1
        else:
            print("Your list is currently empty!")
            
def create_task(list_inst):
    task = ''
    status = False  # Can be assumed if adding new thing status is incomplete
    
    while task == '':
        task = input("What would you like to add to your list: ")
    
    new_task = Task(task, status)
    list_inst.add_task(new_task)

def delete_task(list_inst):
    index = -1
    
    list_inst.read_list()
    while index == -1:
        try:
            index = int(input("Specify the task index to delete it from the list: "))
        except:
            print("Please enter an integer value for the index.")
            
        list_inst.remove_task(index)
        
def main_menu():
    # Add menu colors perhaps?
    print('╔═══════════════════╗')
    print('║     MAIN MENU     ║')
    print('╠═══════════════════╣')
    print('║   CREATE TASK: C  ║')
    print('║   DELETE TASK: D  ║')
    print('║   SHOW LIST: S    ║')
    print('║   EXIT: E         ║')
    print('╚═══════════════════╝')
    
def navigate_menu(list_inst):
    argument = ''
    options = ['c','d','s','e']
    
    while argument not in options:
        argument = input("Please select an option from the main menu: ").lower()
        
    if argument == 'c':
        create_task(list_inst)
    elif argument == 'd':
        delete_task(list_inst)
    elif argument == 's':
        list_inst.read_list()
    elif argument == 'e':
        return exit()
        
def exit():
    exit = ''
    
    while exit != 'y' and exit != 'n':
        exit = input("Would you like to exit the program?(Y/N): ").lower()
    
        if exit == 'y':
            return True
            break
        else:
            return False
            break

#---------------[ V1.2 ]---------------

import os
from colorama import init
from colorama import Fore
init()

class Task():
    def __init__(self,description,status):
        self.description = description
        self.status = status
        
    def __str__(self):
        return f"{self.description} - Status: {self.status}"
        
class Todo_list():
    def __init__(self,list_name):
        self.list_name = list_name
        self.task_list = []
        
    def add_task(self,task):
        self.write_file = open(f"{self.list_name}.txt", "a+")
            
        with self.write_file as wf:
            wf.write(str(task)+"\n")
            print(f"'{task.description}' successfully created.")
    
    def remove_task(self,index):
        if os.path.exists(f"{self.list_name}.txt"):
            self.read_file = open(f"{self.list_name}.txt", "r")
            self.write_list = []
            
            with self.read_file as rf:
                for line in rf:
                    self.write_list.append(line.replace("\n", ""))
            
            if index in range(0, len(self.write_list)):
                rem_task = self.write_list.pop(index)
                print(f"'{rem_task}' successfully deleted")

                self.write_file = open(f"{self.list_name}.txt", "w")

                with self.write_file as wf:
                    for task in self.write_list:
                        wf.write(str(task)+"\n")
            else:
                print("Please enter a valid index position!")
        else:
            print("There are currently no tasks to remove!")
        
    def read_list(self):
        if os.path.exists(f"{self.list_name}.txt"):  
            self.read_file = open(f"{self.list_name}.txt", "r+")

            with self.read_file as rf:
                self.line = rf.readline()
                self.cnt = 0
                while self.line:
                    print(f"{self.cnt}) {self.line.strip()}")
                    self.line = rf.readline()
                    self.cnt += 1
        else:
            print("Your list is currently empty!")
            
def input_color(my_string):
    print(Fore.CYAN + my_string + Fore.RESET)
    
def status_code():
    display_menu('status_options')
    
    argument = ''
    status_codes = ['i','p','c']

    while argument not in status_codes:
        argument = input("Please select a status code from the options menu: ").lower()

    if argument == 'i':
        argument = Fore.RED + 'INCOMPLETE' + Fore.RESET
    if argument == 'p':
        argument = Fore.YELLOW + 'IN PROGRESS' + Fore.RESET
    if argument == 'c':
        argument = Fore.GREEN + 'COMPLETED' + Fore.RESET

    return argument
            
def create_task(list_inst):
    task = ''
    status = ''
    
    while task == '':
        task = input("What would you like to add to your list: ")
        
    status = status_code()
    new_task = Task(task, status)
    list_inst.add_task(new_task)

def delete_task(list_inst):
    index = -1
    
    list_inst.read_list()
    while index == -1:
        try:
            index = int(input("Specify the task index to delete it from the list: "))
        except:
            print("Please enter an integer value for the index.")
            
        list_inst.remove_task(index)
        
def display_menu(menu_type):
    # Add menu colors perhaps?
    # Could make menu into a class?
    if menu_type == 'main':
        print('╔═══════════════════╗')
        print('║     MAIN MENU     ║')
        print('╠═══════════════════╣')
        print('║   CREATE TASK: C  ║')
        print('║   DELETE TASK: D  ║')
        print('║   SHOW LIST: S    ║')
        print('║   EXIT: E         ║')
        print('╚═══════════════════╝')
    elif menu_type == 'status_options':
        print('╔═══════════════════╗')
        print('║      OPTIONS      ║')
        print('╠═══════════════════╣')
        print('║   INCOMPLETE: I   ║')
        print('║   IN PROGRESS: P  ║')
        print('║   COMPLETED: C    ║')
        print('╚═══════════════════╝')
    elif menu_type == 'yes_no':
        print('╔═══════════════════╗')
        print('║      OPTIONS      ║')
        print('╠═══════════════════╣')
        print('║   YES: Y          ║')
        print('║   NO: N           ║')
        print('╚═══════════════════╝')
    
def navigate_menu(list_inst):
    argument = ''
    options = ['c','d','s','e']
    
    while argument not in options:
        input_color("Please select an option from the main menu: ")
        argument = input().lower()
        
    if argument == 'c':
        create_task(list_inst)
    elif argument == 'd':
        delete_task(list_inst)
    elif argument == 's':
        list_inst.read_list()
    elif argument == 'e':
        return exit()
        
def exit():
    display_menu('yes_no')

    exit = ''
    
    while exit != 'y' and exit != 'n':
        exit = input("Would you like to exit the program: ").lower()
    
    if exit == 'y':
        return True
    else:
        return False

if __name__ == "__main__":
    
    my_todo_list = Todo_list('list')

    display_menu('main')

    while True:
        if navigate_menu(my_todo_list) == True:
            break

# if __name__ == "__main__":

	# my_todo_list = Todo_list()
	
	# while True:
		# main_menu()
		# if navigate_menu(my_todo_list) == True:
			# break