import os
import sys
import customtkinter as ctk
from PIL import Image

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the main function from your main app file
from main import main as main_app

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def startup():
    app = ctk.CTk()
    app.title("Easy Leaks")
    
    # Set icon
    icon_path = resource_path("components/icons/app_icon.ico")
    if os.path.exists(icon_path):
        try:
            app.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")
            # Fallback to using PhotoImage if iconbitmap fails
            try:
                icon = Image.open(icon_path)
                photo = ctk.CTkImage(light_image=icon, dark_image=icon, size=(32, 32))
                app.wm_iconphoto(True, photo._light_image)
            except Exception as e:
                print(f"Error setting icon with PhotoImage: {e}")
    else:
        print(f"Warning: Icon file not found at {icon_path}")

    # Close this startup window
    app.destroy()

    # Run the main application
    main_app()

if __name__ == "__main__":
    startup()