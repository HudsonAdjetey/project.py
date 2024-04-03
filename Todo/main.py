import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_frame = tk.Frame(master)
        self.tasks_frame.pack(pady=10)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(master, text="Delete Selected", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.render_tasks()

    def render_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks):
            task_label = tk.Label(self.tasks_frame, text=task)
            task_label.grid(row=index, column=0, sticky="w")
            task_checkbox = tk.Checkbutton(self.tasks_frame, command=lambda index=index: self.toggle_done(index))
            task_checkbox.grid(row=index, column=1)

    def toggle_done(self, index):
        # Toggle the state of the task at the given index
        self.tasks[index] = f"[Done] {self.tasks[index]}" if "[Done]" not in self.tasks[index] else self.tasks[index].replace("[Done] ", "")
        self.render_tasks()

    def delete_task(self):
        # Delete the selected tasks
        new_tasks = [task for i, task in enumerate(self.tasks) if i not in self.get_selected_indexes()]
        self.tasks = new_tasks
        self.render_tasks()

    def clear_tasks(self):
        # Clear all tasks
        self.tasks = []
        self.render_tasks()

    def get_selected_indexes(self):
        # Get the indexes of selected tasks
        indexes = []
        for index, task in enumerate(self.tasks):
            if "[Done]" in task:
                indexes.append(index)
        return indexes

    def load_tasks(self):
        # Load tasks from a file or database
        pass

    def save_tasks(self):
        # Save tasks to a file or database
        pass

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
