import tkinter as tk
import random
import string

def generate_password():

     
    length = int(lengthinentry.get())
    
    chars = ""
    if uppercase.get():
        chars += string.ascii_uppercase
    if lowercase.get():
        chars += string.ascii_lowercase
    if digits.get():
        chars += string.digits
    if specialchars.get():
        chars += string.punctuation
    
    

    password = "".join(random.choice(chars) for _ in range(length))
    result_entry.delete(0,"end")
    result_entry.insert(0, password)


# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#D3D3D3")


# Password length
tk.Label(root, text="Password Length:", font=("Arial", 14)).pack(pady=10)
lengthinentry = tk.Entry(root, font=("Arial", 14), width=5)
lengthinentry.pack()

# Options for password characters
uppercase = tk.BooleanVar()
lowercase = tk.BooleanVar()
digits = tk.BooleanVar()
specialchars = tk.BooleanVar()

options_frame = tk.Frame(root,bg="#D3D3D3")
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Uppercase", variable=uppercase, font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
tk.Checkbutton(options_frame, text="Lowercase", variable=lowercase, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)
tk.Checkbutton(options_frame, text="Digits", variable=digits, font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
tk.Checkbutton(options_frame, text="Special Characters", variable=specialchars, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Baskerville Old Face", 14), bg="#660000", fg="white", activebackground="white", activeforeground="black")
generate_btn.pack(pady=10)

# display
tk.Label(root, text="Generated Password:", font=("Arial", 14)).pack(pady=10)
result_entry = tk.Entry(root, font=("Arial", 14), width=30)
result_entry.pack()


root.mainloop()
