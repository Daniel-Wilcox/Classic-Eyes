class Model:
    def __init__(self):
        self.todos = []
        self.last_conversion = {
            "input_value": 0.0,
            "converted_value": 32.0,
            "conversion_type": "C_to_F",
        }

    def add_todo_item(self, item):
        self.todos.append(item)

    def remove_todo_item(self, item):
        if item in self.todos:
            self.todos.remove(item)

    def reset_defaults(self):
        self.todos = []
        self.last_conversion = {
            "input_value": 0.0,
            "converted_value": 32.0,
            "conversion_type": "C_to_F",
        }

    def set_conversion(self, input_value, converted_value, conversion_type):
        self.last_conversion = {
            "input_value": input_value,
            "converted_value": converted_value,
            "conversion_type": conversion_type,
        }
