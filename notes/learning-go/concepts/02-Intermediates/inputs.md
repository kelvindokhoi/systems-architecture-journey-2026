# Read inputs in Go (mostly for CP)

In Go, we can read inputs using various methods. For competitive programming (CP) and similar scenarios, we often use `bufio` and `os` packages for efficient input reading.
Here's a simple example of how to read inputs from standard input:

```go
package main
import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)
func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter numbers separated by space: ")
    input, _ := reader.ReadString('\n')
    input = strings.TrimSpace(input)
    strNumbers := strings.Split(input, " ")

    var numbers []int
    for _, strNum := range strNumbers {
        num, err := strconv.Atoi(strNum)
        if err != nil {
            fmt.Println("Error converting string to int:", err)
            return
        }
        numbers = append(numbers, num)
    }

    fmt.Println("You entered the numbers:", numbers)
}
```
In this example:
1. We import necessary packages: `bufio` for buffered I/O, `fmt` for formatted I/O, `os` for OS-level operations, `strconv` for string conversion, and `strings` for string manipulation.
2. We create a `bufio.Reader` to read from standard input.
3. We read a line of input using `ReadString('\n')`, which reads until a newline character.
4. We trim any extra whitespace and split the input string into individual number strings.
5. We convert each string to an integer using `strconv.Atoi` and store them in a slice.
6. Finally, we print the slice of numbers.

We can also use fmt package for simpler input reading, but it's less efficient for large inputs:
```go
var n int
fmt.Scan(&n) // Reads a single integer
var i,j int
fmt.Scan(&i, &j) // Reads two integers
fmt.Scanf("%d %d", &i, &j) // Reads two integers with formatted input
fmt.Scanln(&i, &j) // Reads two integers until newline
```