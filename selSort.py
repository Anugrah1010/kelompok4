import tkinter as tk
from tkinter import ttk

class ElectronicItems:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ElectronicInventory:
    def __init__(self):
        self.items = [
            ElectronicItems("Laptop", 1000.0, 20),
            ElectronicItems("Phone", 500.0, 30),
            ElectronicItems("Tablet", 750.0, 10),
            ElectronicItems("TV", 1500.0, 5),
        ]
        
    def add_item(self, name, price, quantity):
        item = ElectronicItems(name, price, quantity)
        self.items.append(item)
        
    def delete_item(self, item):
        self.items.remove(item)
        
    def edit_item(self, item, name, price, quantity):
        item.name = name
        item.price = price
        item.quantity = quantity
        
    def sort_items(self, sort_type):
        for i in range(len(self.items)):
            min_index = i
            for j in range(i+1, len(self.items)):
                if sort_type == "name":
                    if self.items[j].name < self.items[min_index].name:
                        min_index = j
                elif sort_type == "price":
                    if self.items[j].price < self.items[min_index].price:
                        min_index = j
                elif sort_type == "quantity":
                    if self.items[j].quantity < self.items[min_index].quantity:
                        min_index = j

            self.items[i], self.items[min_index] = self.items[min_index], self.items[i]


class StoreGUI:
    def __init__(self, store):
        self.store = store
        self.root = tk.Tk()
        self.root.title("Electronic Inventory")
        
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("price", "quantity")
        self.tree.column("#0", width=150, minwidth=150)
        self.tree.column("price", width=150, minwidth=150)
        self.tree.column("quantity", width=150, minwidth=150)
        self.tree.heading("#0", text="Item Name")
        self.tree.heading("price", text="Price")
        self.tree.heading("quantity", text="Quantity")
        self.tree.pack(side="top", fill="both", expand=True)
        
        self.add_frame = ttk.Frame(self.root)
        self.add_frame.pack(side="top", fill="both", expand=True)
        self.add_name_label = ttk.Label(self.add_frame, text="Item Name:")
        self.add_name_label.grid(row=0, column=0)
        self.add_name_entry = ttk.Entry(self.add_frame)
        self.add_name_entry.grid(row=0, column=1)
        self.add_price_label = ttk.Label(self.add_frame, text="Price:")
        self.add_price_label.grid(row=1, column=0)
        self.add_price_entry = ttk.Entry(self.add_frame)
        self.add_price_entry.grid(row=1, column=1)
        self.add_quantity_label = ttk.Label(self.add_frame, text="Quantity:")
        self.add_quantity_label.grid(row=2, column=0)
        self.add_quantity_entry = ttk.Entry(self.add_frame)
        self.add_quantity_entry.grid(row=2, column=1)
        self.add_button = ttk.Button(self.add_frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2)    
        self.edit_frame = ttk.Frame(self.root)
        self.edit_frame.pack(side="top", fill="both", expand=True)
        self.edit_name_label = ttk.Label(self.edit_frame, text="Item Name:")
        self.edit_name_label.grid(row=0, column=0)
        self.edit_name_entry = ttk.Entry(self.edit_frame)
        self.edit_name_entry.grid(row=0, column=1)
        self.edit_price_label = ttk.Label(self.edit_frame, text="Price:")
        self.edit_price_label.grid(row=1, column=0)
        self.edit_price_entry = ttk.Entry(self.edit_frame)
        self.edit_price_entry.grid(row=1, column=1)
        self.edit_quantity_label = ttk.Label(self.edit_frame, text="Quantity:")
        self.edit_quantity_label.grid(row=2, column=0)
        self.edit_quantity_entry = ttk.Entry(self.edit_frame)
        self.edit_quantity_entry.grid(row=2, column=1)
        self.edit_button = ttk.Button(self.edit_frame, text="Edit Item", command=self.edit_item)
        self.edit_button.grid(row=3, column=0, columnspan=2)
        
        self.delete_button = ttk.Button(self.root, text="Delete Item", command=self.delete_item)
        self.delete_button.pack(side="bottom", fill="both", expand=True)
        
        self.sort_frame = ttk.Frame(self.root)
        self.sort_frame.pack(side="bottom", fill="both", expand=True)
        self.sort_label = ttk.Label(self.sort_frame, text="Sort by:")
        self.sort_label.grid(row=0, column=0)
        self.sort_option = tk.StringVar(value="name")
        self.sort_menu = ttk.OptionMenu(self.sort_frame, self.sort_option, "name", "name", "price", "quantity", command=self.sort_items)
        self.sort_menu.grid(row=0, column=1)
        

        self.update_tree()
    
    def add_item(self):
        name = self.add_name_entry.get()
        price = float(self.add_price_entry.get())
        quantity = int(self.add_quantity_entry.get())
        self.store.add_item(name, price, quantity)
        self.update_tree()
        self.add_name_entry.delete(0, "end")
        self.add_price_entry.delete(0, "end")
        self.add_quantity_entry.delete(0, "end")
    
    def delete_item(self):
        selected_item = self.tree.selection()[0]
        item_name = self.tree.item(selected_item)["text"]
        for item in self.store.items:
            if item.name == item_name:
                self.store.delete_item(item)
                break
        self.update_tree()
    
    def edit_item(self):
        selected_item = self.tree.selection()[0]
        item_name = self.tree.item(selected_item)["text"]
        for item in self.store.items:
            if item.name == item_name:
                name = self.edit_name_entry.get()
                price = float(self.edit_price_entry.get())
                quantity = int(self.edit_quantity_entry.get())
                self.store.edit_item(item, name, price, quantity)
                break
        self.update_tree()

    def sort_items(self, sort_type):
        self.store.sort_items(sort_type)
        self.update_tree()

    def update_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.store.items:
            self.tree.insert("", "end", text=item.name, values=(item.price, item.quantity))

store = ElectronicInventory()
gui = StoreGUI(store)
gui.root.mainloop()