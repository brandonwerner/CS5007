#Name: Brandon Werner
#Assignment 5
#12/15/2017

from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont

root = Tk()

def button_lambda_handler(widget):
    print(widget["text"])

def button_lambda_handler1(widget):
    print(widget["text"] + " Selected" + str(widget.instate(statespec=["!selected"])))

def key_release_handler(event):
    print(event.widget["text"] + str(event.widget.get()))

def button1_handler(event):
    print("Submit")

def button2_handler(event):
    print("Cancel")

def combobox_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.get()))

def enter_release_text_handler(event):
    print(event.widget.get("1.0", END))

top_frame = Frame(root, highlightcolor="pink", highlightbackground="pink",  highlightthickness=5)
middle_frame = Frame(root, highlightcolor="teal", highlightbackground="teal",  highlightthickness=5)
middle_left_frame = Frame(middle_frame, highlightcolor="orange", highlightbackground="orange",  highlightthickness=5)
middle_right_frame = Frame(middle_frame, highlightcolor="green", highlightbackground="green",  highlightthickness=5)
sub_middle_frame = Frame(root, highlightcolor="red", highlightbackground="red",  highlightthickness=5)
bottom_frame = Frame(root, highlightcolor="blue", highlightbackground="blue",  highlightthickness=5)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)

top_frame.rowconfigure(0, weight=1)
top_frame.rowconfigure(1, weight=1)
top_frame.rowconfigure(2, weight=1)
top_frame.rowconfigure(3, weight=1)
top_frame.rowconfigure(4, weight=1)
top_frame.rowconfigure(5, weight=1)
middle_left_frame.rowconfigure(0, weight=1)
middle_left_frame.rowconfigure(1, weight=1)
middle_left_frame.rowconfigure(2, weight=1)
middle_right_frame.rowconfigure(0, weight=1)
middle_right_frame.rowconfigure(1, weight=1)
middle_right_frame.rowconfigure(2, weight=1)
bottom_frame.rowconfigure(0, weight=1)
middle_frame.rowconfigure(0, weight=1)

top_frame.columnconfigure(1, weight=1)
middle_frame.columnconfigure(0, weight=1)
middle_frame.columnconfigure(1, weight=1)
sub_middle_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)


text_field1 = ttk.Entry(top_frame)
text_field2 = ttk.Entry(top_frame)
text_field3 = ttk.Entry(top_frame)
text_field4 = ttk.Entry(top_frame, )

text_field1["width"] = 50
text_field2["width"] = 50
text_field3["width"] = 50
text_field4["width"] = 50

text_field1.grid(row=0, column=1, sticky=N+E+S+W)
text_field2.grid(row=1, column=1, sticky=N+E+S+W)
text_field3.grid(row=2, column=1, sticky=N+E+S+W)
text_field4.grid(row=3, column=1, sticky=N+E+S+W)

combo_box1 = ttk.Combobox(top_frame)
combo_box1.grid(row=4, column=1, sticky=N+E+S+W)
combo_box1["width"] = 50

combo_box1.bind("<<ComboboxSelected>>", combobox_handler)

# combo boxes are typically not editable
combo_box1.state(["readonly"])

combo_box1["values"] = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Pink", "White", "Black"]
combo_box1.current(0)

# radio buttons
# control group for buttons
control1 = IntVar()
control1.set(0)

control2 = IntVar()
control2.set(0)


radio_button1 = ttk.Radiobutton(middle_left_frame, value=YES, variable=control1, text="Yes", command=lambda:
button_lambda_handler(radio_button1))

radio_button2 = ttk.Radiobutton(middle_left_frame, value=NO, variable=control1, text="No", command=lambda:
button_lambda_handler(radio_button2))

radio_button3 = ttk.Radiobutton(middle_left_frame, value=YES, variable=control2, text="Yes", command=lambda:
button_lambda_handler(radio_button3))

radio_button4 = ttk.Radiobutton(middle_left_frame, value=NO, variable=control2, text="No", command=lambda:
button_lambda_handler(radio_button4))

radio_button1.state(statespec=["!selected"])
radio_button2.state(statespec=["!selected"])
radio_button3.state(statespec=["!selected"])
radio_button4.state(statespec=["!selected"])

radio_button1.grid(row=1, column=0, sticky=W)
radio_button2.grid(row=1, column=2, sticky=N+S+W)
radio_button3.grid(row=2, column=0, sticky=W)
radio_button4.grid(row=2, column=2, sticky=N+S+W)


control1 = IntVar()
control1.set(0)

control2 = IntVar()
control2.set(0)

control3 = IntVar()
control3.set(0)

control4 = IntVar()
control4.set(0)

check_button1 = ttk.Checkbutton(middle_right_frame, variable=control1, text="Baseball", command=lambda: button_lambda_handler1(check_button1))
check_button2 = ttk.Checkbutton(middle_right_frame, variable=control2, text="Basketball", command=lambda: button_lambda_handler1(check_button2))
check_button3 = ttk.Checkbutton(middle_right_frame, variable=control3, text="Football", command=lambda: button_lambda_handler1(check_button3))
check_button4 = ttk.Checkbutton(middle_right_frame, variable=control4, text="Hockey", command=lambda: button_lambda_handler1(check_button4))

check_button1.grid(row=1, column=0, sticky=N+S+W+E)
check_button2.grid(row=1, column=1, sticky=N+S+W+E)
check_button3.grid(row=2, column=0, sticky=N+S+W+E)
check_button4.grid(row=2, column=1, sticky=N+S+W+E)


# attach label to frame window
label1 = ttk.Label(top_frame, text="User Name:", font=tkfont.Font(family="Times New Roman", size=12))
label2 = ttk.Label(top_frame, text="First Name:", font=tkfont.Font(family="Times New Roman", size=12))
label3 = ttk.Label(top_frame, text="Last Name:", font=tkfont.Font(family="Times New Roman", size=12))
label4 = ttk.Label(top_frame, text="Password:", font=tkfont.Font(family="Times New Roman", size=12))
label5 = ttk.Label(top_frame, text="Favorite Color:", font=tkfont.Font(family="Times New Roman", size=12))
label6 = ttk.Label(top_frame, text="Account Options:", font=tkfont.Font(family="Times New Roman", size=12))
label7 = ttk.Label(top_frame, text="Sports (like to watch):",font=tkfont.Font(family="Times New Roman", size=12))
label8 = ttk.Label(middle_left_frame, text="Updates:", font=tkfont.Font(family="Times New Roman", size=10))
label9 = ttk.Label(middle_left_frame, text="Notification Emails:", font=tkfont.Font(family="Times New Roman", size=10))
label10 = ttk.Label(sub_middle_frame, text="Other Comments:", font=tkfont.Font(family="Times New Roman", size=12))
label11 = ttk.Label(middle_right_frame, text="")

label1.grid(row=0, column=0, sticky=W)
label2.grid(row=1, column=0, sticky=W)
label3.grid(row=2, column=0, sticky=W)
label4.grid(row=3, column=0, sticky=W)
label5.grid(row=4, column=0, sticky=W)
label6.grid(row=5, column=0, sticky=W)
label7.grid(row=5, column=1, sticky=E)
label8.grid(row=0, column=0, sticky=E)
label9.grid(row=0, column=2, sticky=E)
label10.grid(row=0, column=0, sticky=W)
label11.grid(row=0, column=0, sticky=N+S+E+W)

text_field1.bind("<KeyRelease-Return>", key_release_handler)
text_field2.bind("<KeyRelease-Return>", key_release_handler)
text_field3.bind("<KeyRelease-Return>", key_release_handler)
text_field4.bind("<KeyRelease-Return>", key_release_handler)

# create a style for the label
label1 = ttk.Style()


# configure a style for label

text1 = Text(sub_middle_frame, wrap=WORD, height=10, width=50)
text1.bind("<KeyRelease-Return>", enter_release_text_handler)
y_scrollbar = ttk.Scrollbar(sub_middle_frame, orient=VERTICAL, command=text1.yview) # yview called when scrollbar moves
text1['yscrollcommand'] = y_scrollbar.set

y_scrollbar.grid(row=1, column=1, sticky=N+S+E+W)
text1.grid(row=1, column=0, sticky=N+S+E+W)


# place frame on left on root
top_frame.grid(row=0, column=0, sticky=N+S+E+W)

# place frame on right of root
middle_frame.grid(row=1, column=0, sticky=N+S+E+W)

# place frame on top and bottom of right frame
middle_right_frame.grid(row=0, column=1, sticky=N+S+E)
middle_left_frame.grid(row=0, column=0, sticky=N+S+W)

sub_middle_frame.grid(row=2, column=0, sticky=N+S+E+W)

bottom_frame.grid(row=3, column=0, sticky=N+S+E+W)

#creates buttons
button1 = ttk.Button(bottom_frame)
button2 = ttk.Button(bottom_frame)
button1['text'] = "Submit"
button2['text'] = "Cancel"

# sets location of buttons
button1.grid(row=0, column=0, sticky=N+W+S+E)
button2.grid(row=0, column=1, sticky=N+W+S+E)

# create a style for the button
button_style1 = ttk.Style()
button_style2 = ttk.Style()

# configure button styles called button1 and button2
button_style1.configure('button1.TButton', font=("Times New Roman", 12))
button_style2.configure('button2.TButton', font=("Times New Roman", 12))

# set button1 and button2 to have the "button1" and "button2" styles
button1.configure(style='button1.TButton')
button2.configure(style='button2.TButton')

button1.bind("<ButtonRelease-1>", button1_handler)
button2.bind("<ButtonRelease-1>", button2_handler)

root.mainloop()