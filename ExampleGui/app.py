from src.model import Model
from src.view import ApplicationView
from src.presenter import Presenter

if __name__ == "__main__":
    model = Model()
    view = ApplicationView()
    presenter = Presenter(model, view)

    presenter.start_application()
    # view.root.mainloop()
