package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	length, _ := strconv.Atoi(os.Args[1])
	nop, _ := strconv.Atoi(os.Args[2])
	list := make([]int, 1)
	list[0] = length
	count := 0
	for {
		if len(list) == length {
			break
		}
		count++
		max := nop
		if nop > len(list) {
			max = len(list)
		}
		for i := 0; i < max; i++ {
			list = devideList(list)
		}
	}
	fmt.Println(count)
}

func devideList(list []int) []int {
	var result []int
	process := false
	for _, v := range list {
		if v == 1 || process {
			result = append(result, v)
		} else {
			process = true
			result = append(result, v/2)
			if v%2 != 0 {
				result = append(result, v/2+1)
			} else {
				result = append(result, v/2)
			}
		}
	}
	return result
}
