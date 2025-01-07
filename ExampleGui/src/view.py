import tkinter as tk


class ApplicationView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Multipage Application")

        self.frames = {}

        # Create all the frames
        self.create_home_view()
        self.create_todo_view()
        self.create_temp_converter_view()

        # Show the home frame by default
        self.show_frame("home")

    def create_home_view(self):
        home_frame = tk.Frame(self.root)
        home_label = tk.Label(home_frame, text="Home Page")
        home_label.pack()
        self.todo_button = tk.Button(home_frame, text="Go to Todo List")
        self.todo_button.pack()
        self.temp_button = tk.Button(home_frame, text="Go to Temp Converter")
        self.temp_button.pack()
        self.reset_button = tk.Button(home_frame, text="Reset Defaults")
        self.reset_button.pack()

        self.frames["home"] = home_frame

    def create_todo_view(self):
        todo_frame = tk.Frame(self.root)
        self.todo_entry = tk.Entry(todo_frame)
        self.todo_entry.pack()
        self.add_todo_button = tk.Button(todo_frame, text="Add Todo")
        self.add_todo_button.pack()
        self.todo_listbox = tk.Listbox(todo_frame)
        self.todo_listbox.pack()
        self.delete_todo_button = tk.Button(todo_frame, text="Delete Selected")
        self.delete_todo_button.pack()
        self.todo_home_button = tk.Button(todo_frame, text="Go Home")
        self.todo_home_button.pack()

        self.frames["todo"] = todo_frame

    def create_temp_converter_view(self):
        temp_frame = tk.Frame(self.root)
        self.temp_entry = tk.Entry(temp_frame)
        self.temp_entry.pack()
        self.conversion_type = tk.StringVar(value="C_to_F")
        self.c_to_f_button = tk.Radiobutton(
            temp_frame, text="C to F", variable=self.conversion_type, value="C_to_F"
        )
        self.c_to_f_button.pack()
        self.f_to_c_button = tk.Radiobutton(
            temp_frame, text="F to C", variable=self.conversion_type, value="F_to_C"
        )
        self.f_to_c_button.pack()
        self.convert_button = tk.Button(temp_frame, text="Convert")
        self.convert_button.pack()
        self.result_label = tk.Label(temp_frame, text="")
        self.result_label.pack()
        self.temp_home_button = tk.Button(temp_frame, text="Go Home")
        self.temp_home_button.pack()

        self.frames["temp_converter"] = temp_frame

    def show_frame(self, frame_name):
        """Hide all frames and show the selected frame."""
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)
