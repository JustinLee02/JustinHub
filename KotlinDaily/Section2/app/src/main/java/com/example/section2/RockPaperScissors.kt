package com.example.section2

fun main() {
    var computerChoice = ""
    var playerChoice = ""

    println("Rock, Paper or Scissors?")
    playerChoice = readln()
    val random = (1..3).random() //1은 바위 2는 보 3은 가위
    if (playerChoice=="Rock") {
        if (random == 1) {
            println("ComputerChoice is Rock. Draw")
        } else if (random == 2) {
            println("ComputerChoice is Paper. Lose")
        } else println("ComputerChoice is Scissors. Win")
    } else if (playerChoice == "Paper") {
        if (random == 1) {
            println("ComputerChoice is Rock. Win")
        } else if (random == 2) {
            println("ComputerChoice is Paper. Draw")
        }
        else println("ComputerChoice is Scissors. Lose")
    } else {
        if (random == 1) {
            println("ComputerChoice is Rock. Lose")
        } else if (random == 2) {
            println("ComputerChoice is Paper. Win")
        }
        else println("ComputerChoice is Scissors. Draw")
    }

}