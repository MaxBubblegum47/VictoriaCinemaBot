import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_952=tk.Listbox(root)
        GListBox_952["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=40)
        GListBox_952["font"] = ft
        GListBox_952["fg"] = "#333333"
        GListBox_952["justify"] = "center"
        GListBox_952.place(x=150,y=40,width=415,height=367)

        GButton_299=tk.Button(root)
        GButton_299["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=40)
        GButton_299["font"] = ft
        GButton_299["fg"] = "#000000"
        GButton_299["justify"] = "center"
        GButton_299["text"] = "Chat"
        GButton_299.place(x=30,y=350,width=100,height=50)
        GButton_299["command"] = self.GButton_299_command

        GButton_517=tk.Button(root)
        GButton_517["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=40)
        GButton_517["font"] = ft
        GButton_517["fg"] = "#000000"
        GButton_517["justify"] = "center"
        GButton_517["text"] = "Mostra Film"
        GButton_517.place(x=30,y=50,width=200,height=50)
        GButton_517["command"] = self.GButton_517_command

        GButton_697=tk.Button(root)
        GButton_697["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=40)
        GButton_697["font"] = ft
        GButton_697["fg"] = "#000000"
        GButton_697["justify"] = "center"
        GButton_697["text"] = "Login/Register"
        GButton_697.place(x=20,y=420,width=200,height=50)
        GButton_697["command"] = self.GButton_697_command

        GButton_825=tk.Button(root)
        GButton_825["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=40)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Info Film"
        GButton_825.place(x=190,y=420,width=200,height=50)
        GButton_825["command"] = self.GButton_825_command

        GButton_551=tk.Button(root)
        GButton_551["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=40)
        GButton_551["font"] = ft
        GButton_551["fg"] = "#000000"
        GButton_551["justify"] = "center"
        GButton_551["text"] = "Scarica Lista Film"
        GButton_551.place(x=490,y=420,width=200,height=50)
        GButton_551["command"] = self.GButton_551_command

        GButton_392=tk.Button(root)
        GButton_392["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=40)
        GButton_392["font"] = ft
        GButton_392["fg"] = "#000000"
        GButton_392["justify"] = "center"
        GButton_392["text"] = "<3"
        GButton_392.place(x=350,y=420,width=200,height=50)
        GButton_392["command"] = self.GButton_392_command

    def GButton_299_command(self):
        print("command")


    def GButton_517_command(self):
        print("command")


    def GButton_697_command(self):
        print("command")


    def GButton_825_command(self):
        print("command")


    def GButton_551_command(self):
        print("command")


    def GButton_392_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
