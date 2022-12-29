import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re
import vonage
import time
import shelve


def save_inputs():
        with shelve.open('input_fields') as db:
            db['message_entry'] = message_entry.get()
            db['key_entry'] = key_entry.get()
            db['secret_entry'] = secret_entry.get()
            db['msg_form_entry'] = msg_form_entry.get()

# Load input fields from a shelve file
def load_inputs():
        with shelve.open('input_fields') as db:
            # message_entry.insert(db.get('message_entry', ''))
            message_entry.insert(0, db['message_entry'])
            # key_entry.insert(db.get('key_entry', ''))
            key_entry.insert(0, db['key_entry'])
            # secret_entry.insert(db.get('secret_entry', ''))
            secret_entry.insert(0, db['secret_entry'])
            # msg_form_entry.insert(db.get('msg_form_entry', ''))
            msg_form_entry.insert(0, db['msg_form_entry'])

#function for submit button
def get_data():
    #label.config(

    
    num_list= receiver_entry.get()
    msg = message_entry.get()
    new_key = key_entry.get()
    new_secret = secret_entry.get()
    From = msg_form_entry.get()
    msg_delay = delay_entry.get()
    country_code = country_code_entry.get()
    print("list:",num_list," msg:",msg," key:",new_key," secret:",new_secret,"From:",From,"msg_delay:",msg_delay)

    file = open(num_list,"r")
    text = file.read()

    pattern = r"\d{3}\-\d{3}\-\d{4}"
    phone_numbers = re.findall(pattern , text)            
    def convert_phone_number(phone):
        result = re.sub(r'(?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'\1\2\3', phone)
        return result
    
    converted_num_list = []

    print(len(converted_num_list))
    
    
    for i in range(len(phone_numbers)):
        # print(convert_phone_number(phone_numbers[i]))
        print("phone numbers",phone_numbers[i])
        converted_num = convert_phone_number(phone_numbers[i])
        print("hey",converted_num)
        
        converted_num_list.append(converted_num)
        print("cnlist:",converted_num_list)
        print("type of cnlist:",type(converted_num_list))

    # label.config(text=converted_num_list)

    for item in converted_num_list:
        my_list.insert(END,item)


    print("========")
    #function for sending message
    def Text_SMS(num, msg):
        time.sleep(int(msg_delay))
        var1 = country_code
        num_new = "".join([var1, num])
        print("Numnew",num_new)
        print("========from textsms")
        responseData = sms.send_message({
            'from': From,
            'to': num_new,
            'text': msg,
            'type': "unicode"
        })

        
        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully to",num_new)
        else:
            error = responseData['messages'][0]['error-text']
            print(f"Message failed with error:",error)
            new_label.config(text = error)
    n3 = "/"
    n4= "Total contact no:"
    n2 = str(len(converted_num_list))
    n1 = n4+n2+n3+n2
    # total_num = "".join([var1, converted_num_list])
    total_num_label.config(text = n1 )
        # time.sleep(int(msg_delay))
    
    client = vonage.Client(key= new_key, secret= new_secret)
    sms = vonage.Sms(client)

    for i in range(len(converted_num_list)):
        # print("this is :", i ,"=",converted_num_list[i])
        Text_SMS(str(converted_num_list[i]), msg)

    # for i in range(len(phone_numbers)):
    #     print(phone_numbers[i])
    #     Text_SMS(str(phone_numbers[i]), msg)

    

def browsefunc():
      filename = askopenfilename(filetypes=(("All files", "*.*"),))
      receiver_entry.insert(END, filename)
      print(filename)

    


# def convert_phone_number(phone):
#   result = re.sub(r'(?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'\1\2\3', phone)
#   return result

# Create the main window
window = tk.Tk()
window.geometry("850x650")
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
submit_button = tk.Button(text="Submit",width=10, command=get_data)
submit_button.config(font=("Arial 12 bold" ),bg="#046204",fg="white")

# Create the browse button
# browse_button = tk.Button(window, text='Browse File', 
#    width=20,command = lambda:upload_file())



browse_button=tk.Button(window,text="Browse File",width=20,command=browsefunc)
browse_button.config(font=("Arial 12 bold" ),bg="#046204",fg="white")

xscrollbar = Scrollbar(window, orient=HORIZONTAL, width=20, activebackground='red', )
yscrollbar = Scrollbar(window, orient=VERTICAL, width=20, activebackground='green', )
xscrollbar.pack( side = BOTTOM, fill = X )
yscrollbar.pack( side = RIGHT, fill = Y )


#error label
new_label = Label(window,text="")
new_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white",wraplength=500)

#create output display
phone_label = Label(window,text ="Phone numbers")
phone_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")


#country code
country_code_label = tk.Label(text="Country code(of receiver):")
country_code_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")
country_code_entry = tk.Entry()
country_code_entry.config(font=("Arial 12 " ),bg="#525251",fg="white")


#total number of contacts
total_num_label = tk.Label(text="")
total_num_label.config(font=("Arial 12 bold" ),bg="#444544",fg="white")

#headline
header_label = tk.Label(text="Bulk SMS Sender")
header_label.config(font=("Batang 25 bold" ),bg="#444544",fg="#3ef49c")

# label=Label(window, text="" ,font=('Times 14'), width=20, height=15)
my_list = Listbox(window,xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set, width = 20 , height=15)
my_list.config(font=("Courier 13 " ),bg="#525251",fg="white")

xscrollbar.config( command = my_list.xview )
yscrollbar.config( command = my_list.yview )

#save button
save_button=tk.Button(window,text="Save ",width=10,command= save_inputs)
save_button.config(font=("Arial 12 bold" ),bg="#046204",fg="white")


#load button
load_button=tk.Button(window,text=" Load",width=10,command=load_inputs)
load_button.config(font=("Arial 12 bold" ),bg="#046204",fg="white")


# Place the widgets in the window
header_label.place(relx=0.35, rely=0.03, anchor = NW)
receiver_label.place(relx=0.1, rely=0.12, anchor = NW)
receiver_entry.place(relx=0.4, rely=0.12, anchor= NW)
browse_button.place(relx=0.7, rely=0.12, anchor = NW)
country_code_label.place(relx=0.1, rely=0.22, anchor = NW)
country_code_entry.place(relx = 0.4, rely = 0.22, anchor = NW)
message_label.place(relx=0.1, rely=0.32, anchor = NW)
message_entry.place(relx = 0.4, rely = 0.32, anchor = NW)
key_label.place(relx = 0.1, rely = 0.42, anchor = NW)
key_entry.place(relx = 0.4, rely = 0.42, anchor = NW)
secret_label.place(relx = 0.1, rely = 0.52, anchor = NW)
secret_entry.place(relx = 0.4, rely = 0.52, anchor = NW)
msg_form_label.place(relx = 0.1, rely = 0.62, anchor = NW)
msg_form_entry.place(relx = 0.4, rely = 0.62, anchor = NW)
delay_label.place(relx = 0.1, rely = 0.72, anchor = NW)
delay_entry.place(relx = 0.4, rely = 0.72, anchor = NW)
save_button.place(relx=0.1,rely=0.82)
load_button.place(relx=0.3,rely=0.82)
submit_button.place(relx = 0.5, rely = 0.82, anchor = NW)
total_num_label.place(relx = 0.7, rely = 0.82, anchor = NW)
phone_label.place(relx=0.75,rely=0.22)
# label.place(relx=0.7,rely=0.27)
my_list.place(relx=0.7,rely=0.3)
new_label.place(relx=0.1,rely=0.9)


fob=0
def upload_file():
    file = filedialog.askopenfilename()
    fob=open(file,'r')
    print(fob.name)
    receiver_label.config(textvariable=fob.name)



# Run the Tkinter event loop
window.mainloop()