from modules import functions
import PySimpleGUI as sg

sg.theme('DarkAmber')
label=sg.Text('Type in a todo')
input_box=sg.InputText(tooltip='Enter a todo',key='todo')
add_button=sg.Button('Add')
edit_button=sg.Button('Edit')
complete_button=sg.Button('Complete')
exit_button=sg.Button('Exit')
list_box=sg.Listbox(values=functions.get_todos(),
                    key='todos',
                    size=[45,10],
                    enable_events=True)

window=sg.Window('My todo app',layout=[
    [label],
    [input_box,add_button],
    [list_box,edit_button,complete_button],
    [exit_button]])

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
        print('todo is ',todo_to_edit)
        new_to_do=values['todo']
        print('todo is ',new_to_do)
        todos=functions.get_todos()
        index=todos.index(todo_to_edit)
        todos[index]=new_to_do
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif(event=='Complete'):
        to_do_delete=values['todos'][0]
        todos=functions.get_todos()
        todos.remove(to_do_delete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')
    elif(event=='Exit'):
        break
    elif(event=='todos'):
        window['todo'].update(value=values['todos'][0])
    elif(event==sg.WIN_CLOSED):
        break

window.close()