import tkinter as tk
import numpy as np

#Box dimensions
w = 100

class GUI:
    def __init__(self, master):
        #Frame for canvases
        self.frame = tk.Frame(root, width = w*3, height = w*3, bg = "grey")
        self.frame.pack()

        self.frame.bind('<Button-1>', lambda x: self.draw, add="+")
        self.frame.bind('<Button-1>', lambda x: self.turn(), add="+")
        self.frame.bind("<Button-1>", lambda x: self.callback(x) , add="+")

        #Setup matrix for keeping score/drawing canvases
        m_i = 3 # square matrix setup
        m = ([ [ 0 for i in range(m_i) ] for j in range(m_i) ])
        #m_r = {}
        #for j in range(m_i):
        #    for i in range(m_i):
        #        m_w = m_w={}
        self.m_r = np.array([ w*i for i in range(m_i+1) ])
        print(self.m_r)

        #Initial draw
        self.Canvas = m
        for i in range(m_i):
            for x in range(m_i):
                self.Canvas[i][x] = tk.Canvas(self.frame, bg="white", width=w, height=w)
                self.Canvas[i][x].grid(row = i, column = x)

                bindtags=list(self.Canvas[i][x].bindtags())
                bindtags.insert(0, self.frame)
                self.Canvas[i][x].bindtags(tuple(bindtags))

                self.Canvas[i][x].bind("<1>", self.on_sub_click)

        #Quit button
        self.quit_button = tk.Button(master,text="Quit", command=master.destroy).pack()

        #Turn count
        self.t = 1

    #Turn counter
    def turn(self):
        self.t+=1
    
    #Draw on click
    def draw(self):
        lw = 10 #line width
        if self.t%2==0:
            self.Canvas[0][0].create_line(0+lw, 0+lw, w-lw, w-lw, width = lw, fill = "red")
            self.Canvas[0][0].create_line(w-lw, 0+lw, 0+lw, w-lw, width = lw, fill = "red")
        elif self.t%2!=0:
            self.Canvas[2][2].create_oval(0+lw, 0+lw, w-lw, w-lw, width = lw, outline = "blue")

    def on_sub_click(self, event):
        print("sub widgets: clicked at", event.x, event.y, event)
        self.callback(event)

    def callback(self, event):
        print("clicked at", event.x, event.y, event)
        print(np.digitize(np.array([event.x,event.y]), self.m_r)) #first region is 1,1

root = tk.Tk()
root.title("Noughts and Crosses")
root.resizable(width=False, height=False)
my_gui = GUI(root)
root.mainloop()