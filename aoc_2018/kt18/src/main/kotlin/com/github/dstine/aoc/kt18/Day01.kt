package com.github.dstine.aoc.kt18

// added in Kotlin 1.3
import kotlin.sequences.sequence

fun part1(changes: List<String>): Int =
    changes.asSequence()
        .map { it.toInt() }
        .sum()

// https://stackoverflow.com/a/48007581
fun <T> Sequence<T>.repeat() = sequence { while (true) yieldAll(this@repeat) }

// find first repeated intermediate result for any number of passes
fun part2(changes: List<String>): Int {
    var result = 0
    val results = mutableSetOf(result)
    changes.asSequence()
        .map { it.toInt() }
        .repeat()
        .forEach {
            result += it
            if (result in results) {
                return result
            }
            results.add(result)
        }

    throw RuntimeException("should never get here")
}
