import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from tkcalendar import Calendar
from SQL import SQLData  # Ensure this module is correctly imported

# Defining Class for the Transaction Page
class FinancialApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Initialize frames
        self.options_frame = DebitCreditFrame(self)
        self.accounts_frame = AccountsFrame(self)
        self.purpose_frame = PurposeFrame(self)
        self.amount_frame = AmountFrame(self)
        self.date_frame = DateFrame(self)
        self.submit_frame = SubmitFrame(self)

        # Arrange frames in a grid
        self.options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.accounts_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.purpose_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.amount_frame.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.date_frame.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.submit_frame.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Toggle date entry based on "Now" checkbox
        self.toggle_date_time_entry()

    def toggle_date_time_entry(self):
        if self.date_frame.now_var.get():
            self.date_frame.date_entry.config(state="disabled")
            self.date_frame.date_entry.delete(0, tk.END)
            self.date_frame.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            self.date_frame.date_entry.config(state="normal")

    def submit_amount(self):
        selected_option = self.options_frame.get_selected_option()
        entered_amount = self.amount_frame.amount_entry.get()
        selected_account = self.accounts_frame.selected_account.get()
        selected_purpose = self.purpose_frame.selected_purpose.get()
        entered_date = self.date_frame.date_entry.get()

        # Create an SQLData object with filename for writing (optional)
        sql_data = SQLData(filename="transactions.txt")  # Set filename here
        sql_data.data = (selected_option, entered_amount, selected_purpose, entered_date, selected_account)

        # Write data to file (optional)
        sql_data.write_to_file()  # Call the write_to_file method from SQLData

        # Show confirmation message
        messagebox.showinfo("Success", "Data submitted successfully!")
        print("Data submitted successfully!")

# Class for Credit or Debit Selection
class DebitCreditFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Transaction Type")
        self.debit_var = tk.BooleanVar()
        self.credit_var = tk.BooleanVar()

        self.debit_option = ttk.Checkbutton(self, text="Debit", variable=self.debit_var, onvalue=True,
                                            offvalue=False, command=self.update_options)
        self.debit_option.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        self.credit_option = ttk.Checkbutton(self, text="Credit", variable=self.credit_var, onvalue=True,
                                             offvalue=False, command=self.update_options)
        self.credit_option.grid(column=1, row=0, padx=10, pady=5, sticky="w")

    def update_options(self):
        if self.debit_var.get():
            self.credit_var.set(False)
        if self.credit_var.get():
            self.debit_var.set(False)

    def get_selected_option(self):
        return "Debit" if self.debit_var.get() else "Credit"

# Class to select Account
class AccountsFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Select Account")
        self.selected_account = tk.StringVar()

        self.accounts_options = ["Account 1", "Account 2", "Cash"]
        for idx, account in enumerate(self.accounts_options):
            button = ttk.Button(self, text=account, command=lambda acc=account: self.select_account(acc))
            button.grid(row=0, column=idx, padx=10, pady=5, sticky="w")

    def select_account(self, account):
        self.selected_account.set(account)
        print(f"Selected account: {account}")

# Class to select Purpose for the transaction
class PurposeFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Transaction Purpose")
        self.selected_purpose = tk.StringVar()

        self.purpose_options = ["Salary", "Home", "Food", "Sports", "Subscription", "Car"]
        for idx, purpose in enumerate(self.purpose_options):
            button = ttk.Button(self, text=purpose, command=lambda purp=purpose: self.select_purpose(purp))
            button.grid(row=0, column=idx, padx=10, pady=5, sticky="w")

    def select_purpose(self, purpose):
        self.selected_purpose.set(purpose)
        print(f"Selected purpose: {purpose}")

# Class to enter Amount
class AmountFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Enter Amount")
        self.amount_entry = ttk.Entry(self, width=20)
        self.amount_entry.grid(column=0, row=0, padx=10, pady=5, sticky="w")

# Class to ask for Date and Time
class DateFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Date and Time")
        self.now_var = tk.BooleanVar()
        self.now_checkbutton = ttk.Checkbutton(self, text="Now", variable=self.now_var,
                                               command=self.toggle_date_time_entry)
        self.now_checkbutton.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        self.date_entry = ttk.Entry(self, width=20)
        self.date_entry.grid(column=1, row=0, padx=10, pady=5, sticky="w")
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        self.pick_date_button = ttk.Button(self, text="Select Date and Time", command=self.pick_date_time)
        self.pick_date_button.grid(column=2, row=0, padx=10, pady=5, sticky="w")

    def toggle_date_time_entry(self):
        if self.now_var.get():
            self.date_entry.config(state="disabled")
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            self.date_entry.config(state="normal")

    def pick_date_time(self):
        def set_date_time():
            selected_date = cal.selection_get().strftime("%Y-%m-%d")
            selected_time = time_var.get()
            if selected_time:
                selected_time = datetime.strptime(selected_time, "%H:%M:%S").strftime("%H:%M:%S")
            else:
                selected_time = datetime.now().strftime("%H:%M:%S")
            self.date_entry.config(state="normal")
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, f"{selected_date} {selected_time}")
            top.destroy()

        top = tk.Toplevel()
        top.title("Select Date and Time")

        cal = Calendar(top, selectmode='day')
        cal.pack(pady=10)

        time_var = tk.StringVar()
        time_picker = ttk.Entry(top, textvariable=time_var)
        time_picker.pack(pady=10)

        confirm_button = ttk.Button(top, text="OK", command=set_date_time)
        confirm_button.pack(pady=10)

# Class to Submit
class SubmitFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="")
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_action)
        self.submit_button.grid(column=0, row=0, padx=10, pady=5, sticky="w")

    def submit_action(self):
        self.master.submit_amount()


if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialApp(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
