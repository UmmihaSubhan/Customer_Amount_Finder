# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 22:09:18 2025

@author: USubhan
"""

import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

# Global variable to hold the data
data = None

# Load the CSV file into a DataFrame
def load_data(file_path):
    global data
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully:")
        print(data.head())  # Print the first few rows of the DataFrame for debugging
        messagebox.showinfo("Success", "Data loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to open a file dialog and load the selected CSV file
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        load_data(file_path)

# Function to get customer amount by ID
def get_customer_amount():
    customer_id = entry.get()
    if customer_id.isdigit():
        customer_id = int(customer_id)
        print(f"Searching for Customer ID: {customer_id}")  # Debugging output
        result = data[data['customer_id'] == customer_id]
        if not result.empty:
            amount = result['customer_amount'].values[0]
            result_window = tk.Toplevel(app)
            result_window.title("Customer Amount")
            result_window.configure(bg="black")
            result_label = tk.Label(result_window, text=f"Customer ID: {customer_id}\nAmount: {amount}", bg="black", fg="yellow", font=("Arial", 14))
            result_label.pack(pady=20)
        else:
            messagebox.showwarning("Not Found", "Customer ID not found.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid customer ID.")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Customer Amount Finder")
app.geometry("400x300")  # Set the window size
app.configure(bg="black")  # Set background color to black

# Create a frame for better layout
frame = tk.Frame(app, bg="black")
frame.pack(pady=20)

# Create and place the widgets
label = tk.Label(frame, text="Enter Customer ID:", bg="black", fg="yellow", font=("Arial", 14))
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 14), width=20, bg="black", fg="yellow")
entry.grid(row=0, column=1, padx=10, pady=10)

upload_button = tk.Button(frame, text="Upload CSV", command=upload_file, bg="yellow", fg="black", font=("Arial", 12))
upload_button.grid(row=1, column=0, columnspan=2, pady=10)

button = tk.Button(frame, text="Get Customer Amount", command=get_customer_amount, bg="yellow", fg="black", font=("Arial", 12))
button.grid(row=2, column=0, columnspan=2, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear_entry, bg="yellow", fg="black", font=("Arial", 12))
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()

cd "Customer Amount Finder"
pyinstaller main.py
