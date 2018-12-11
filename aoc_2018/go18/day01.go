package main

import (
	"strconv"
)

func Part1(changes []string) int {
	var result int
	for _, change := range changes {
		val, _ := strconv.Atoi(change)
		result += val
	}
	return result
}

func Part2(changes []string) int {
	result := 0
	results := make(map[int]int)
	results[result] = 1
	for true {
		for _, change := range changes {
			val, _ := strconv.Atoi(change)
			result += val
			_, encountered := results[result]
			if encountered {
				return result
			} else {
				results[result] = 1
			}
		}
	}
	return 0
}
