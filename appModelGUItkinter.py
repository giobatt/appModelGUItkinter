## app model to create a GUI with tkinter in python3


# imports libraries
import tkinter as tk
from tkinter import ttk  # import ttk to have better graphic aspects


# definition of app class
class GUIApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None

        self.winfo_toplevel().title('APP MODEL with GUI')
        self.geometry('300x200')

        # menubar configuration
        menubar = tk.Menu(self)
        menu = tk.Menu(menubar)

        menu_quit = tk.Menu(menubar)
        menu_quit.add_command(label='Quit', command=self.quit)
        menubar.add_cascade(label='File', menu=menu_quit)

        menu.add_command(label='Start', command=lambda: self.switch_frame(StartPage))
        menu.add_command(label='Page 1', command=lambda: self.switch_frame(PageOne))
        menu.add_command(label='Page 2', command=lambda: self.switch_frame(PageTwo))
        menubar.add_cascade(label='Options', menu=menu)

        self.config(menu=menubar)

        self.switch_frame(StartPage)

    # definition function to switch frames deleting the old one
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# StartPage definition
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        ttk.Button(self, text="Open page one",
                   command=lambda: master.switch_frame(PageOne)).pack()
        ttk.Button(self, text="Open page two",
                   command=lambda: master.switch_frame(PageTwo)).pack()


# PageOne definition
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        ttk.Button(self, text="Return to start page",
                   command=lambda: master.switch_frame(StartPage)).pack()


# PageTwo definition
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        ttk.Button(self, text="Return to start page",
                   command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()
