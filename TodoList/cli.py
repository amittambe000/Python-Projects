from modules.functions import get_todos,write_todos 
while True:
    user_input=input("Type add/show/edit/complete/exit: ").strip()
    if user_input.startswith('show'):
        todos=get_todos()
        for index,item in enumerate(todos):
            print(f"{index+1}-{item}")
    elif user_input.startswith('add'):
         todo=user_input[4:]+'\n'
         ## Read File
         todos=get_todos()
         todos.append(todo.capitalize())

        ## Write to file
         write_todos(todos)
    elif user_input.startswith('edit'):
        try:
            number=int(user_input[5:])
            number=number-1
            todos=get_todos("todos.txt")
            existing_todo=todos[number]
            todo=input("Enter the new todo")
            todos[number]=todo +'\n'
            write_todos(todos)
        except ValueError:
            print('You enter wrong command')
            continue

    elif user_input.startswith('complete'):
        try:
            number=int(user_input[9:])
            todos=get_todos()
            todos.pop(number-1)
            write_todos(todos)
        except IndexError:
            print('There is no task with that number')
            continue

    elif user_input.startswith('exit'):
        break
    else:
        print('Not a valid command')

print("Bye..")

