package main

import (
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/widget"
)

// Main Function GUI.
func CreateApplication() {

	a := app.New()
	w := a.NewWindow("Steam Wishlist Monitoring")
	w.Resize(fyne.NewSize(500, 600))

	drawGui(w)

	w.ShowAndRun()
}

// Function for downloading the wish list.
// Takes steamId and fyne.Window (for dialog)
func downloadWishlist(steamId string, window fyne.Window) (UserWishlist, bool) {
	userWishlist, err := GetUserWishlist(steamId)
	result := true
	if err != nil {
		dialog.ShowInformation(
			"Failed Download Wishlist",
			"Please make sure your steamID and \nprivacy settings are correct in\nSteam (wishlist must be public)",
			window)
		result = false
	}
	return userWishlist, result
}

// Creates a convenient line to display information about the game
func createText(gameInfo GameInfo) (text string) {
	if len(gameInfo.Subs) > 0 {
		str := fmt.Sprint(gameInfo.Subs[0].Price)
		text = fmt.Sprintf(
			"%10s, %2d%% - %s",
			str[:len(str)-2]+"₴",
			gameInfo.Subs[0].Discount,
			gameInfo.Name)
	} else {
		text = fmt.Sprintf("%20s - %s", "TBA", gameInfo.Name)
	}
	return
}

// Creates a fyne-list from UserWishlist
func createWishlist(wishlist UserWishlist, ok bool) fyne.CanvasObject {
	var fyneList fyne.CanvasObject
	if ok {
		fyneList = widget.NewList(
			func() int {
				return len(wishlist)
			},
			func() fyne.CanvasObject {
				return widget.NewLabel("template")
			},
			func(i widget.ListItemID, o fyne.CanvasObject) {
				text := createText(wishlist[i])
				o.(*widget.Label).SetText(text)
			})
	} else {
		fyneList = widget.NewLabel("Failed Download Wishlist\nPlease make sure your steamID and \nprivacy settings are correct in\nSteam (wishlist must be public)")
	}
	return fyneList
}

// Function for displaying and updating graphics
func drawGui(w fyne.Window) {
	steamId, err := ReadSteamId()
	if err != nil {
		panic(err)
	}
	wishlist, ok := downloadWishlist(steamId, w)

	labelSteamId := widget.NewLabel(
		"Your SteamID: if you open the program for the first time, enter it")
	entrySteamId := widget.NewEntry()
	entrySteamId.Text = steamId
	buttonRefreshSteamId := widget.NewButton("Download Wish List", func() {
		steamId = entrySteamId.Text
		SaveSteamId(steamId)
		drawGui(w)
	})

	contentSteamIdBox := container.NewVBox(
		labelSteamId, entrySteamId, buttonRefreshSteamId)

	fyneWishlist := createWishlist(wishlist, ok)

	mainContent := container.NewVSplit(
		fyneWishlist, contentSteamIdBox)

	w.SetContent(mainContent)
}
