// Програма для моніторингу вашого списку бажаного у Steam
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

// TODO
// 1. Англійська документація.
// 2. Сортування за скидками.
