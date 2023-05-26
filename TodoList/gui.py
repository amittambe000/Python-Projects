from modules import functions
import PySimpleGUI as sg

sg.theme('DarkAmber')
label=sg.Text('Type in a todo')
input_box=sg.InputText(tooltip='Enter a todo',key='todo')
add_button=sg.Button('Add')
edit_button=sg.Button('Edit')
list_box=sg.Listbox(values=functions.get_todos(),
                    key='todos',
                    size=[45,10],
                    enable_events=True)

window=sg.Window('My todo app',layout=[
    [label],
    [input_box,add_button],
    [list_box,edit_button]])

while True:
    event,values =window.read()
    print(event)
    print(values)
    if(event=='Add'):
        todos=functions.get_todos()
        todos.append(values['todo']+'\n')
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif(event=='Edit'):
        todo_to_edit=values['todos'][0]
        new_to_do=values['todo']
        todos=functions.get_todos()
        index=todos.index(todo_to_edit)
        todos[index]=new_to_do+'\n'
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif(event=='todos'):
        window['todo'].update(value=values['todos'][0])
    elif(event==sg.WIN_CLOSED):
        break

window.close()