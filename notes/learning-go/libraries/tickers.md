# Tickers

- [time.Tick()](https://golang.org/pkg/time/#Tick) is a standard library function that returns a channel that sends a value on a given interval.
- [time.After()](https://golang.org/pkg/time/#After) sends a value once after the duration has passed.
- [time.Sleep()](https://golang.org/pkg/time/#Sleep) blocks the current goroutine for the specified duration of time.

The functions take a `time.Duration` as an argument. For example:
```go
time.Tick(500 * time.Millisecond)
```
If you don't add `time.Millisecond` (or another unit), it will default to nanoseconds. That's — taking a wild guess here — probably faster than you want it to be.