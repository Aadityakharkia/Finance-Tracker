from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Finance Tracker")

        self.root.geometry("1000x700")
        self.root.minsize(1000, 700)
        self.root.maxsize(1000, 700)

        self.button_frame = Frame(self.root)
        self.button_frame.pack(fill=X, pady=10)

        # This will ensure the buttons are centered in the middle under one another
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Add buttons in the grid layout
        self.add_expenditure_button = Button(
            self.button_frame, text="Add Expenditure", command=self.add_expenditure
        )
        self.add_expenditure_button.grid(row=0, column=0, padx=10, pady=10)

        self.dashboard_button = Button(
            self.button_frame, text="Dashboard", command=self.show_dashboard
        )
        self.dashboard_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_statements_button = Button(
            self.button_frame, text="View Statements", command=self.view_statements
        )
        self.view_statements_button.grid(row=2, column=0, padx=10, pady=10)

        self.analytics_button = Button(
            self.button_frame, text="See Analytics", command=self.see_analytics
        )
        self.analytics_button.grid(row=3, column=0, padx=10, pady=10)

        # Create a Canvas widget
        self.canvas = Canvas(self.root, width=500, height=400, bg="lightblue")

        # Pack the Canvas widget into the main window
        self.canvas.pack(fill=BOTH, expand=True)

    def run(self):
        self.root.mainloop()


# Placeholder functions

    def add_expenditure(self):
        messagebox.showinfo("Add Expenditure", "This function will add an expenditure.")

    def show_dashboard(self):
        messagebox.showinfo("Dashboard", "This function will display the dashboard.")

    def view_statements(self):
        messagebox.showinfo("View Statements", "This function will display statements.")

    def see_analytics(self):
        messagebox.showinfo("See Analytics", "This function will display analytics.")
