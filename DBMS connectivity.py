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
root.geometry("600x500")
root.configure(bg="#f0f0f0")

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

# Label Frame for form
form_frame = tk.Frame(root, bg="#e1e8f2", bd=5, relief=tk.GROOVE)
form_frame.pack(padx=10, pady=10, fill=tk.X)

# Labels and Entry widgets for form
tk.Label(form_frame, text="Student ID (for update/delete):", bg="#e1e8f2", font=("Arial", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_id = tk.Entry(form_frame, width=30, font=("Arial", 10))
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="First Name:", bg="#e1e8f2", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_fname = tk.Entry(form_frame, width=30, font=("Arial", 10))
entry_fname.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Last Name:", bg="#e1e8f2", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_lname = tk.Entry(form_frame, width=30, font=("Arial", 10))
entry_lname.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Email:", bg="#e1e8f2", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(form_frame, width=30, font=("Arial", 10))
entry_email.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Phone:", bg="#e1e8f2", font=("Arial", 10)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_phone = tk.Entry(form_frame, width=30, font=("Arial", 10))
entry_phone.grid(row=4, column=1, padx=5, pady=5)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(padx=10, pady=10)

# Buttons for operations
tk.Button(button_frame, text="Add Student", command=add_student, width=15, font=("Arial", 10), bg="#4caf50", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Update Student", command=update_student, width=15, font=("Arial", 10), bg="#2196f3", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Delete Student", command=delete_student, width=15, font=("Arial", 10), bg="#f44336", fg="white").grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Clear Fields", command=clear_fields, width=15, font=("Arial", 10), bg="#9e9e9e", fg="white").grid(row=0, column=3, padx=5, pady=5)

# Listbox to display student records
listbox_frame = tk.Frame(root, bg="#e1e8f2", bd=5, relief=tk.GROOVE)
listbox_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(listbox_frame, text="Student Records:", bg="#e1e8f2", font=("Arial", 10, "bold")).pack(anchor="w", padx=5, pady=5)
listbox_students = tk.Listbox(listbox_frame, width=80, height=10, font=("Arial", 10), bd=2, relief=tk.SUNKEN)
listbox_students.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Display initial data
display_students()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when done
conn.close()
