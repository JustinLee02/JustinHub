package com.example.section2

fun main() {
    println("Hello world")

    val a = 3 // immutable
    var b = 5 // mutable
    b = 7

    var c: Byte = 120 // Byte가 있음. 127 까지
    var d = 3.14f // f를 뒤에 써줘야 float로 인식
    var e: UShort = 35000u // u를 뒤에 써줘야 unsigned short로 인식
    var f: Char = '\u00AE' // Unicode로 특별한 문자를 사용 가능
    println(f)
}