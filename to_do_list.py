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
        self.data_folder = os.path.relpath("data/")
        self.list_file = self.data_folder + f"/{self.list_name}.txt"
        self.task_list = []
        
    def add_task(self,task):
        self.write_file = open(self.list_file, "a+")
            
        with self.write_file as wf:
            wf.write(str(task)+"\n")
            print(f"'{task.description}' successfully created.")
    
    def remove_task(self,index):
        if os.path.exists(self.list_file):
            self.read_file = open(self.list_file, "r")
            self.write_list = []
            
            with self.read_file as rf:
                for line in rf:
                    self.write_list.append(line.replace("\n", ""))
            
            if index in range(0, len(self.write_list)):
                rem_task = self.write_list.pop(index)
                print(f"'{rem_task}' successfully deleted")

                self.write_file = open(self.list_file, "w")

                with self.write_file as wf:
                    for task in self.write_list:
                        wf.write(str(task)+"\n")
            else:
                print("Please enter a valid index position!")
        else:
            print("There are currently no tasks to remove!")
        
    def read_list(self):
        if os.path.exists(self.list_file):  
            self.read_file = open(self.list_file, "r+")

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

def exit():
    display_menu('yes_no')
    exit = ''
    
    while exit != 'y' and exit != 'n':
        exit = input("Would you like to exit the program: ").lower()
    
    if exit == 'y':
        return True
    else:
        return False

def display_menu(menu_type):
    # Add menu colors perhaps?
    # Could make menu into a class?
    if  menu_type == 'main':
        print('╔═══════════════════╗')
        print('║     MAIN MENU     ║')
        print('╠═══════════════════╣')
        print('║   CHOOSE LIST: C  ║')
        print('║   NEW LIST: N     ║')
        print('║   EXIT: E         ║')
        print('╚═══════════════════╝')
    elif menu_type == 'list':
        print('╔═══════════════════╗')
        print('║     LIST MENU     ║')
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

def list_menu(list_inst):
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

def main_menu():
    display_menu('main')
    
    argument = ''
    options = ['c','n','e']
    
    while argument not in options:
        input_color("Please select an option from the main menu: ")
        argument = input().lower()
        
    if argument == 'c':
        list_chosen = choose_list()
        return list_chosen
    if argument == 'n':
        new_list = create_list()
        return new_list
    elif argument == 'e':
        return exit()

def create_list():
    list_name = ''
    
    list_name = input("Create a name for your list: ").lower()
    
    return list_name

def choose_list():
    list_choice = ''
    file_dir = os.listdir("data/")
    options = []
    
    if len(file_dir) == 0:
        print("You have not made any lists! What would you like to call your first list: ")
        pass
    else:
        for index, file in enumerate(file_dir):
            options.append(file.replace(".txt",""))
            print("{}) {}".format(index, file.replace(".txt",'')))

        while list_choice not in options:
            list_choice = input("Choose a list to navigate: ")

        return list_choice   
        
if __name__ == "__main__":
    
    if not os.path.exists('data'):
        os.makedirs('data')
    
    while True:
        
        menu_choice = main_menu()
        
        if menu_choice == True:
            break
        elif menu_choice == None:
            menu_choice = create_list()
            
            my_todo_list = Todo_list(menu_choice)
            
            display_menu('list')
            
            while True:
                if list_menu(my_todo_list) == True:
                    break
        elif menu_choice != False:
            my_todo_list = Todo_list(menu_choice)
            
            display_menu('list')
            
            while True:
                if list_menu(my_todo_list) == True:
                    break