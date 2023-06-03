import tkinter as tk
import generator, gen_sequences

def on_focus_in(entry, click_id):
    entry.delete(0,tk.END)
    entry.unbind('<FocusIn>', click_id)

root = tk.Tk()

sequence_list = ['primes', 'fibonacci', 'squares', 'triangles', 'cubes', 'tables']
colours = {'primes': (0,0,0),'fibonacci': (0,0,0),'squares': (0,0,0),'triangles': (0,0,0),'cubes': (0,0,0),'tables': (0,0,0),}
name_to_RGB = {'red': (255,0,0), 'blue': (0,0,255), 'green': (0,255,0), 'magenta': (255,0,255), 'cyan': (0,255,255), 'yellow': (255,255,0), 'white': (255,255,255)}
all_colours = ['red', 'blue', 'green', 'magenta', 'cyan', 'yellow', 'white']

dimensions = tk.Frame()
x_lbl = tk.Label(master=dimensions, text="X size: ")
x_lbl.pack(side=tk.LEFT)
x_size = tk.Entry(master=dimensions, width=5)
x_size.pack(side=tk.LEFT)
x_size.insert('1', '200')
x_click_id = x_size.bind("<FocusIn>", lambda args: on_focus_in(x_size, x_click_id))
y_lbl = tk.Label(master=dimensions, text="Y size: ")
y_lbl.pack(side=tk.LEFT)
y_size = tk.Entry(master=dimensions, width=5)
y_size.pack(side=tk.LEFT)
y_size.insert('1', '200')
y_click_id = y_size.bind("<FocusIn>", lambda args: on_focus_in(y_size, y_click_id))
dimensions.pack()

framelist = []
for x in range(6):
    frame = tk.Frame(borderwidth=5)
    frame.pack()
    framelist.append(frame)

colour_list = []
chosen_sequences = []
for x in range(6):
    checkbox_num = tk.IntVar()
    checkbox = tk.Checkbutton(framelist[x], text=sequence_list[x],variable=checkbox_num, onvalue=1, offvalue=0)
    checkbox.pack(side=tk.LEFT)
    options = tk.StringVar()
    options.set(all_colours[-1])
    drop = tk.OptionMenu(framelist[x], options, *all_colours)
    drop.pack(side=tk.LEFT)
    colour_list.append(options)
    chosen_sequences.append(checkbox_num)

# def showimg():
#     global image
#     image.destroy()
#     img = Image.open("image.png")
#     photo = ImageTk.PhotoImage(img)
#     image = tk.Label(image=photo)
#     image.pack()
def generate(event):
    gen_btn["text"] = 'Generating...'
    sequences_chosen = []
    x_size_int = int(x_size.get())
    y_size_int = int(y_size.get())
    for x in range(6):
        if chosen_sequences[x].get() == 1:
            sequences_chosen.append(sequence_list[x])
        colours[sequence_list[x]] = name_to_RGB[colour_list[x].get()]
    generator.image(x_size_int,y_size_int,gen_sequences.get_sequences(sequences_chosen, y_size_int*x_size_int),colours)
    gen_btn["text"] = 'Generate!'
    # showimg()

gen_btn = tk.Button(text="Generate!", width=15, height=3, bg="orange", fg="blue")
gen_btn.bind('<Button-1>', generate)
gen_btn.pack()

# image = tk.Label(text="No image")
# image.pack()


root.mainloop()