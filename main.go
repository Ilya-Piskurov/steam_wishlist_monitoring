// A program that allows you to price changes and discounts on your
// Steam wishlist
package main

func main() {
	firstRun()
	CreateApplication()
}

func firstRun() {
	_, err := ReadSteamId()
	if err != nil {
		SaveSteamId("Enter your steamId here.")
	}
}
