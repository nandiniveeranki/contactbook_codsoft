import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(task, root):
        task.contacts = []
        task.root = root
        task.root.title("Contacts")

        task.menu = tk.Menu(task.root)
        task.root.config(menu=task.menu)
        task.file_menu = tk.Menu(task.menu, tearoff=False)
        task.menu.add_cascade(label="File", menu=task.file_menu)
        task.file_menu.add_command(label="View Contacts", command=task.view_contacts)
        task.file_menu.add_separator()
        task.file_menu.add_command(label="Exit", command=root.quit)

        task.add_frame = tk.LabelFrame(task.root, text="Add New Contact", padx=10, pady=10)
        task.add_frame.pack(padx=10, pady=10, fill="x")

        task.name_label = tk.Label(task.add_frame, text="Name")
        task.name_label.grid(row=0, column=0, sticky="e")
        task.name_entry = tk.Entry(task.add_frame)
        task.name_entry.grid(row=0, column=1, pady=2, padx=5, sticky="w")

        task.phone_label = tk.Label(task.add_frame, text="Phone Number")
        task.phone_label.grid(row=1, column=0, sticky="e")
        task.phone_entry = tk.Entry(task.add_frame)
        task.phone_entry.grid(row=1, column=1, pady=2, padx=5, sticky="w")

        task.add_button = tk.Button(task.add_frame, text="Add Contact", command=task.add_contact)
        task.add_button.grid(row=2, columnspan=2, pady=10)

        task.view_frame = tk.Frame(task.root)
        task.view_frame.pack(pady=10)

        task.contacts_listbox = tk.Listbox(task.view_frame, width=50)
        task.contacts_listbox.pack()

        task.contacts_listbox.bind("<Double-1>", task.select_contact)

        task.button_frame = tk.Frame(task.root)
        task.button_frame.pack(pady=10)

        
        task.delete_button = tk.Button(task.button_frame, text="Delete Contact", command=task.delete_contact)
        task.delete_button.grid(row=0, column=1, padx=5)
        task.update_button = tk.Button(task.button_frame, text="Update Contact", command=task.update_contact)
        task.update_button.grid(row=0, column=0, padx=5)

        task.search_frame = tk.LabelFrame(task.root, text="Search Contact", padx=10, pady=10)
        task.search_frame.pack(padx=10, pady=10, fill="x")

        task.search_label = tk.Label(task.search_frame, text="Search by Name or Phone Number")
        task.search_label.grid(row=0, column=0, sticky="e")
        task.search_entry = tk.Entry(task.search_frame)
        task.search_entry.grid(row=0, column=1, pady=2, padx=5, sticky="w")

        task.search_button = tk.Button(task.search_frame, text="Search", command=task.search_contact)
        task.search_button.grid(row=1, columnspan=2, pady=10)

    def add_contact(task):
        name = task.name_entry.get()
        phone = task.phone_entry.get()
        if name and phone:
            task.contacts.append({"name": name, "phone": phone})
            task.contacts_listbox.insert(tk.END, f"{name} - {phone}")
            task.name_entry.delete(0, tk.END)
            task.phone_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and Phone Number are required!")

    def view_contacts(task):
        task.contacts_listbox.delete(0, tk.END)
        for contact in task.contacts:
            task.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def select_contact(task, event):
        selected_index = task.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            contact = task.contacts[index]
            task.name_entry.delete(0, tk.END)
            task.name_entry.insert(tk.END, contact['name'])
            task.phone_entry.delete(0, tk.END)
            task.phone_entry.insert(tk.END, contact['number'])

    def update_contact(task):
        selected_index = task.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            name = task.name_entry.get()
            number = task.phone_entry.get()
            if name and number:
                task.contacts[index] = {"name": name, "number": number}
                task.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showwarning("Warning", "Name and Phone Number are required!")
        else:
            messagebox.showwarning("Warning", "No contact selected!")

    def search_contact(task):
        search_query = task.search_entry.get().lower()
        task.contacts_listbox.delete(0, tk.END)
        for contact in task.contacts:
            if search_query in contact['name'].lower() or search_query in contact['phone']:
                task.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def delete_contact(task):
        selected_index = task.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            del task.contacts[index]
            task.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No contact selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

