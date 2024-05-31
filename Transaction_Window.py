import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar
from SQL-Data import SQL

# Defining Class for the Trasaction Page
class FinancialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transaction Window")
        self.root.minsize(1200,600)
        self.root.maxsize(1200,600)

        self.options_frame = DebitCreditFrame(root, self)
        self.accounts_frame = AccountsFrame(root, self)
        self.purpose_frame = PurposeFrame(root, self)
        self.amount_frame = AmountFrame(root)
        self.date_frame = DateFrame(root, self)
        self.submit_frame = SubmitFrame(root, self)

        self.toggle_date_time_entry()

    def toggle_date_time_entry(self):
        if self.date_frame.now_var.get():
            self.date_frame.date_entry.config(state="disabled")
            self.date_frame.date_entry.delete(0, tk.END)
            self.date_frame.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            self.date_frame.date_entry.config(state="normal")

    def submit_amount(self):
        selected_option = self.options_frame.debit_var.get() if self.options_frame.debit_var.get() else self.options_frame.credit_var.get()
        entered_amount = self.amount_frame.amount_entry.get()
        selected_account = self.accounts_frame.account_var.get()
        selected_purpose = self.purpose_frame.purpose_var.get()
        entered_date = self.date_frame.date_entry.get()
        return selected_option, entered_amount, selected_purpose, entered_date, selected_account


# Class for Credit or Debit Selection
class DebitCreditFrame:
    def __init__(self, root, app):
        self.app = app
        self.frame = ttk.LabelFrame(root, text="Transaction Type")
        self.frame.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        self.debit_var = tk.BooleanVar()
        self.credit_var = tk.BooleanVar()

        self.debit_option = ttk.Checkbutton(self.frame, text="Debit", variable=self.debit_var, onvalue=True,
                                            offvalue=False, command=self.update_options,)
        self.debit_option.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        self.credit_option = ttk.Checkbutton(self.frame, text="Credit", variable=self.credit_var, onvalue=True,
                                             offvalue=False, command=self.update_options)
        self.credit_option.grid(column=1, row=0, padx=10, pady=5, sticky="w")

    def update_options(self):
        if self.debit_var.get():
            self.credit_var.set(False)
        if self.credit_var.get():
            self.debit_var.set(False)

# Class to select Account
class AccountsFrame:
    def __init__(self, root, app):
        self.app = app
        self.frame = ttk.LabelFrame(root, text="Select Account")
        self.frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        self.accounts_options = ["Account 1", "Account 2", "Cash"]
        self.account_var = tk.StringVar()
        self.account_var.set(self.accounts_options[0])

        self.account_dropdown = ttk.OptionMenu(self.frame, self.account_var, *self.accounts_options)
        self.account_dropdown.grid(column=0, row=0, padx=10, pady=5, sticky="w")

# Class to select Purpose for the transaction
class PurposeFrame:
    def __init__(self, root, app):
        self.app = app
        self.frame = ttk.LabelFrame(root, text="Transaction Purpose")
        self.frame.grid(column=0, row=2, padx=10, pady=10, sticky="w")

        self.purpose_options = ["Salary", "Home", "Food", "Sports", "Subscription", "Car"]
        self.purpose_var = tk.StringVar()
        self.purpose_var.set(self.purpose_options[0])

        self.purpose_dropdown = ttk.OptionMenu(self.frame, self.purpose_var, *self.purpose_options)
        self.purpose_dropdown.grid(column=0, row=0, padx=10, pady=5, sticky="w")

# Class to enter Amount
class AmountFrame:
    def __init__(self, root):
        self.frame = ttk.LabelFrame(root, text="Enter Amount")
        self.frame.grid(column=0, row=3, padx=10, pady=10, sticky="w")

        self.amount_entry = ttk.Entry(self.frame, width=10)
        self.amount_entry.grid(column=0, row=0, padx=10, pady=5, sticky="w")

# Class to ask for Date and Time
class DateFrame:
    def __init__(self, root, app):
        self.app = app
        self.frame = ttk.LabelFrame(root, text="Date and Time")
        self.frame.grid(column=0, row=4, padx=10, pady=10, sticky="w")

        self.now_var = tk.BooleanVar()
        self.now_checkbutton = ttk.Checkbutton(self.frame, text="Now", variable=self.now_var,
                                               command=self.app.toggle_date_time_entry)
        self.now_checkbutton.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        self.date_entry = ttk.Entry(self.frame, width=20)
        self.date_entry.grid(column=1, row=0, padx=10, pady=5, sticky="w")
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        self.pick_date_button = ttk.Button(self.frame, text="Select Date and Time", command=self.pick_date_time)
        self.pick_date_button.grid(column=2, row=0, padx=10, pady=5, sticky="w")

    def pick_date_time(self):
        def set_date_time():
            selected_date = cal.selection_get().strftime("%Y-%m-%d")
            selected_time = time_var.get()
            if selected_time:
                selected_time = selected_time.strftime("%H:%M:%S")
            else:
                selected_time = datetime.now().strftime("%H:%M:%S")
            self.date_entry.config(state="normal")
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, f"{selected_date} {selected_time}")
            top.destroy()

        top = tk.Toplevel()
        top.title("Select Date and Time")

        cal = Calendar(top, selectmode='day')
        cal.pack()

        time_var = tk.StringVar()
        time_picker = ttk.Entry(top, textvariable=time_var)
        time_picker.pack()

        confirm_button = ttk.Button(top, text="OK", command=set_date_time)
        confirm_button.pack()

# Class to Submit
class SubmitFrame:
    def __init__(self, root, app):
        self.app = app
        self.frame = ttk.LabelFrame(root, text="")
        self.frame.grid(column=0, row=5, padx=10, pady=10, sticky="w")

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.submit_action)
        self.submit_button.grid(column=0, row=0, padx=10, pady=5, sticky="w")

    def submit_action(self):
        result = self.app.submit_amount()
        print("Returned:", result)

