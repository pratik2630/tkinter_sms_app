import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


#function for submit button
def get_data():
    #label.config(
    num_list= receiver_entry.get()
    msg = message_entry.get()
    key = key_entry.get()
    secret = secret_entry.get()
    From = msg_form_entry.get()
    msg_delay = delay_entry.get()
    print("list:",num_list," msg:",msg," key:",key," secret:",secret,"From:",From,"msg_delay:",msg_delay)


# Create the main window
window = tk.Tk()
window.geometry("800x600")
window.title("Bulk SMS")
window.configure(bg='#444544')

# Create the Receiver List field
receiver_label = tk.Label(text="Receiver List (CSV):")
receiver_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
receiver_entry = tk.Entry(textvariable="")
receiver_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")

# Create the Message field
message_label = tk.Label(text="Message:")
message_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
message_entry = tk.Entry()
message_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")

# Create the Key field
key_label = tk.Label(text="Key:")
key_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
key_entry = tk.Entry()
key_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")

# Create the Secret field
secret_label = tk.Label(text="Secret:")
secret_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
secret_entry = tk.Entry()
secret_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")

# Create the Msg Form field
msg_form_label = tk.Label(text="Msg Form:")
msg_form_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
msg_form_entry = tk.Entry()
msg_form_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")

# Create the Message Send Delay field
delay_label = tk.Label(text="Message Send Delay (s):")

delay_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
delay_entry = tk.Entry()
delay_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")

# Create the submit button
submit_button = tk.Button(text="Submit", command=get_data)
submit_button.config(font=("Arial 12 bold" ),bg="#046204",fg="white")

# Create the browse button
# browse_button = tk.Button(window, text='Browse File', 
#    width=20,command = lambda:upload_file())

def browsefunc():
      filename = askopenfilename(filetypes=(("All files", "*.*"),))
      receiver_entry.insert(END, filename)
      print(filename)

browse_button=tk.Button(window,text="Browse File",width=20,command=browsefunc)
browse_button.config(font=("Arial 12 bold" ),bg="#046204",fg="white")



#create output display
phone_label = Label(window,text ="Phone numbers")
phone_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
label=Label(window, text="" ,font=('Times 14'), width=20, height=15)




# Place the widgets in the window
receiver_label.place(relx=0.1, rely=0.1, anchor = NW)
receiver_entry.place(relx=0.4, rely=0.1, anchor= NW)
browse_button.place(relx=0.7, rely=0.1, anchor = NW)
message_label.place(relx=0.1, rely=0.2, anchor = NW)
message_entry.place(relx = 0.4, rely = 0.2, anchor = NW)
key_label.place(relx = 0.1, rely = 0.3, anchor = NW)
key_entry.place(relx = 0.4, rely = 0.3, anchor = NW)
secret_label.place(relx = 0.1, rely = 0.4, anchor = NW)
secret_entry.place(relx = 0.4, rely = 0.4, anchor = NW)
msg_form_label.place(relx = 0.1, rely = 0.5, anchor = NW)
msg_form_entry.place(relx = 0.4, rely = 0.5, anchor = NW)
delay_label.place(relx = 0.1, rely = 0.6, anchor = NW)
delay_entry.place(relx = 0.4, rely = 0.6, anchor = NW)
submit_button.place(relx = 0.5, rely = 0.7, anchor = NW)
phone_label.place(relx=0.75,rely=0.2)
label.place(relx=0.7,rely=0.27)

fob=0
def upload_file():
    file = filedialog.askopenfilename()
    fob=open(file,'r')
    print(fob.name)
    receiver_label.config(textvariable=fob.name)

# Run the Tkinter event loop
window.mainloop()