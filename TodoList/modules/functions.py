FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    """
        Read the text file and return
        the todos 
    """
    with open(filepath,'r') as file:
        todos=file.readlines()
        return todos
def write_todos(todos,filepath=FILEPATH):
    """
        Write the todos to file 
    """
    with open(filepath,'w') as file:
        file.writelines(todos)

print(__name__) 
if __name__=="__main__":
    todos=get_todos()
    print(todos)