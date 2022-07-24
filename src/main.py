import steamwishlist as sw
import swgui

if __name__ == "__main__":
    my_steam_id = '76561198428243990'
    my_wishlist = sw.SteamWishlist(my_steam_id)
    my_wishlist.download_wishlist()
    #my_wishlist.print_wishlist()

    gui = swgui.SWGui('Steam Wishlist', my_wishlist.get_wishlist())
    gui.swgui_draw()