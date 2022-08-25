package main

import (
	"fmt"
	"os"
)

const (
	// Path to the file that contains the steam_id between sessions
	filePath = "steamId.txt"
)

//  A function that reads steamId from a file in the "filePath"
func ReadSteamId() (string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return "", fmt.Errorf("Cannot read steamId from file: %v", err)
	}
	return string(data), nil
}

//  A function that write steamId in the "filePath" path
func SaveSteamId(steamId string) error {
	file, err := os.Create(filePath)
	if err != nil {
		return fmt.Errorf("Cannot create save file: %v", err)
	}
	file.WriteString(steamId)
	return nil
}
