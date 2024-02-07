import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Modern color scheme
        self.root.configure(bg="#1E1E1E")
        self.label_color = "#FFFFFF"
        self.entry_bg = "#363636"
        self.button_bg = "#007ACC"

        # Fonts
        self.title_font = ("Helvetica", 16, "bold")
        self.label_font = ("Helvetica", 12)
        self.entry_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")

        self.contacts = []
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Contact Book", bg="#1E1E1E", fg=self.label_color, font=self.title_font)
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Labels
        labels_frame = tk.Frame(self.root, bg="#1E1E1E")
        labels_frame.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        tk.Label(labels_frame, text="Store Name:", bg="#1E1E1E", fg=self.label_color, font=self.label_font).grid(row=0, column=0, sticky="e")
        tk.Label(labels_frame, text="Phone:", bg="#1E1E1E", fg=self.label_color, font=self.label_font).grid(row=1, column=0, sticky="e")
        tk.Label(labels_frame, text="Email:", bg="#1E1E1E", fg=self.label_color, font=self.label_font).grid(row=2, column=0, sticky="e")
        tk.Label(labels_frame, text="Address:", bg="#1E1E1E", fg=self.label_color, font=self.label_font).grid(row=3, column=0, sticky="e")

        # Entry Widgets
        entries_frame = tk.Frame(self.root, bg="#1E1E1E")
        entries_frame.grid(row=1, column=1, padx=10, pady=5)

        self.name_entry = tk.Entry(entries_frame, bg=self.entry_bg, fg=self.label_color, font=self.entry_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_entry = tk.Entry(entries_frame, bg=self.entry_bg, fg=self.label_color, font=self.entry_font)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_entry = tk.Entry(entries_frame, bg=self.entry_bg, fg=self.label_color, font=self.entry_font)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_entry = tk.Entry(entries_frame, bg=self.entry_bg, fg=self.label_color, font=self.entry_font)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Listbox with Scrollbar
        listbox_frame = tk.Frame(self.root, bg="#1E1E1E")
        listbox_frame.grid(row=1, column=2, rowspan=8, padx=10, pady=5)

        self.contacts_listbox = tk.Listbox(listbox_frame, bg=self.entry_bg, fg=self.label_color, selectbackground=self.button_bg, selectforeground=self.label_color, font=self.entry_font)
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.Y)

        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contacts_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contacts_listbox.yview)

        # Buttons
        buttons_frame = tk.Frame(self.root, bg="#1E1E1E")
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(buttons_frame, text="Add Contact", command=self.add_contact, bg=self.button_bg, fg=self.label_color, font=self.button_font).grid(row=0, column=0, padx=10)
        tk.Button(buttons_frame, text="Show Contacts", command=self.show_contacts, bg=self.button_bg, fg=self.label_color, font=self.button_font).grid(row=0, column=1, padx=10)
        tk.Button(buttons_frame, text="Edit Contact", command=self.edit_contact, bg=self.button_bg, fg=self.label_color, font=self.button_font).grid(row=0, column=2, padx=10)
        tk.Button(buttons_frame, text="Delete Contact", command=self.delete_contact, bg=self.button_bg, fg=self.label_color, font=self.button_font).grid(row=0, column=3, padx=10)
        tk.Button(buttons_frame, text="Search Contacts", command=self.search_contacts, bg=self.button_bg, fg=self.label_color, font=self.button_font).grid(row=0, column=4, padx=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            contact = f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}"
            self.contacts.append(contact)
            self.update_contacts_listbox()
            messagebox.showinfo("Contact Added", "Contact added successfully!")
        else:
            messagebox.showwarning("Error", "Please enter all fields (Name, Phone, Email, Address).")

        # Clear entry fields after adding contact
        self.clear_entry_fields()

    def show_contacts(self):
        if self.contacts:
            contact_list = [f"{i + 1}. {contact}" for i, contact in enumerate(self.contacts)]
            self.contacts_listbox.delete(0, tk.END)
            for contact in contact_list:
                self.contacts_listbox.insert(tk.END, contact)
        else:
            messagebox.showinfo("Contacts", "No contacts to display.")

    def edit_contact(self):
        if not self.contacts:
            messagebox.showwarning("No Contacts", "There are no contacts to edit.")
            return

        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            # Parse existing contact information
            existing_contact = self.contacts[index].split(", ")
            existing_name = existing_contact[0].split(": ")[1]
            existing_phone = existing_contact[1].split(": ")[1]
            existing_email = existing_contact[2].split(": ")[1]
            existing_address = existing_contact[3].split(": ")[1]

            # Update entry fields with existing information
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)

            self.name_entry.insert(0, existing_name)
            self.phone_entry.insert(0, existing_phone)
            self.email_entry.insert(0, existing_email)
            self.address_entry.insert(0, existing_address)

            # Remove the edited contact from the list
            del self.contacts[index]
            self.update_contacts_listbox()

            messagebox.showinfo("Edit Contact", "You can now modify the contact information.")
        else:
            messagebox.showwarning("No Selection", "Please select a contact to edit.")

    def delete_contact(self):
        if not self.contacts:
            messagebox.showwarning("No Contacts", "There are no contacts to delete.")
            return

        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            # Remove the contact from the list
            del self.contacts[index]
            self.update_contacts_listbox()

            messagebox.showinfo("Delete Contact", "Contact deleted successfully!")
        else:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")

    def search_contacts(self):
        if not self.contacts:
            messagebox.showwarning("No Contacts", "There are no contacts to search.")
            return

        search_term = simpledialog.askstring("Search", "Enter the name or phone number to search:")
        if search_term is not None:
            search_results = []

            for contact in self.contacts:
                if search_term.lower() in contact.lower():
                    search_results.append(contact)

            if search_results:
                result_text = "\n".join(search_results)
                messagebox.showinfo("Search Results", result_text)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")

    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def update_contacts_listbox(self):
        self.show_contacts()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.geometry("1000x280")  # Set initial window size
    root.mainloop()
