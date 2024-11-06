import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',          # Replace with your MySQL username
    password='G@nesh123',  # Replace with your MySQL password
    database='SM'         # Your database name
)
cursor = conn.cursor()

# Tkinter setup
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x400")

# Function to add a student to the database
def add_student():
    first_name = entry_fname.get()
    last_name = entry_lname.get()
    email = entry_email.get()
    phone = entry_phone.get()

    if first_name and last_name and email and phone:
        query = "INSERT INTO stud (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, email, phone))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        clear_fields()
        display_students()
    else:
        messagebox.showwarning("Input error", "All fields are required!")

# Function to delete a student from the database
def delete_student():
    student_id = entry_id.get()

    if student_id:
        query = "DELETE FROM stud WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        messagebox.showinfo("Success", "Student deleted successfully!")
        clear_fields()
        display_students()
    else:
        messagebox.showwarning("Input error", "Please enter the student ID to delete.")

# Function to update a student's information
def update_student():
    student_id = entry_id.get()
    first_name = entry_fname.get()
    last_name = entry_lname.get()
    email = entry_email.get()
    phone = entry_phone.get()

    if student_id and first_name and last_name and email and phone:
        query = "UPDATE stud SET first_name=%s, last_name=%s, email=%s, phone=%s WHERE id=%s"
        cursor.execute(query, (first_name, last_name, email, phone, student_id))
        conn.commit()
        messagebox.showinfo("Success", "Student updated successfully!")
        clear_fields()
        display_students()
    else:
        messagebox.showwarning("Input error", "All fields are required for update!")

# Function to clear input fields
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_fname.delete(0, tk.END)
    entry_lname.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# Function to display students in the listbox
def display_students():
    cursor.execute("SELECT * FROM stud")
    rows = cursor.fetchall()
    listbox_students.delete(0, tk.END)
    for row in rows:
        listbox_students.insert(tk.END, f"ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Phone: {row[4]}")

# Labels and Entry widgets for form
tk.Label(root, text="Student ID (for update/delete):").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="First Name:").pack()
entry_fname = tk.Entry(root)
entry_fname.pack()

tk.Label(root, text="Last Name:").pack()
entry_lname = tk.Entry(root)
entry_lname.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# Buttons for operations
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields).pack(pady=5)

# Listbox to display student records
listbox_students = tk.Listbox(root, width=80, height=10)
listbox_students.pack(pady=10)

# Display initial data
display_students()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when done
conn.close()
