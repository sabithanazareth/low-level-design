# Creating families of related or dependent objects without specifying their concrete classes. All about encapsulating the object creation process and ensuring that the created objects are compatible.
# Ex: 
# - It will support Email, SMS, and Push Notifications. Our service also integrates with two different imaginary notifications SAAS providers: FastNotif and SendBlue.
# - UI Factory with Button and CheckBox Interface and Light/Dark Factory classes, UIFactory with create_button and create_checkbox abc methods, Light/Dark concrete products amd calling LightButton() etc
# - Formatter, Exporter, Compressor for PDF vs HTML
# - Similarly, Button and Checkbox for Light vs Dark UI

# As the system evolves, you may need to switch between different families of objects without altering existing code.


from abc import ABC, abstractmethod

# ——— Abstract Products ———
class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        """Draw the button on screen."""
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        """Draw the checkbox on screen."""
        pass

# ——— Concrete Products: Light Theme ———
class LightButton(Button):
    def render(self) -> None:
        print("[LightButton] white background, dark text")

class LightCheckbox(Checkbox):
    def render(self) -> None:
        print("[LightCheckbox] white box, dark check")

# ——— Concrete Products: Dark Theme ———
class DarkButton(Button):
    def render(self) -> None:
        print("[DarkButton] dark background, light text")

class DarkCheckbox(Checkbox):
    def render(self) -> None:
        print("[DarkCheckbox] dark box, light check")

# ——— Abstract Factory ———
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# ——— Concrete Factories ———
class LightUIFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()

class DarkUIFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()
    
def create_ui_factory(theme: str = "Light") -> UIFactory:
    factories = {
        "Light": LightUIFactory,
        "Dark": DarkUIFactory,
    }
    return factories[theme]()

# ——— Client Code ———
if __name__ == "__main__":
    # create factories for both themes
    light_factory = create_ui_factory("Light")
    dark_factory  = create_ui_factory("Dark")

    # render Light theme UI
    print("Light theme:")
    btn_l = light_factory.create_button()
    cb_l  = light_factory.create_checkbox()
    btn_l.render()
    cb_l.render()

    # render Dark theme UI
    print("\nDark theme:")
    btn_d = dark_factory.create_button()
    cb_d  = dark_factory.create_checkbox()
    btn_d.render()
    cb_d.render()

# OR
# def render_ui(factory: UIFactory) -> None:
#     btn = factory.create_button()
#     cb  = factory.create_checkbox()
#     btn.render()
#     cb.render()

# if __name__ == "__main__":
#     print("Light theme:")
#     render_ui(LightUIFactory())

#     print("\nDark theme:")
#     render_ui(DarkUIFactory())