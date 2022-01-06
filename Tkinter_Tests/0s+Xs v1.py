import tkinter as tk
import numpy as np

#Box dimensions
w = 500
lw = 10 #line width
m_i = 3 # square matrix length
ws = None #Win state (0 or 1) or draw (-1)

class GUI:
    def __init__(self, master):
        #Frame for canvases
        self.frame = tk.Frame(root, width = w*3, height = w*3, bg = "grey")
        self.frame.pack()

        #Setup matrix for keeping score/drawing canvases
        self.m = np.array([ [ None for i in range(m_i) ] for j in range(m_i) ])
        r = m_i + 1 #Different ints to define regions
        self.m_c = [None] * r
        for i in range(r):
            self.m_c[i] = i*(w/m_i)

        #Initial draw of grid in Canvas
        self.Canvas = tk.Canvas(self.frame, bg="white", width=w, height=w)
        rng = list(range(m_i))
        del rng[0]
        for i in rng:
            for j in rng:
                self.Canvas.create_line(0, i*w/3, w, i*w/3, width = lw)
                self.Canvas.create_line(j*w/3, 0, j*w/3, w, width = lw)
        self.Canvas.pack()

        #Bind
        self.Canvas.bind("<1>", lambda x: self.turn(x))

        #Quit button
        self.quit_button = tk.Button(master,text="Quit", command=master.destroy).pack()
        self.restart_button = tk.Button(master,text="Restart", command=self.restart).pack()

        #Turn count
        self.t = 1

    #def restart(self):
        #self.Canvas.delete("all")
        #self.frame.pack_forget
        #self.__init__(0)

    #Click - turn counter and click recording
    def turn(self, event):
        self.t+=1

        for i in range(m_i): #Check for which region click happened in x-direction
            if self.m_c[i] < event.y < self.m_c[i+1]:
                for j in range(m_i): #Check for which region click happened in y-direction
                    if self.m_c[j] < event.x < self.m_c[j+1]:
                        if self.m[i][j] is None: #If not already played in box
                            self.m[i][j] = self.t%2
                            #print("scores:\n",self.m)

                            if self.t%2!=0: #Draw and change score matrix - Crosses
                                self.Canvas.create_line(self.m_c[j],self.m_c[i],self.m_c[j+1],
                                    self.m_c[i+1],width = lw, fill = "red")
                                self.Canvas.create_line(self.m_c[j+1],self.m_c[i],self.m_c[j],
                                    self.m_c[i+1],width = lw, fill = "red")

                            elif self.t%2==0: #Draw and change score matrix - Noughts
                                self.Canvas.create_oval(self.m_c[j+1],self.m_c[i],self.m_c[j],
                                    self.m_c[i+1], width = lw, outline = "blue")
        
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
        elif self.t>=9 and w_f is None: #Draw
            self.end(-1)



    def end(self,w_f):
        if w_f == 0:
            print("Noughts wins!")
        elif w_f == 1:
            print("Crosses wins!")
        elif w_f == -1:
            print("Draw!")  

        self.Canvas.unbind("<1>") #Unbind to prevent further entries

root = tk.Tk()
root.title("Noughts and Crosses")
root.resizable(width=False, height=False)
my_gui = GUI(root)
root.mainloop()