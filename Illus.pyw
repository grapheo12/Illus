'''
   Copyright 2017 Shubham Mishra
   
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from Tkinter import *

class RtDialog(Label):
    def __init__(self, root, color, pwidth, x, y):
        Label.__init__(self, root, height=40, width=40)
        self.colors = ('White', 'Black', 'Blue', 'Beige',\
                       'Cyan', 'Magenta', 'Green', 'Red', 'Orange', 'Brown',\
                       'Yellow')
        self.menu = apply(OptionMenu, (self, color) + self.colors)
        self.menu.pack()
        
        self.pwidth = pwidth
        self.wcontrol = Scale(self, from_=1, to=100, orient=HORIZONTAL)
        self.wcontrol.bind('<Button-1>', self.assignwidth)
        self.wcontrol.bind('<B1-Motion>', self.assignwidth)
        self.wcontrol.set(pwidth.get())
        self.wcontrol.pack()

        self.place(x=x, y=y)
        
    def assignwidth(self, event):
        self.pwidth.set(self.wcontrol.get())

class DrawBoard(Canvas):
    def __init__(self, root):
        self.root = root
        Canvas.__init__(self, root, background="black")
        self.configure(height=768, width=1024)
        self.bind("<Button-1>", self.coordreset)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<B2-Motion>", self.erase)
        self.bind("<Button-3>", self.showDialog)
        self.config(scrollregion=self.bbox(ALL))
	    self.x = 0
	    self.y = 0
        self.dialogbox = Label(root)
        self.color = StringVar()
        self.color.set('white')
        self.pwidth = IntVar()
        self.pwidth.set('50')
        
        self.pack()
        
    def draw(self, event):
        self.dialogdeath()
        col = self.color.get()
        pwi = self.pwidth.get() / 10
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        self.create_line(self.x, self.y, x, y, fill=col, width=pwi)
	self.coordreset(event)
        
    def erase(self, event):
        self.dialogdeath()
        col = self.cget('bg')
        pwi = self.pwidth.get() / 10
        x = event.x
        y = event.y
        self.create_oval(x-pwi, y-pwi, x+pwi, y+pwi, fill=col)
                  
    def showDialog(self, event):
        self.dialogdeath()
        self.dialogbox = RtDialog(self.root, self.color, self.pwidth, event.x, event.y)
    def dialogdeath(self):
        self.dialogbox.destroy()

    def coordreset(self, event):
	self.x, self.y = self.canvasx(event.x), self.canvasy(event.y)
        

if __name__=="__main__":
    def createboard(*args):
        global Board
        Board.destroy()
        Board = DrawBoard(root)
        
    def onmousewheel(event):
        if event.num == 4:
            Board.yview_scroll(-1, "units")
        else:
            Board.yview_scroll(1, "units")

        
    root = Tk()
    root.geometry('640x480')
    root.maxsize(width=1024, height=768)
    
    icon = PhotoImage(file="icon.png")
    root.tk.call('wm', 'iconphoto', root._w, icon)
           
    Board = Label(text='ILLUS\nby Shubham Mishra')
    Board.pack()
    root.title('ILLUS')
    root.bind('<N>', createboard)
    createboard()
    Board.bind_all("<Button-4>",onmousewheel)
    Board.bind_all("<Button-5>", onmousewheel)


    
    root.mainloop()
    
