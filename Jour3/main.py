"""
Job first draft. Need to implement pygame to print everything with graphics.
Stock management, add, delete and modify product (stock, price...)
"""

import mysql.connector
from dotenv import load_dotenv
import os
import pygame
import sys

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    user="root",
    password=PASSWORD,
    host="127.0.0.1",
    database="store",
)

if mydb != None:
    print("CONNECTION... ESTABLISHED ! WOUSSSSHHHHHHHHH !!!")

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Stock Management Dashboard")

# Function to fetch products from the database
def fetch_products():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    cursor.close()
    return products

# Function to add a product to the database
def add_product(name, stock, price):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO product (name, stock, price) VALUES (%s, %s, %s)", (name, stock, price))
    mydb.commit()
    cursor.close()

# Function to delete a product from the database
def delete_product(product_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    mydb.commit()
    cursor.close()

# Function to modify a product in the database
def modify_product(product_id, name, stock, price):
    cursor = mydb.cursor()
    cursor.execute("UPDATE product SET name = %s, stock = %s, price = %s WHERE id = %s", (name, stock, price, product_id))
    mydb.commit()
    cursor.close()

# Function to draw a button
def draw_button(screen, text, x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    adjusted_color = tuple(max(0, min(255, c - 20)) for c in color)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, adjusted_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(text, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)

# Function to create text objects
def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()

# Function to truncate text
def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

# Function to handle adding a product
def handle_add_product():
    name = input("Enter product name: ")
    stock = int(input("Enter product stock: "))
    price = float(input("Enter product price: "))
    add_product(name, stock, price)

# Function to handle deleting a product
def handle_delete_product():
    product_id = int(input("Enter product ID to delete: "))
    delete_product(product_id)

# Function to handle modifying a product
def handle_modify_product():
    product_id = int(input("Enter product ID to modify: "))
    name = input("Enter new product name: ")
    stock = int(input("Enter new product stock: "))
    price = float(input("Enter new product price: "))
    modify_product(product_id, name, stock, price)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Fetch and display the products
    products = fetch_products()
    font = pygame.font.Font(None, 36)
    y = 50
    for product in products:
        product_text = f"ID: {product[0]}, Name: {truncate_text(product[1], 10)}, Stock: {product[2]}, Price: {product[3]}"
        text = font.render(product_text, True, (0, 0, 0))
        screen.blit(text, (50, y))
        y += 40

    # Draw buttons
    draw_button(screen, "Add Product", 50, 500, 150, 50, (0, 255, 0), action=handle_add_product)
    draw_button(screen, "Delete Product", 250, 500, 150, 50, (255, 0, 0), action=handle_delete_product)
    draw_button(screen, "Modify Product", 450, 500, 150, 50, (0, 0, 255), action=handle_modify_product)

    pygame.display.flip()

pygame.quit()
sys.exit()