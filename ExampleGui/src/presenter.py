import tkinter as tk


class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind buttons to methods
        self.view.todo_button.config(command=self.show_todo_page)
        self.view.temp_button.config(command=self.show_temp_converter_page)
        self.view.reset_button.config(command=self.reset_defaults)

        self.view.add_todo_button.config(command=self.add_todo)
        self.view.delete_todo_button.config(command=self.delete_todo)
        self.view.todo_home_button.config(command=self.show_home_page)

        self.view.convert_button.config(command=self.convert_temperature)
        self.view.temp_home_button.config(command=self.show_home_page)

    def start_application(self):
        self.view.root.mainloop()

    def show_home_page(self):
        self.view.show_frame("home")

    def show_todo_page(self):
        self.view.show_frame("todo")
        self.update_todo_listbox()

    def show_temp_converter_page(self):
        self.view.show_frame("temp_converter")
        self.update_temp_view()

    def reset_defaults(self):
        self.model.reset_defaults()
        self.update_todo_listbox()
        self.update_temp_view()

    def add_todo(self):
        todo_item = self.view.todo_entry.get()
        if todo_item:
            self.model.add_todo_item(todo_item)
            self.view.todo_entry.delete(0, tk.END)
            self.update_todo_listbox()

    def delete_todo(self):
        selected_item = self.view.todo_listbox.get(tk.ACTIVE)
        if selected_item:
            self.model.remove_todo_item(selected_item)
            self.update_todo_listbox()

    def update_todo_listbox(self):
        self.view.todo_listbox.delete(0, tk.END)
        for item in self.model.todos:
            self.view.todo_listbox.insert(tk.END, item)

    def convert_temperature(self):
        input_value = float(self.view.temp_entry.get())
        conversion_type = self.view.conversion_type.get()
        if conversion_type == "C_to_F":
            converted_value = (input_value * 9 / 5) + 32
        else:
            converted_value = (input_value - 32) * 5 / 9
        self.model.set_conversion(input_value, converted_value, conversion_type)
        self.view.result_label.config(text=f"Converted: {converted_value:.2f}")

    def update_temp_view(self):
        last_data = self.model.last_conversion
        self.view.temp_entry.delete(0, tk.END)
        if last_data["input_value"] is not None:
            self.view.temp_entry.insert(0, last_data["input_value"])
        self.view.result_label.config(
            text=f"Last Converted: {last_data['converted_value']:.2f}"
        )
        self.view.conversion_type.set(last_data["conversion_type"])
