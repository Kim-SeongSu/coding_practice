import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()

    for (i in 1..n) {
        val x = sc.nextInt()
        if (x % 2 == 0) {
            println("$x is even")
        } else {
            println("$x is odd")
        }
    }
    
    sc.close()
}