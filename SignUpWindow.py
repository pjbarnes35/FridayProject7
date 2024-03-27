from tkinter import Tk, Label, Entry, Button, messagebox

# Database connection (replace with your actual connection logic)
def connect_db():
  # Your code to connect to the database (e.g., using sqlite3)
  pass

def validate_email(email):
  return "@" in email and "." in email

def validate_password(password1, password2):
  return password1 == password2

def sign_up():
  email = email_entry.get()
  password1 = password_entry1.get()
  password2 = password_entry2.get()

  if not validate_email(email):
    messagebox.showerror("Error", "Invalid email format")
    return

  if not validate_password(password1, password2):
    messagebox.showerror("Error", "Passwords do not match")
    return

  # Connect to database and store user information (replace with actual logic)
  connect_db()
  # Your code to save email and hashed password to the database

  messagebox.showinfo("Success", "Account created successfully!")
  window.destroy()  # Close the sign-up window

# Create the main window
window = Tk()
window.title("Sign Up")

# Create labels and entry fields
email_label = Label(window, text="Email:")
email_entry = Entry(window)

password_label1 = Label(window, text="Password:")
password_entry1 = Entry(window, show="*")  # Hide password characters

password_label2 = Label(window, text="Re-enter Password:")
password_entry2 = Entry(window, show="*")  # Hide password characters

# Create the submit button
submit_button = Button(window, text="Sign Up", command=sign_up)

# Arrange the elements on the window
email_label.pack()
email_entry.pack()

password_label1.pack()
password_entry1.pack()

password_label2.pack()
password_entry2.pack()

submit_button.pack()

# Run the main event loop
window.mainloop()
