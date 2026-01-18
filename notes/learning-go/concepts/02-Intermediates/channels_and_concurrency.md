# Channels and Concurrency in Go

### 1. How does concurrency work in Go?

Go was designed to be concurrent. It excels at performing many tasks simultaneously safely using simple syntax.

Concurrency in Go is as simple as using the `go` keyword when calling a function. This spawns a new goroutine, which is a lightweight thread managed by the Go runtime.
```go
go doSomething()
```

```go
func sendEmail(message string) {
	go func() {
		time.Sleep(time.Millisecond * 250)
		fmt.Printf("Email received: '%s'\n", message)
	}()
	fmt.Printf("Email sent: '%s'\n", message)
}
```
Here:
That func() is an anonymous function:
- `func` - defines a function without that takes no parameters
- `{...}` - its body
- `()` at the very end - calls it immediately
- `go` in front - spawns a new goroutine to run that function concurrently

### 2. Channels

Channels are a typed, [thread-safe](https://en.wikipedia.org/wiki/Thread_safety) queue. Channels allow different goroutines to communicate with each other.

1. ***Create a channel***:
Like map and slices, channels must be created before use:
```go
ch := make(chan int)
```

2. ***Send data to a channel***:
The <- operator is called the channel operator. Data flows in the direction of the arrow. This operation will [block](https://en.wikipedia.org/wiki/Blocking_(computing)) until another goroutine is ready to receive the value.
```go
ch <- 69
```

3. ***Receive data from a channel***:
```go
v := <-ch
```
This reads and removes a value from the channel and saves it into the variable `v`. This operation will block until there is a value in the channel to be read.

4. ***Reference Type***:
Like maps and slices, channels are reference types, meaning they are passed by reference by default.
```go
func send(ch chan int) {
    ch <- 99
}

func main() {
    ch := make(chan int)
    go send(ch)
    fmt.Println(<-ch) // 99
}
```

5. ***Blocking and Deadlocks***:
A [deadlock](https://yourbasic.org/golang/detect-deadlock/#:~:text=yourbasic.org%2Fgolang,look%20at%20this%20simple%20example.) is when a group of goroutines are all blocking so none of them can continue. This is a common bug that you need to watch out for in concurrent programming.