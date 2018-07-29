
from tkinter import *
from tkinter import ttk

root = Tk()

# sticky -> means widget can be places or stretched within the limits of its bounding area
# row/column configure -> allow row/column to expand to fill more area (instead of "dead space")


# attached left and right to root
# give a huge border to demonstrate
left = Frame(root, highlightcolor="orange", highlightbackground="orange",  highlightthickness=5)
right = Frame(root, highlightcolor="red", highlightbackground="red",  highlightthickness=5)

# attached right_sub_top to right, give a huge border to demonstrate
right_sub_top = Frame(right, highlightcolor="blue", highlightbackground="blue",  highlightthickness=5)

# attached right_sub_bottom, give a huge border to demonstrate
right_sub_bottom = Frame(right, highlightcolor="green", highlightbackground="green", highlightthickness=5)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

print(right_sub_bottom.configure())

# give equal weight to all four rows on left frame
left.rowconfigure(0, weight=1)
left.rowconfigure(1, weight=1)
left.rowconfigure(2, weight=1)
left.rowconfigure(3, weight=1)

# one column
left.columnconfigure(0, weight=1)

# give equal weight to the two rows (each row will contain another frame)
right.rowconfigure(0, weight=1)
right.rowconfigure(1, weight=1)

# one column
right.columnconfigure(0, weight=1)

# give equal weight to both rows and columns
right_sub_top.rowconfigure(0, weight=1)
right_sub_top.rowconfigure(1, weight=1)
right_sub_top.columnconfigure(0, weight=1)
right_sub_top.columnconfigure(1, weight=1)

right_sub_bottom.rowconfigure(0, weight=1)
right_sub_bottom.rowconfigure(1, weight=1)
right_sub_bottom.columnconfigure(0, weight=1)
right_sub_bottom.columnconfigure(1, weight=1)


button1 = ttk.Button(left, text="Button 1")
button2 = ttk.Button(left, text="Button 2")
button3 = ttk.Button(left, text="Button 3")
button4 = ttk.Button(left, text="Button 4")
button5 = ttk.Button(right_sub_top, text="Button 5")
button6 = ttk.Button(right_sub_top, text="Button 6")
button7 = ttk.Button(right_sub_top, text="Button 7")
button8 = ttk.Button(right_sub_top, text="Button 8")
button9 = ttk.Button(right_sub_bottom, text="Button 9")
button10 = ttk.Button(right_sub_bottom, text="Button 10")
button11 = ttk.Button(right_sub_bottom, text="Button 11")
button12 = ttk.Button(right_sub_bottom, text="Button 12")


# place on left
button1.grid(row=0, column=0, sticky=N+S+E+W)
button2.grid(row=1, column=0, sticky=N+S+E+W)
button3.grid(row=2, column=0, sticky=N+S+E+W)
button4.grid(row=3, column=0, sticky=N+S+E+W)

# place on top right
button5.grid(row=0, column=0, sticky=N+S+E+W)
button6.grid(row=0, column=1, sticky=N+S+E+W)
button7.grid(row=1, column=0, sticky=N+S+E+W)
button8.grid(row=1, column=1, sticky=N+S+E+W)

# place on bottom right
button9.grid(row=0, column=0, sticky=N+S+E+W)
button10.grid(row=0, column=1, sticky=N+S+E+W)
button11.grid(row=1, column=0, sticky=N+S+E+W)
button12.grid(row=1, column=1, sticky=N+S+E+W)

# place frame on left on root
left.grid(row=0, column=0, sticky=N+S+E+W)

# place frame on right of root
right.grid(row=0, column=1, sticky=N+S+E+W)

# place frame on top and bottom of right frame
right_sub_top.grid(row=0, column=0, sticky=N+S+E+W)
right_sub_bottom.grid(row=1, column=0, sticky=N+S+E+W)

root.mainloop()
