import tkinter as tk
from tkinter import messagebox

contacts = {} #initialization as a dictionary

def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contacts[name] = number
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("!!!Error!!!", "Please,Atleast enter name and number!")

def update_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name in contacts:
        contacts[name] = number
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Entered details aint existing in this record.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Entered details aint existing in this record.")

def view_contacts():
    if contacts:
        contacts_str = "\n".join([f"{name}: {number}" for name, number in contacts.items()])
        messagebox.showinfo("Contacts", contacts_str)
    else:
        messagebox.showinfo("Contacts", "No contacts in the contact book yet.")

def main():
    root = tk.Tk()
    root.title("Contact Book")

    # Labels and Entry widgets for name and number
    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Number:").grid(row=1, column=0, padx=10, pady=5)
    global number_entry
    number_entry = tk.Entry(root)
    number_entry.grid(row=1, column=1, padx=10, pady=5)

    # Buttons for Add, Update, Delete, View Contacts, and Exit
    add_btn = tk.Button(root, text="Add", command=add_contact)
    add_btn.grid(row=2, column=0, padx=10, pady=5)

    update_btn = tk.Button(root, text="Update", command=update_contact)
    update_btn.grid(row=2, column=1, padx=10, pady=5)

    delete_btn = tk.Button(root, text="Delete", command=delete_contact)
    delete_btn.grid(row=2, column=2, padx=10, pady=5)

    view_btn = tk.Button(root, text="View Contacts", command=view_contacts)
    view_btn.grid(row=2, column=3, padx=10, pady=5)

    exit_btn = tk.Button(root, text="Exit", command=root.quit)
    exit_btn.grid(row=2, column=4, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
