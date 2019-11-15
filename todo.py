
def print_todos(todos):
    if len(todos) == 0:
        print("You have nothing to do.")
    else:
        # i = 0
        # for todo in todos:
        #     print(f"{i}: {todo}")
        #     i += 1
        print("====Pending=======")
        for key in todos.keys():
            if todos[key]['completed'] == False:
                print(f"{todos[key]['index']}. {todos[key]['title']}")
        print("==================")
        print("====Completed=====")
        for key in todos.keys():
            if todos[key]['completed'] == True:
                print(f"{todos[key]['index']}. {todos[key]['title']}")
        print("==================")


            # ========Pending========
            # 0. titles in dictionary
            # 1. title in dictionary
            # =======================
            # ========Completed======
            # index number. title
            # =======================

def add_todo(todos, item):
    # todos.append(item)
    todos[item] = {
        "title": item,
        "completed": False,
        "index": len(todos)
    }
    # print(todos)

def delete_todo(todos, item):
    try:
        todos[item]['completed'] = True
        # print(todos)
    except KeyError:
        print("That todo does not exist.")

def print_menu():
    message = """
    Todo App
==================
0. quit
1. print todos
2. add a todo
3. complete a todo
4. clear todo list
"""
    print(message)

def get_choice(prompt="Choose one: "):
    is_valid_choice = False
    choice = 0
    while not is_valid_choice:
        try:    
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Please enter a number.")
    return choice

def clear_todos(todos):
    todos = {

    }
    return todos
    
def main():
    todo_list = {
        
    }

    
    is_running = True
    while is_running:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("K. Byeeee!")
            is_running = False
        elif choice == 1:
            print_todos(todo_list)
        elif choice == 2:
            new_todo = input("Enter a todo: ")
            add_todo(todo_list, new_todo)
        elif choice == 3:            
            item_to_delete = input("Enter the item to complete: ")
            delete_todo(todo_list, item_to_delete)
        elif choice == 4:
            todo_list = clear_todos(todo_list)
        

main()
