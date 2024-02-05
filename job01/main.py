import tkinter as tk
from tkinter import messagebox
import mysql.connector
 
class Stock:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")
 
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FH202417m.",
            database="store"
        )
        self.cursor = self.connection.cursor()
 
        self.create_tables()
 
        self.create_widgets()
 
    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS category (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)
 
    
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                price INT,
                quantity INT,
                id_category INT,
                FOREIGN KEY (id_category) REFERENCES category(id)
            )
        """)
        self.connection.commit()
 
    def create_widgets(self):
        pass
 
    def run(self):
        self.root.mainloop()
 
if __name__ == "__main__":
    root = tk.Tk()
    app = Stock(root)
    app.run()
 
