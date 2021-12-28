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