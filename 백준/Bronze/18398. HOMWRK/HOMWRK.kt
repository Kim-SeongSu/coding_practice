import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)
    val T = sc.nextInt()

    for (i in 1..T) {
        val N = sc.nextInt()
        for (j in 1..N) {
            val a = sc.nextInt()
            val b = sc.nextInt()
            println("${a+b} ${a*b}")
        }
    }
    sc.close()
}