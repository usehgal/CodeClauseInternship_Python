import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    long_url = entry_url.get()
    try:
        short_url = pyshorteners.Shortener().tinyurl.short(long_url)
        entry_shortened_url.delete(0, tk.END)
        entry_shortened_url.insert(0, short_url)
    except:
        messagebox.showerror("Error", "Invalid URL or connection error.")

def clear_entries():
    entry_url.delete(0, tk.END)
    entry_shortened_url.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")

# Heading
heading_label = tk.Label(root, text="URL Shortener", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=10)

# Create widgets
label_url = tk.Label(root, text="Paste your URL:")
entry_url = tk.Entry(root, width=40)
label_shortened_url = tk.Label(root, text="Shortened URL:")
entry_shortened_url = tk.Entry(root, width=40)
button_shorten = tk.Button(root, text="Shorten", command=shorten_url)
button_clear = tk.Button(root, text="Clear", command=clear_entries)

# Pack widgets
label_url.pack(pady=5)
entry_url.pack(pady=5)
label_shortened_url.pack(pady=5)
entry_shortened_url.pack(pady=5)
button_shorten.pack(pady=10)
button_clear.pack(pady=5)

# Start the main event loop
root.mainloop()
