import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()

    if not name or not age or not email or not phone or not gender:
        messagebox.showerror("Error", "All fields are required")
        return

    messagebox.showinfo("Success", f"Name: {name}\nAge: {age}\nEmail: {email}\nPhone: {phone}\nGender: {gender}")

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Name label and entry
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Age label and entry
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Email label and entry
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=10)

# Phone label and entry
tk.Label(root, text="Phone").grid(row=3, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1, padx=10, pady=10)

# Gender label and radio buttons
tk.Label(root, text="Gender").grid(row=4, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, padx=10, pady=10)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=2, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
