import tkinter as tk
from tkinter import messagebox, ttk
from Transaction_Window import FinancialApp  # Ensure this module is correctly imported

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Finance Tracker Dashboard")

        self.root.geometry("1250x750")
        self.root.resizable(False, False)

        # Style configuration
        style = ttk.Style(self.root)
        style.configure('TButton', font=('Arial', 12), padding=10)

        # Menu buttons
        self.create_menu_buttons()

        # Canvas for dynamic content
        self.canvas = tk.Canvas(self.root, bg="lightblue")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status_bar = ttk.Label(self.root, text="Welcome to Finance Tracker", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu_buttons(self):
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y, pady=10, padx=10)

        buttons = [
            ("Add Expenditure", self.add_expenditure),
            ("Dashboard", self.show_dashboard),
            ("View Statements", self.view_statements),
            ("See Analytics", self.see_analytics)
        ]

        for i, (text, command) in enumerate(buttons):
            button = ttk.Button(self.button_frame, text=text, command=command)
            button.grid(row=i, column=0, pady=10)

    def run(self):
        self.root.mainloop()

    def add_expenditure(self):
        self.clear_canvas()
        # Assuming FinancialApp is a tkinter frame-like class
        app_frame = FinancialApp(self.canvas)
        app_frame.pack(fill=tk.BOTH, expand=True)
        self.update_status("Add Expenditure window opened.")

    def show_dashboard(self):
        self.clear_canvas()
        # Placeholder: Populate the canvas with dashboard elements
        tk.Label(self.canvas, text="Dashboard Content Here", font=("Arial", 24)).pack(pady=20)
        self.update_status("Dashboard displayed.")

    def view_statements(self):
        self.clear_canvas()
        # Placeholder: Populate the canvas with statements
        tk.Label(self.canvas, text="Statements Content Here", font=("Arial", 24)).pack(pady=20)
        self.update_status("Statements displayed.")

    def see_analytics(self):
        self.clear_canvas()
        # Placeholder: Populate the canvas with analytics
        tk.Label(self.canvas, text="Analytics Content Here", font=("Arial", 24)).pack(pady=20)
        self.update_status("Analytics displayed.")

    def clear_canvas(self):
        for widget in self.canvas.winfo_children():
            widget.destroy()

    def update_status(self, message):
        self.status_bar.config(text=message)


if __name__ == "__main__":
    gui = GUI()
    gui.run()
