package main

import (
	"fmt"
	"flag"
	"io/ioutil"
	"strings"
)

var (
	filepath = flag.String("input", "input/problem_008.txt", "file containing the input value")
)

func getInputValue(filename string) []int {
	dat, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	digitList := []byte(strings.ReplaceAll(string(dat), "\n", ""))

	res := make([]int, len(digitList))
	for i, c := range digitList {
		res[i] = int(c - '0')
	}
	return res
}

func multiplySlice(digits []int) int {
	partial := 1
	for _, v := range digits {
		partial *= v
	}
	return partial
}

func highestSequence(digits []int, k int) int {
	digitsLen := len(digits)

	highest := -1
	for i := 0; i < digitsLen - k; i++ {
		product := multiplySlice(digits[i:i+k])
		if product > highest {
			highest = product
		}
	}
	return highest
}

func main() {
	flag.Parse()

	inputValue := getInputValue(*filepath)
	highest := highestSequence(inputValue, 4)
	fmt.Println(highest)

	highest = highestSequence(inputValue, 13)
	fmt.Println(highest)
}