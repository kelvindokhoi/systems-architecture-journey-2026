### Error Interface in Go

Go programs express errrors using the `error` interface, which is a built-in interface type.
```go
type error interface {
    Error() string
}
```

When sth go wrong in a function, it returns an error value as the last return value.
Any code that calls a function that can return an error should check the error value whether it is `nil` or not.


### 1. Creating Custom Errors
You can create custom error types by implementing the `Error()` method.
Example:
```go
type userError struct {
    name string
}

func (e userError) Error() string {
    return fmt.Sprintf("%v has a problem with their account", e.name)
}
```
It can then be used as an error:
```go
func sendSMS(msg, userName string) error {
    if !canSendToUser(userName) {
        return userError{name: userName}
    }
    ...
}
```
The underlying type of the error is `userError`, but it is returned as the `error` interface type.

### 2. Using the `errors` Package
The standard library provides the `errors` package to create simple error values.
Example:
```go
import "errors"
var err error = errors.New("something went wrong")
```
You can also wrap errors with additional context using `fmt.Errorf`.
Example:
```go
import "fmt"
var err error = fmt.Errorf("failed to send message: %w", err)
```
Aside from `Errorf`, the `fmt` package provides other functions that work with errors, such as `Println` and `Printf`.

### 3. Panic and Recover
There's a dangerous way to handle errors, which is to use `panic`. When a function call `panic`, the program crashes and prints a stack trace.
As a general rule, do not use `panic`!
Example:
```go
func divide(a, b int) int {
    if b == 0 {
        panic("division by zero")
    }
    return a / b
}
```
The `panic` function will yeets control out of the current function and up the call stack until it reaches a function that [`defers a recover`](https://go.dev/blog/defer-panic-and-recover). If no function call `recover`, the goroutine, often the whole program, crashes.

Example of `recover`:
```go
func enrichUser(userID string) User {
    user, err := getUser(userID)
    if err != nil {
        panic(err)
    }
    return user
}

func main() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("recovered from panic:", r)
        }
    }()

    // this panics, but the defer/recover block catches it
    // a truly astonishingly bad way to handle errors. Comparable to the speed of a try/catch block of Python in competitive programming.
    enrichUser("123")
}
```
As a rule of thumb, don't use `panic`, instead, return error values and handle them gracefully. If you truely have unrecoverable errors, use [`log.Fatal`](https://golang.org/pkg/log/#Fatal) to print a message and exit the program.
