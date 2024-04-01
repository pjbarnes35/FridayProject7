# FridayProject7
Template and working sign up and in

# User Authentication System

This project implements a basic user authentication system using Python, SQLite, and Tkinter for the GUI. The system allows users to sign up with a valid email and password, and then sign in with their credentials. Passwords are hashed using SHA-256 before storing them in the database for security.

## Project Structure

- **`SignUpWindow.py` and 'SignInWindow.py'**: Contains the main code for the sign-up and sign-in functionalities using Tkinter for the GUI.
- **`DatabaseCreate.py`**: Python script to create the SQLite database (`user_data.db`) and the `users` table to store user information.
- **`README.md`**: This file, providing an overview of the project.

## Requirements

- Python 3.x
- Tkinter (standard library)
- SQLite3 (standard library)

## Installation and Setup

1. Clone or download the project repository to your local machine and GITHUB.

## Database Creation

Run the `DatabaseCreate.py` script to create the database (`user_data.db`) and the `users` table:

```bash
python DatabaseCreate.py
```

## Running the Application

Run the ``SignUpWindow.py` and 'SignInWindow.py'` script to launch the application:

The application window will open, allowing users to sign up and sign in.

## Additional Notes

- Ensure that you have proper error handling and security measures (such as password hashing) in a real-world application.
- This project uses a basic hashing method (SHA-256) for demonstration purposes; consider using more secure hashing libraries (e.g., bcrypt) in production.

---