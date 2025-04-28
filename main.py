import tkinter as tk
from tkinter import messagebox
from task_manager import Task_Manager

# Create the object
task_manager = Task_Manager() # Default name of the file

# Load tasks from the file
task_manager.load_tasks()

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in task_manager.get_tasks():
        task_listbox.insert(tk.END, task)
    
def add_task():
    task = task_entry.get()

    if task:
        task_manager.add_task(task)
        task_entry.delete(0, tk.END)
        update_task_listbox()
        task_manager.save_tasks()
    else:
        messagebox.showwarning("Advertencia","La tarea no debe estar vacía.")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_manager.delete_task(selected)
        update_task_listbox()
        task_manager.save_tasks()
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar")

# Create main window
root = tk.Tk()
root.title("Gestor de Tareas")

# Text entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Agregar tarea", command=add_task)
add_button.pack(pady=5)

# Listbox, show tasks
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

# Delete task button
delete_button = tk.Button(root, text= "Eliminar tarea", command=delete_task)
delete_button.pack(pady=10)

# Update listbox
update_task_listbox()

# Run interphace
root.mainloop()