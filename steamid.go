package main

import (
	"fmt"
	"os"
)

const (
	// Шлях до файлу, який зберігає steam_id користувача між сесіями.
	filePath = "steamId.txt"
)

// Функція, що читає steam_id користувача з файлу.
func ReadSteamId() (string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return "", fmt.Errorf("Cannot read steamId from file: %v", err)
	}
	return string(data), nil
}

// Функція, що записує отриманий steam_id користувача у файл.
func SaveSteamId(steamId string) error {
	file, err := os.Create(filePath)
	if err != nil {
		return fmt.Errorf("Cannot create save file: %v", err)
	}
	file.WriteString(steamId)
	return nil
}
