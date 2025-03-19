import mysql.connector
from dotenv import load_dotenv
import os
import customtkinter as ctk
from tkinter import messagebox

# Load environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

# Connect to the database
mydb = mysql.connector.connect(
    user="root",
    password=PASSWORD,
    host="127.0.0.1",
    database="store",
)

if mydb is not None:
    print("CONNECTION... ESTABLISHED! WOUSSSSHHHHHHHHH!!!")

# Function to fetch products from the database
def fetch_products():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    cursor.close()
    return products

# Function to add a product to the database
def add_product(name, description, price, quantity, category):
    cursor = mydb.cursor()
    cursor.execute(
        "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
        (name, description, price, quantity, category),
    )
    mydb.commit()
    cursor.close()

# Function to delete a product from the database
def delete_product(product_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    mydb.commit()
    cursor.close()

# Function to modify a product in the database
def modify_product(product_id, name, description, price, quantity, category):
    cursor = mydb.cursor()
    cursor.execute(
        "UPDATE product SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = %s",
        (name, description, price, quantity, category, product_id),
    )
    mydb.commit()
    cursor.close()

# Function to handle adding a product
def handle_add_product():
    input_window("Add Product", add_product)

# Function to handle deleting a product
def handle_delete_product():
    input_window("Delete Product", delete_product, ["Product ID"])

# Function to handle modifying a product
def handle_modify_product():
    input_window("Modify Product", modify_product, ["Product ID", "Name", "Description", "Price", "Quantity", "Category"])

# Function to create an input window
def input_window(title, action, fields=["Name", "Description", "Price", "Quantity", "Category"]):
    def submit():
        values = [entry.get() for entry in entries]
        try:
            if action == delete_product:
                action(int(values[0]))
            else:
                action(*values)
            refresh_table()
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    window = ctk.CTkToplevel(root)
    window.title(title)
    entries = []
    for field in fields:
        label = ctk.CTkLabel(window, text=field)
        label.pack(pady=5)
        entry = ctk.CTkEntry(window)
        entry.pack(pady=5)
        entries.append(entry)
    submit_button = ctk.CTkButton(window, text="Submit", command=submit)
    submit_button.pack(pady=20)

# Function to refresh the table
def refresh_table():
    for widget in table_frame.winfo_children():
        widget.destroy()
    headers = ["ID", "Name", "Description", "Price", "Quantity", "Category"]
    for i, header in enumerate(headers):
        label = ctk.CTkLabel(table_frame, text=header, width=15)
        label.grid(row=0, column=i, padx=5, pady=5)
    products = fetch_products()
    for row_index, product in enumerate(products, start=1):
        for col_index, value in enumerate(product):
            label = ctk.CTkLabel(table_frame, text=value, width=15)
            label.grid(row=row_index, column=col_index, padx=5, pady=5)

# Initialize the main window
root = ctk.CTk()
root.title("Stock Management Dashboard")
root.geometry("800x600")

# Create a frame for the table
table_frame = ctk.CTkFrame(root)
table_frame.pack(pady=20)

# Create buttons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=20)

add_button = ctk.CTkButton(button_frame, text="Add Product", command=handle_add_product)
add_button.grid(row=0, column=0, padx=10)

delete_button = ctk.CTkButton(button_frame, text="Delete Product", command=handle_delete_product)
delete_button.grid(row=0, column=1, padx=10)

modify_button = ctk.CTkButton(button_frame, text="Modify Product", command=handle_modify_product)
modify_button.grid(row=0, column=2, padx=10)

# Refresh the table to display initial data
refresh_table()

# Start the main loop
root.mainloop()