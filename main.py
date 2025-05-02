import tkinter as tk
from tkinter import messagebox, simpledialog
from task_manager import Task_Manager

#If we wanna create a new file or not
def ask_create_file():
    global file_name
    response = messagebox.askyesno("Crear archivo", "¿Desea crear un nuevo archivo?")
    if response:
        file_name = tk.simpledialog.askstring("Nombre del archivo", "Ingrese el nombre del archivo:")
        if file_name:
            with open(file_name, 'w') as file:
                file.write("")  # Create an empty file
            messagebox.showinfo("Éxito", f"Archivo '{file_name}' creado exitosamente.")
            return True
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para el archivo.")
            return False
    else:
        messagebox.showinfo("Información", "No se creará un archivo nuevo. Se usará el gestor de tareas sin archivo.")
        return False
        

# Create the object
while True:
    if ask_create_file():
        try:
            task_manager = Task_Manager(file_name)
            break
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear el gestor de tareas: {e}")
            task_manager = Task_Manager()  # Default to a Task_Manager with no file
    else:
        task_manager = Task_Manager()  # Default to a Task_Manager with no file
        break

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

ask_create_file()

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