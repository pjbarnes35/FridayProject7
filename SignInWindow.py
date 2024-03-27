from tkinter import Tk, Label, Entry, Button, messagebox
import sqlite3

# Database connection function
def connect_db():
  conn = sqlite3.connect("user_data.db")
  return conn, conn.cursor()

def validate_login(email, password):
  conn, c = connect_db()
  # Retrieve hashed password from database based on email
  c.execute("SELECT password_hash FROM users WHERE email = ?", (email,))
  data = c.fetchone()
  conn.close()

  # Check if email exists and compare hashed passwords (replace with your hashing library)
  if data:
    # Use your password hashing library (e.g., bcrypt) to compare hashed password with entered password
    return True  # Replace with actual comparison logic
  else:
    return False

def sign_in():
  email = email_entry.get()
  password = password_entry.get()

  if validate_login(email, password):
    messagebox.showinfo("Success", "Login successful!")
    # Close the window or open a new window for the logged-in user (replace with your logic)
  else:
    messagebox.showerror("Error", "Email or password incorrect")

# Create the main window
window = Tk()
window.title("Sign In")

# Create labels and entry fields
email_label = Label(window, text="Email:")
email_entry = Entry(window)

password_label = Label(window, text="Password:")
password_entry = Entry(window, show="*")  # Hide password characters

# Create the submit button
sign_in_button = Button(window, text="Sign In", command=sign_in)

# Arrange the elements on the window
email_label.pack()
email_entry.pack()

password_label.pack()
password_entry.pack()

sign_in_button.pack()

# Run the main event loop
window.mainloop()

