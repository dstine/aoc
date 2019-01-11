package com.github.dstine.aoc.kt18

import java.io.File
import org.junit.Assert.assertEquals
import org.junit.Test

class Day01Test {

    @Test
    fun test1() {
        assertEquals(part1(listOf("+1", "-2", "+3", "+1")), 3)
        assertEquals(part1(listOf("+1", "+1", "+1")), 3)
        assertEquals(part1(listOf("+1", "+1", "-2")), 0)
        assertEquals(part1(listOf("-1", "-2", "-3")), -6)
        val myInput = getMyInput()
        assertEquals(part1(myInput), 400)
    }
    
    @Test
    fun test2() {
        assertEquals(part2(listOf("+1", "-2", "+3", "+1")),  2)
        assertEquals(part2(listOf("+1", "-1")), 0)
        assertEquals(part2(listOf("+3", "+3", "+4", "-2", "-4")), 10)
        assertEquals(part2(listOf("-6", "+3", "+8", "+5", "-6")), 5)
        assertEquals(part2(listOf("+7", "+7", "-2", "-7", "-4")), 14)
        val myInput = getMyInput()
        assertEquals(part2(myInput), 232)

    }

    private fun getMyInput(): List<String> {
        val path = "../data/day01_input.txt"
        return File(path).useLines { it.toList() }
    }
}
