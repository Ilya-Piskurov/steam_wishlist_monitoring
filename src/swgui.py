import tkinter as tk

class SWGui:
    def __init__(self, name, wishlist):
        self.window = tk.Tk()
        self.window.title(name)
        self.window.geometry('400x500')

        self.wishlist_frame = tk.LabelFrame(
            self.window,
            text       = 'Your Wishlist',
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16)
        )
        self.wishlist_frame.pack(expand=True, fill=tk.BOTH)
        for key in wishlist.keys():
            label = tk.Label(
                self.wishlist_frame,
                text = key + "  || " + wishlist[key][0] + " ||",
                foreground = '#ebcb8b',
                background = '#434c5e',
            )
            label.pack()
        self.sales_frame = tk.LabelFrame(
            self.window,
            text       = 'Sales',
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16)
        )
        self.sales_frame.pack(expand=True, fill=tk.BOTH)
        for key in wishlist.keys():
            if wishlist[key][1]:
                label = tk.Label(
                    self.sales_frame,
                    text = key + "  || " + wishlist[key][0] + " ||",
                    foreground = '#ebcb8b',
                    background = '#434c5e',
                )
                label.pack()
    
    def swgui_draw(self):
        self.window.mainloop()