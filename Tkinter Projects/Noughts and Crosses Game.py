import tkinter as tk
import numpy as np

class GUI:
    # Box dimensions
    w = 500
    lw = 5 #line width

    def __init__(self, master):
        #Frame for canvases
        self.frame = tk.Frame(root, width = self.w*3, height = self.w*3, bg = "grey")
        self.frame.pack()

        #Initial draw of grid in Canvas
        self.Canvas = tk.Canvas(self.frame, bg="white", width=self.w, height=self.w)
        m_i = 3
        self.set(m_i)

        #Buttons
        self.quit_button = tk.Button(master,text="Quit", command=master.destroy).pack(side="right")
        self.label = tk.Label(master, text = "Enter size of playing field:").pack(side = "left")
        m_i = tk.IntVar(master,value=3)
        self.input_field = tk.Entry(master, font = ('arial', 18, 'bold'), textvariable = m_i, width = 2, bg = "white", bd = 0).pack(side="left", padx=15)
        self.restart_button = tk.Button(master,text="Restart", command= lambda: self.reset(m_i.get())).pack(side="left")

    def set(self, m_i):
        #Setup matrix for keeping score/drawing canvases
        self.m = np.array([ [ None for i in range(m_i) ] for j in range(m_i) ])
        r = m_i + 1 #Different ints to define regions
        self.m_c = [None] * r
        for i in range(r):
            self.m_c[i] = i*(self.w/m_i)

        #Draw grid to canvas
        rng = list(range(m_i))
        del rng[0]
        for i in rng:
            for j in rng:
                self.Canvas.create_line(0, i*self.w/m_i, self.w, i*self.w/m_i, width = self.lw)
                self.Canvas.create_line(j*self.w/m_i, 0, j*self.w/m_i, self.w, width = self.lw)
        self.Canvas.pack()

        #Bind
        self.Canvas.bind("<1>", lambda x: self.turn(x,m_i))

        #Turn count
        self.t = 1

    def reset(self, m_i):
        self.Canvas.delete("all")
        self.set(m_i)

    # Click - turn counter and click recording
    def turn(self, event, m_i):
        self.t += 1

        for i in range(m_i): #Check for which region click happened in x-direction
            if self.m_c[i] < event.y < self.m_c[i+1]:
                for j in range(m_i): #Check for which region click happened in y-direction
                    if self.m_c[j] < event.x < self.m_c[j+1]:
                        if self.m[i][j] is None: #If not already played in box
                            self.m[i][j] = self.t%2 #Element scored as 1 or 0

                            if self.t%2!=0: #Draw to relfect changed score matrix - Crosses
                                line = self.Canvas.create_line(self.m_c[j],self.m_c[i],self.m_c[j+1],
                                    self.m_c[i+1],width = self.lw, fill = "red")
                                line = self.Canvas.create_line(self.m_c[j+1],self.m_c[i],self.m_c[j],
                                    self.m_c[i+1],width = self.lw, fill = "red")

                            elif self.t%2==0: #Draw to relfect changed score matrix - Noughts
                                self.Canvas.create_oval(self.m_c[j+1],self.m_c[i],self.m_c[j],
                                    self.m_c[i+1],width = self.lw, outline = "blue")
        
        #Search for win condition
        w_f = None
        for w in range(2):
            for i in range(m_i):
                if all(self.m[i] == w):
                    w_f = w
            for j in range(m_i):
                if all(self.m[:,j] == w):
                    w_f = w
            if all(np.diagonal(self.m) == w):
                w_f = w
            elif all(np.diagonal(self.m[::-1,:] == w)):
                w_f = w
        
        if w_f is not None:
            self.end(w_f)
        elif self.t>(m_i**2): #Draw
            self.end(-1)

    def end(self,w_f):
        if w_f == 0:
            self.Canvas.create_rectangle(50,200,450,300,fill="white")
            self.Canvas.create_text(250,250,fill="blue",font="Helvetica 40 bold",text="Noughts wins!")
        elif w_f == 1:
            self.Canvas.create_rectangle(50,200,450,300,fill="white")
            self.Canvas.create_text(250,250,fill="red",font="Helvetica 40 bold",text="Crosses wins!")
        elif w_f == -1:
            self.Canvas.create_rectangle(50,200,450,300,fill="white")
            self.Canvas.create_text(250,250,fill="red",font="Helvetica 40 bold",text="Draw \U0001F634")
        self.Canvas.unbind("<1>") #Unbind to prevent further entries

root = tk.Tk()
root.title("Noughts and Crosses")
root.resizable(width=False, height=False)
my_gui = GUI(root)
root.mainloop()