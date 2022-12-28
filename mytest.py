import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

# Create the main window
window = tk.Tk()
window.geometry("500x600")
window.title("Bulk SMS")
window.configure(bg='#444544')

# Create the Receiver List field
receiver_label = tk.Label(text="Receiver List (CSV):")
receiver_label.config(font=("Arial 10 bold" ),bg="#444544",fg="white")
receiver_entry = tk.Entry(textvariable="")
receiver_entry.config(font=("Arial 10 " ),bg="#525251",fg="white")

# Create the Message field
message_label = tk.Label(text="Message:")
message_label.config(font=("Arial 10 bold" ),bg="#444544",fg="white")
message_entry = tk.Entry()
message_entry.config(font=("Arial 10 " ),bg="#525251",fg="white")

# Create the Key field
key_label = tk.Label(text="Key:")
key_label.config(font=("Arial 10 bold" ),bg="#444544",fg="white")
key_entry = tk.Entry()
key_entry.config(font=("Arial 10 " ),bg="#525251",fg="white")

# Create the Secret field
secret_label = tk.Label(text="Secret:")
secret_label.config(font=("Arial 10 bold" ),bg="#444544",fg="white")
secret_entry = tk.Entry()
secret_entry.config(font=("Arial 10 " ),bg="#525251",fg="white")

# Create the Msg Form field
msg_form_label = tk.Label(text="Msg Form:")
msg_form_label.config(font=("Arial 10 bold" ),bg="#444544",fg="white")
msg_form_entry = tk.Entry()
msg_form_entry.config(font=("Arial 10 " ),bg="#525251",fg="white")

# Create the Message Send Delay field
delay_label = tk.Label(text="Message Send Delay (s):")
delay_label.config(font=("Arial 10 bold" ),bg="#444544",fg="white")
delay_entry = tk.Entry()
delay_entry.config(font=("Arial 10 " ),bg="#525251",fg="white")

# Create the submit button
submit_button = tk.Button(text="Submit")
submit_button.config(font=("Arial 10 bold" ),bg="#046204",fg="white")

# Create the browse button
browse_button = tk.Button(window, text='Browse File', 
   width=20,command = lambda:upload_file())
browse_button.config(font=("Arial 10 bold" ),bg="#046204",fg="white")

# Place the widgets in the window
receiver_label.grid(row=0 , column=0 , padx=5 , pady=5)
receiver_entry.grid(row=0 , column=1, padx=5 , pady=5)
browse_button.grid(row=0 , column=2, padx=5 , pady=5)
message_label.grid(row=1 , column=0, padx=5 , pady=5)
message_entry.grid(row=1 , column=1, padx=5 , pady=5)
key_label.grid(row=2 , column=0, padx=5 , pady=5)
key_entry.grid(row=2 , column=1, padx=5 , pady=5)
secret_label.grid(row=3 , column=0, padx=5 , pady=5)
secret_entry.grid(row=3 , column=1, padx=5 , pady=5)
msg_form_label.grid(row=4 , column=0, padx=5 , pady=5)
msg_form_entry.grid(row=4 , column=1, padx=5 , pady=5)
delay_label.grid(row=5 , column=0, padx=5 , pady=5)
delay_entry.grid(row=5 , column=1, padx=5 , pady=5)
submit_button.grid(row=6,column=0, padx=5 , pady=5)
fob=0
def upload_file():
    file = filedialog.askopenfilename()
    fob=open(file,'r')
    print(fob.name)
    receiver_label.config(textvariable=fob.name)

# Run the Tkinter event loop
window.mainloop()