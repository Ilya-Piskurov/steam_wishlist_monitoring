import tkinter as tk
import steamwishlist as sw
import os

class SWGui:
    def __init__(self, name):
        '''
        Конструктор класу SWGui (Steam-Wishlish-Gui).
        Створює вікно з назвою name та фрейми.
        '''
        self.steam_id = self.read_steam_id()

        self.window = tk.Tk()
        self.window.title(name)
        self.window.geometry('500x600')
        self.window.configure(background = '#434c5e')

        self.steam_id_frame = tk.LabelFrame(
            self.window,
            text       = 'Steam ID',
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16),
            height     = 100
        )
        self.steam_id_frame.pack(expand=False, fill=tk.BOTH)

        self.edit_id_box = tk.Entry(
            self.steam_id_frame,
            background = '#4c556a',
            foreground = '#bf616a',
            font       = (16),
        )
        self.edit_id_box.insert(0, self.steam_id)
        self.edit_id_box.pack()

        self.refresh_id_button = tk.Button(
            self.steam_id_frame,
            text       = 'Refresh ID',
            command    = self.click_refresh_id,
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16),
        )
        self.refresh_id_button.pack()

        userInfo = tk.Label(
            self.steam_id_frame,
            text = 'Enter steam_id and click "Refresh ID" and "Refresh Data"',
            foreground = '#a3be8c',
            background = '#434c5e',
        )
        userInfo.pack()

        self.sales_frame = tk.LabelFrame(
            self.window,
            text       = 'Sales',
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16),
            height     = 150,
        )
        self.sales_frame.pack(expand=True, fill=tk.BOTH)

        #scrollbar_sf = tk.Scrollbar(self.sales_frame)
        #scrollbar_sf.pack(side = tk.RIGHT, fill = tk.Y)

        self.wishlist_frame = tk.LabelFrame(
            self.window,
            text       = 'Your Wishlist',
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16),
            height     = 300
        )
        self.wishlist_frame.pack(expand=True, fill=tk.BOTH)

        #scrollbar_wf = tk.Scrollbar(self.wishlist_frame)
        #scrollbar_wf.pack(side = tk.RIGHT, fill = tk.Y)

        if self.steam_id != 'Undefined':
            self.wishlist = sw.SteamWishlist(self.steam_id).get_wishlist()
            self.draw_info_about_wishlist()

        self.refresh_data_button = tk.Button(
            self.window,
            text       = 'Refresh Data',
            command    = self.click_refresh_data,
            background = '#434c5e',
            foreground = '#bf616a',
            font       = (16),
        )
        self.refresh_data_button.pack()

    def draw_info_about_wishlist(self):
        '''
        Виводить інфу про ваш список бажаного у визначені фрейми.
        '''
        scrollbar_sf = tk.Scrollbar(self.sales_frame)
        scrollbar_sf.pack(side = tk.RIGHT, fill = tk.Y)

        scrollbar_wf = tk.Scrollbar(self.wishlist_frame)
        scrollbar_wf.pack(side = tk.RIGHT, fill = tk.Y)

        for key in self.wishlist.keys():
            label = tk.Label(
                self.wishlist_frame,
                text = key + "  || " + self.wishlist[key][0] + " ||",
                foreground = '#ebcb8b',
                background = '#434c5e',
                font       = (14)
            )
            label.pack()
        
        for key in self.wishlist.keys():
            if self.wishlist[key][1]:
                label = tk.Label(
                    self.sales_frame,
                    text = key + "  || " + self.wishlist[key][0] + " , " +
                        " SALE: " + str(self.wishlist[key][2]) + "% ||",
                    foreground = '#ebcb8b',
                    background = '#434c5e',
                    font       = (14)
                )
                label.pack()

    def click_refresh_id(self):
        '''
        Обробчик події натиску на кнопку Refresh ID (Оновити ID).
        Зберігає новий айді.
        '''
        self.steam_id = self.edit_id_box.get()

        dirname = os.path.dirname(__file__)
        filename = dirname + '\\res\\steam_id.txt'
        f = open(filename, 'w', encoding='utf-8')
        f.write(self.steam_id)
        f.close()

    def click_refresh_data(self):
        '''
        Обробчик події натиску на кнопку Refresh Data (Оновити дані).
        Видаляє стару інформацію, перекачує й виводить нову.
        '''
        self.wishlist = sw.SteamWishlist(self.steam_id).get_wishlist()
        self.clear_frames_swgui()
        self.draw_info_about_wishlist()

    def clear_frames_swgui(self):
        '''
        Видаляє нащадків фреймів.
        '''
        for widgets in self.wishlist_frame.winfo_children():
            widgets.destroy()
        for widgets in self.sales_frame.winfo_children():
            widgets.destroy()
    
    def swgui_draw(self):
        '''
        Запускає головний цикл вікна.
        '''
        self.window.mainloop()

    def read_steam_id(self) -> str:
        dirname = os.path.dirname(__file__)
        filename = dirname + '\\res\\steam_id.txt'

        try:
            f = open(filename, 'r', encoding='utf-8')
            steam_id = f.readline()
            f.close()
        except:
            steam_id = 'Undefined'

        return steam_id