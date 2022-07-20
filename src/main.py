import requests, json

class SteamWishlist:
    def __init__(self, steam_id: str):
        '''
        Конструктор, отримує steam_id у форматі строки
        '''
        self.steam_id = steam_id
        self.steam_api_get_wishlist = f'https://store.steampowered.com/wishlist/profiles/{steam_id}/wishlistdata/'

    def download_wishlist(self):
        '''
        Завантжує json-об'єкт з списком бажаного, і зберігає у поле
        класу у форматі словник { ім'я гри: ціна }
        '''
        wishlist = json.loads(requests.get(self.steam_api_get_wishlist).text)
        self.wishlist = self.wishlist_to_dict(wishlist)

    def print_wishlist(self):
        '''
        Виводить у консоль список бажаного.
        '''
        for name in self.wishlist.keys():
            print(name.ljust(45) + "Price = " + self.wishlist[name])

    def wishlist_to_dict(self, data):
        '''
        Формотує json-об'єкт у словник { ім'я гри: ціна }
        '''
        wishlist = {}
        for key in data.keys():
            price = "Undefined"
            name  = data[key]['name']
            subs  = data[key]['subs']
            if len(subs) != 0:
                price = str(subs[0]['price'])[0:-2] + "₴"
            wishlist[name] = price
        return wishlist

my_steam_id = '76561198428243990'
my_wishlist = SteamWishlist(my_steam_id)
my_wishlist.download_wishlist()
my_wishlist.print_wishlist()