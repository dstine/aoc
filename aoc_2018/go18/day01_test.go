package main

import (
	"io/ioutil"
	"strings"
	"testing"
)

type Part func(changes []string) int

func TestPart1(t *testing.T) {
	RunPart(t, Part1, []string{"+1", "-2", "+3", "+1"}, 3)
	RunPart(t, Part1, []string{"+1", "+1", "+1"}, 3)
	RunPart(t, Part1, []string{"+1", "+1", "-2"}, 0)
	RunPart(t, Part1, []string{"-1", "-2", "-3"}, -6)
	RunPart(t, Part1, GetChanges("../data/day01_input.txt"), 400)
}

func TestPart2(t *testing.T) {
	RunPart(t, Part2, []string{"+1", "-2", "+3", "+1"}, 2)
	RunPart(t, Part2, []string{"+1", "-1"}, 0)
	RunPart(t, Part2, []string{"+3", "+3", "+4", "-2", "-4"}, 10)
	RunPart(t, Part2, []string{"-6", "+3", "+8", "+5", "-6"}, 5)
	RunPart(t, Part2, []string{"+7", "+7", "-2", "-7", "-4"}, 14)
	RunPart(t, Part2, GetChanges("../data/day01_input.txt"), 232)
}

func RunPart(t *testing.T, part Part, changes []string, expected int) {
	actual := part(changes)
	if actual != expected {
		t.Errorf("Incorrect, got: %d, expected: %d.", actual, expected)
	}
}

func GetChanges(path string) []string {
	bytes, _ := ioutil.ReadFile(path)
	str := string(bytes)
	strs := strings.Split(str, "\n")
	return strs
}
