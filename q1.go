package main

import "fmt"

func main() {
	start := 11
	for {
		if check(start) {
			fmt.Println(start)
			break
		}
		start += 2
	}
}

func check(num int) bool {
	strList := []string{
		fmt.Sprintf("%d", num),
		fmt.Sprintf("%b", num),
		fmt.Sprintf("%o", num),
	}
	for _, v := range strList {
		if v != reverse(v) {
			return false
		}
	}

	return true
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
