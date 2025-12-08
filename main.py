import sys
from PySide6.QtWidgets import QApplication
from widget import Widget  # Import your main Widget class


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create an instance of your main window (Widget)
    window = Widget()
    window.show()  # Show the main window

    # Execute the application
    sys.exit(app.exec())
