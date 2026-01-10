# Conditionals in Go

## Key notes
Unlike other languages, you must put the opening brace on the same line as the condition and not on a new line.

### 1. If Statement
```go
if condition {
    // code to execute if condition is true
} else if anotherCondition {
    // code to execute if anotherCondition is true
} else {
    // code to execute if none of the above conditions are true
}
```
The `elif` keyword is written as `else if` in Go.

### 2. Initial Statement of an If Block
```go
if err := doSomething(); err != nil {
    // handle error
}
```
The initial statement (`err := doSomething()`) is executed before evaluating the condition (`err != nil`). The scope of `err` is limited to the if block.
Having multiple statements in the initial statement is not allowed.

Why would I use this?
1. It's a bit shorter
2. It limits the scope of the initialized variable(s) to the if block

For example, instead of writing:
```go
length := getLength(email)
if length < 1 {
    fmt.Println("Email is invalid")
}
```
We can do:
```go
if length := getLength(email); length < 1 {
    fmt.Println("Email is invalid")
}
```

### 3. Switch Statement
```go
switch variable {
case value1:
    // code to execute if variable == value1
case value2:
    // code to execute if variable == value2
default:
    // code to execute if variable doesn't match any case
}
```
Example:
```go
func getCreator(os string) string {
    var creator string
    switch os {
    case "linux":
        creator = "Linus Torvalds"
    case "windows":
        creator = "Bill Gates"
    case "mac":
        creator = "A Steve"
    default:
        creator = "Unknown"
    }
    return creator
}
```
Notice that in Go, the `break` statement is not required at the end of a `case` to stop it from falling through to the next `case`. The `break` statement is implicit in Go.
If you do want a `case` to fall through to the next `case`, you can use the `fallthrough` keyword.
Example:
```go
func getCreator(os string) string {
    var creator string
    switch os {
    case "linux":
        creator = "Linus Torvalds"
    case "windows":
        creator = "Bill Gates"

    // all three of these cases will set creator to "A Steve"
    case "macOS":
        fallthrough
    case "Mac OS X":
        fallthrough
    case "mac":
        creator = "A Steve"

    default:
        creator = "Unknown"
    }
    return creator
}
```