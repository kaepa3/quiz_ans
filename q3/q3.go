package main

import "fmt"

func main() {
	resultList := make([]bool, 100)

	for start := 2; start < len(resultList); start++ {
		var flg bool
		for i := start - 1; i < len(resultList); i += start {
			flg = true
			resultList[i] = !resultList[i]
		}
		if !flg {
			break
		}
	}
	outputResult(resultList)
}

func outputResult(list []bool) {

	for i, v := range list {
		if !v {
			fmt.Println(i + 1)
		}
	}
}
