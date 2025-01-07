from abc import ABC
from dataclasses import asdict, dataclass, field, fields, MISSING
from typing import Protocol


class AbstractModel(ABC):

    def _get_model_prefix(self) -> str:
        """Default method for getting model's unique prefix."""

        model_name = self.__class__.__name__.lower()
        if model_name.endswith("model"):
            return f"{model_name[:-5]}"

        err_msg = f"Incorrectly defined Model class name: {model_name}. Model class name must end with 'Model' as shown in example: 'UniqueNameModel'."

        raise NotImplementedError(err_msg)

    def _get_variables(self) -> dict:
        return asdict(self)

    def _reset_defaults(self):
        """Default method for models resetting all attributes default values."""
        for f in fields(self):
            default_value = (
                f.default_factory() if f.default_factory is not MISSING else f.default
            )
            setattr(self, f.name, default_value)


@dataclass
class TodoModel(AbstractModel):
    todo_list: list[str] = field(default_factory=list)

    def todo_add_item(self, item: str):
        self.todo_list.append(item)

    def todo_remove_item(self, item: str):
        if item in self.todo_list:
            self.todo_list.remove(item)

    def todo_get_variables(self) -> dict:
        return self._get_variables()

    def todo_reset_defaults(self) -> dict:
        self._reset_defaults()


@dataclass
class TempModel(AbstractModel):
    input_temp: float = 0.0
    converted_temp: float = 32.0
    convert_type: str = "C_to_F"

    def temp_set_conversion(
        self, input_temp: float, converted_temp: float, convert_type: str
    ):

        self.input_temp = input_temp
        self.converted_temp = converted_temp
        self.convert_type = convert_type

    def temp_get_variables(self) -> dict:
        return self._get_variables()

    def temp_reset_defaults(self) -> dict:
        self._reset_defaults()


class Model:
    model_dict: dict[str, AbstractModel]

    def __init__(self, *models: AbstractModel):

        if not models:
            raise NotImplementedError(
                f"Must provide model object(s) to be used within main Model class."
            )

        self.model_dict = {model._get_model_prefix(): model for model in models}

    def get_model(self, model_prefix: str) -> AbstractModel:

        model = self.model_dict.get(model_prefix, None)
        if not model:
            raise AttributeError(
                f"Model Class with prefix '{model_prefix}' does not exist. Please define class as: '{model_prefix.title()}Model' to use '{model_prefix}_' based methods."
            )
        return model

    def models_get_variables(self) -> dict:

        return {
            model_prefix: model._get_variables()
            for model_prefix, model in self.model_dict.items()
        }

    def reset_defaults(self):
        for model in self.model_dict.values():
            model._reset_defaults()

    def __getattr__(self, name: str):
        # Delegate method calls to the appropriate model

        if name.startswith("_"):
            raise AttributeError(
                f"Cannot access private or protected method '{name}' directly."
            )

        # Get model specific method
        model_prefix = name.split("_")[0]
        model = self.model_dict.get(model_prefix, None)

        if not model:
            raise AttributeError(
                f"Model Class with prefix '{model_prefix}' does not exist. Please define class as: '{model_prefix.title()}Model' to use '{model_prefix}_' based methods."
            )

        # Return model's method if exists
        attr = getattr(model, name, None)
        if not attr:
            raise AttributeError(
                f"'{model.__class__.__name__}' object has no attribute '{name}'"
            )

        return attr


class MainModel(Protocol):
    # Default methods
    def get_model(self, model_prefix: str) -> AbstractModel: ...
    def models_get_variables(self, model_prefix: str) -> dict: ...
    def reset_defaults(self) -> None: ...

    # To-do model methods
    def todo_add_item(self, item: str) -> None: ...
    def todo_remove_item(self, item: str) -> None: ...
    def todo_get_variables(self) -> dict[str, float | str]: ...
    def todo_reset_defaults(self) -> None: ...

    # Temp model methods
    def temp_set_conversion(
        self, input_temp: float, converted_temp: float, convert_type: str
    ) -> None: ...
    def temp_get_variables(self) -> dict[str, float | str]: ...
    def temp_reset_defaults(self) -> None: ...


def main():

    todo_model = TodoModel()
    temp_model = TempModel()
    model: MainModel = Model(todo_model, temp_model)


if __name__ == "__main__":
    main()
