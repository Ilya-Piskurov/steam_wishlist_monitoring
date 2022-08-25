package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sort"
)

// Тип, який представляє собою масив структур, що характеризують ігри.
type UserWishlist []GameInfo

//
type GameInfo struct {
	Name string `json:"name"`
	Subs []struct {
		Price    int64 `json:"price"`
		Discount int64 `json:"discount_pct"`
	} `json:"subs"`
}

// Перетворює мапу зі структурами на масив.
func mapToArrayWishlist(mapWishlist map[string]GameInfo) UserWishlist {
	userWishlist := make(UserWishlist, len(mapWishlist))
	i := 0
	for _, elem := range mapWishlist {
		userWishlist[i] = elem
		i++
	}
	return userWishlist
}

// Формує кінечну форму посилання, для цього приймає steam_id користувача.
func wishlistEndpoint(userSteamId string) string {
	return fmt.Sprintf(
		"https://store.steampowered.com/wishlist/profiles/%s/wishlistdata/",
		userSteamId,
	)
}

// Повертає сформований список бажаного, вимагає steam_id користувача.
func GetUserWishlist(userSteamId string) (UserWishlist, error) {
	resp, err := http.Get(wishlistEndpoint(userSteamId))
	if err != nil {
		return nil, fmt.Errorf("Cannot do get request: %v", err)
	}
	defer resp.Body.Close()

	var mapWishlist map[string]GameInfo
	err = json.NewDecoder(resp.Body).Decode(&mapWishlist)
	if err != nil {
		return nil, fmt.Errorf("Cannot decode json: %v", err)
	}

	arrWishlist := mapToArrayWishlist(mapWishlist)
	sort.Sort(arrWishlist)
	return arrWishlist, nil
}

// Для сортування UserWishlist

func (u UserWishlist) Len() int {
	return len(u)
}

func (u UserWishlist) Less(i, j int) bool {

	if len(u[i].Subs) == 0 && len(u[j].Subs) == 0 {
		return false
	}

	if len(u[i].Subs) == 0 && len(u[j].Subs) > 0 {
		return false
	} else if len(u[i].Subs) > 0 && len(u[j].Subs) == 0 {
		return true
	}

	if u[i].Subs[0].Discount < u[j].Subs[0].Discount {
		return false
	} else if u[i].Subs[0].Discount > u[j].Subs[0].Discount {
		return true
	}

	if u[i].Subs[0].Price > u[j].Subs[0].Price {
		return false
	} else {
		return true
	}
}

func (u UserWishlist) Swap(i, j int) {
	u[i], u[j] = u[j], u[i]
}
