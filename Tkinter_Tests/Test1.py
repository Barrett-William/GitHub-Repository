import tkinter as tk

class GUI:
    def __init__(self, master):
        self.label = tk.Label(root, text="               Text in the GUI!                ").pack()

        #Name Entry
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry_submit = tk.Button(master, text="Submit text", command=self.submit).pack()

        #Canvas
        self.Canvas = tk.Canvas(root, bg="white").pack()

        #On/off check
        self.check = tk.IntVar()
        self.e = tk.Checkbutton(root, text="check me", variable=self.check).pack()
        self.macro_button = tk.Button(master, text="Test Button", command=self.test).pack()

        #Quit button
        self.quit_button = tk.Button(master,text="Quit", command=master.destroy).pack()

        #Label 
        #self.label = tk.Label(root, text="Eval function calculator").pack()      

        #Entry
        #self.entry = tk.Entry(root)
        #self.entry.pack()
        #self.entry_submit = tk.Button(master, text="Submit text", command=self.calculate_input).pack()

        #On/off check
        #self.check = tk.IntVar()
        #self.e = tk.Checkbutton(root, text="Check me if you trust the eval (evil) function", variable=self.check).pack()

        #Answer canvas
        #self.canvas = tk.Canvas(root, bg="white",height=70)
        #self.canvas.pack()
        #self.text = self.canvas.create_text((50,30),fill="darkblue",font="Calibri 50",text="__")

    #Calculate input
    def calculate_input(self):
        if self.check.get():
            input = self.entry.get()
            output = str(eval(input))
            self.canvas.itemconfig(self.text, text=output)
            
    #Check on/off state of check
    def test(self):
        if self.check.get():
            print('its on')
        else:
            print('its off')

    #Empty input filter
    def submit(self):
        print(self.entry.get())

root = tk.Tk()
root.title("GUI")
root.resizable(width=False, height=False)
my_gui = GUI(root)
root.mainloop()