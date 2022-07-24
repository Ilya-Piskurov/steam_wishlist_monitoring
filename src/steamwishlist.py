import requests, json, os

class SteamWishlist:
    def __init__(self, steam_id: str):
        '''
        Конструктор, отримує steam_id у форматі строки
        '''
        self.steam_id = steam_id
        self.steam_api_get_wishlist = f'https://store.steampowered.com/wishlist/profiles/{steam_id}/wishlistdata/'
        self.console_max_len = 45

    def download_wishlist(self):
        '''
        Завантжує json-об'єкт з списком бажаного, і зберігає у поле
        класу у форматі словник {ім'я гри: [ціна, розпродаж, процент]}
        '''
        try:
            wishlist = json.loads(requests.get(self.steam_api_get_wishlist).text)
        except:
            print("We're cannot download info from Steam")
            os._exit(0)
        self.wishlist = self.wishlist_to_dict(wishlist)

    def debug_print_wishlist(self):
        '''
        Виводить у консоль список бажаного.
        '''
        for name in self.wishlist.keys():
            print(name.ljust(self.console_max_len) + "Price = " + self.wishlist[name][0])

    def wishlist_to_dict(self, data) -> dict:
        '''
        Формотує json-об'єкт у словник {ім'я гри: [ціна, розпродаж, процент]}
        '''
        wishlist = {}
        for key in data.keys():
            price = "TBA"
            name  = data[key]['name']
            subs  = data[key]['subs']
            sale  = False
            percentage = 0
            if len(subs) != 0:
                price = str(subs[0]['price'])[0:-2] + "₴"
                percentage = subs[0]['discount_pct']
                if percentage > 0:
                    sale = True
            wishlist[name] = [price, sale, percentage]
        return wishlist

    def get_wishlist(self) -> dict:
        '''
        Повертає список бажаного
        '''
        self.download_wishlist()
        return self.wishlist
