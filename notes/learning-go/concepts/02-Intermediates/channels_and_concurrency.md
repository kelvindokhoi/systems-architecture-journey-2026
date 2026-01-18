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

6. **Block channels**:
Sometimes we don't care what's passed through a channel. We only care when and if something is passed. In that situation, we can block and wait until something is sent on the channel using the folling syntax:
```go
<-ch
```
This will block until it pops a single item off the channel, then continue, discarding the item.

In cases like this, [Empty structs](https://dave.cheney.net/2014/03/25/the-empty-struct) are often used as a [unary](https://en.wikipedia.org/wiki/Unary_operation) value so that the sender communicates that this is only a "signal" and not some data that is meant to be captured and used by the receiver.

Here is an example:
```go
func downloadData() chan struct{} {
	downloadDoneCh := make(chan struct{})

	go func() {
		fmt.Println("Downloading data file...")
		time.Sleep(2 * time.Second) // simulate download time

		// after the download is done, send a "signal" to the channel
		downloadDoneCh <- struct{}{}
	}()

	return downloadDoneCh
}

func processData(downloadDoneCh chan struct{}) {
	// any code here can run normally
	fmt.Println("Preparing to process data...")

	// block until `downloadData` sends the signal that it's done
	<-downloadDoneCh

	// any code here can assume that data download is complete
	fmt.Println("Data download complete, starting data processing...")
}

processData(downloadData())
// Preparing to process data...
// Downloading data file...
// Data download complete, starting data processing...
```

7. **Buffered Channels**:

Channels can OPTIONALLY be buffered.

We can create a buffered channel with with a 2nd argument to `make`:
```go
ch := make(chan int, 100)
```

A buffer allows the channel to hold a fixed number of values before sending blocks. This means sending on a buffered channel only blocks when the buffer is full, and receiving blocks only when the buffer is empty.

8. **Closing Channels**:

Channels can be explicitly closed by a sender:
```go
ch := make(chan int)

// do some stuff with the channel

close(ch)
```

To check if a channel is closed:
Similar to the ok value when accessing data in a map, receivers can check the ok value when receiving from a channel to test if a channel was closed.
```go
v, ok := <-ch
```
ok is `false` if the channel is empty and closed.

**DON'T SEND ON A CLOSED CHANNEL**:
Sending on a closed channel will cause a panic.

Closing isn't necessary. There's nothing wrong with leaving channels open, they'll still be garbage collected if they're unused. You should close channels to indicate explicitly to a receiver that nothing else is going to come across.

9. **Range over Channels**:
Similar to slices and maps, channels can be ranged over.
```go
for item := range ch {
    // item is the next value received from the channel
}
```
This example will receive values over the channel (blocking at each iteration if nothing new is there) and will exit only when the channel is closed.

10. **Select Statement**:

Sometimes we have a single goroutine listening to multiple channels and want to process data in the order it comes through each channel.

A `select` statement is used to listen to multiple channels at the same time. It is similar to a `switch` statement but for channels.

```go
select {
case i, ok := <-chInts:
	if ok {
		fmt.Println(i)
	}
case s, ok := <-chStrings:
	if ok {
		fmt.Println(s)
	}
}
```
The first channel with a value ready to be received will fire and its body will execute. If multiple channels are ready at the same time one is chosen randomly. The ok variable in the example above refers to whether or not the channel has been closed by the sender yet.

11. **Default Case in Select**:
The `default` case in a `select` statement executes immediately if no other channel has a value ready. A `default` case stops the `select` statement from blocking.
```go
select {
case v := <-ch:
    // use v
default:
    // receiving from ch would block
    // so do something else
}
```

12. **Ignoring Channels**:
Sometimes you want to ignore a channel's value. You can do this by not binding it to a variable:
```go
select {
case <-ch:
    // event received; value ignored
default:
    // so do something else
}
```
Alternatively, you can use the blank identifier _ to ignore the value:
```go
select {
case _ = <-ch:
    // event received; value ignored
default:
    // so do something else
}
```