import tkinter as tk

class GUI:
    def __init__(self, master):
        widget_width=50
        
        #Input Frame
        self.input_frame = tk.Frame(root, width = widget_width, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
        self.input_frame.pack(side = 'top')

        self.but_input = tk.StringVar()
        self.input_field = tk.Entry(self.input_frame, font = ('arial', 18, 'bold'), textvariable = self.but_input, width = 25, bg = "#eee", bd = 0, justify = 'right')
        self.input_field.grid(row = 0, column = 0)
        self.input_field.pack(ipady = 10)

        #Buttons frame
        self.but_frame = tk.Frame(root, width = widget_width, height = 272.5, bg = "grey")
        self.but_frame.pack()

        #Number and operator buttons - Sequentially create buttons from list (4 columns)
        self.buttons_base = "7,8,9,/,4,5,6,*,1,2,3,-,0,.,**,+".split(",") 
        self.buttons = {}
        for i in range(len(self.buttons_base)):
            o = self.buttons_base[i]
            self.buttons[i] = tk.Button(self.but_frame, text = o, fg = "black", width = round(widget_width*0.25), height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda o=o: self.but_update(o)).grid(row = i//4, column = i-((i//4)*4), padx = 1, pady = 1)

        #Equal and clear buttons/ bindings (return and escape)
        self.equal = tk.Button(self.but_frame, text = "=", fg = "black", width = round(widget_width*0.5), height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.but_equal()).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
        root.bind('<Return>', lambda x: self.but_equal())
        self.clear = tk.Button(self.but_frame, text = "C", fg = "black", width = round(widget_width*0.5), height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.but_clear()).grid(row = 4, column = 2, columnspan = 2, padx = 1, pady = 1)
        root.bind('<Escape>', lambda x: self.but_clear()) 

    #Update after button press
    def but_update(self,operator):
        self.but_input.set(self.but_input.get() + operator)
        self.input_field.icursor("end")
    
    #Calculate input
    def but_equal(self):
        input = self.but_input.get().lstrip("0")
        alpha = [i.isalpha() for i in input]    #Deny invalid alpha chars
        if any(alpha):
            print("Alpha character found")
        elif input == "":                      #Deny empty input
            pass
        else:
            output = str(eval(input))
            self.but_input.set(output)
    
    #Clear input
    def but_clear(self):
        self.but_input.set("")

root = tk.Tk()
root.title("Calculator - Created by WB")
root.resizable(width=False, height=False)
my_gui = GUI(root)
root.mainloop()