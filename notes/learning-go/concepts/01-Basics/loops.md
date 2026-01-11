# Loops in Go

### 1. For Loop
The basic for loop in Go adopts the C-style syntax:
```go
for INITIAL; CONDITION; AFTER{
  // do something
}
```
**`INITIAL`** is run once at the beginning of the loop and can create
variables within the scope of the loop.

**`CONDITION`** is checked before each iteration. If the condition doesn't pass
then the loop breaks.

**`AFTER`** is run after each iteration.

For example:
```go
for i := 0; i < 10; i++ {
  fmt.Println(i)
}
// Prints 0 through 9
```
We can omit sections of the loop. For example, to create a loop that runs forever, we omit the **`CONDITION`** (the middle) part.

### 2. While Loop
There is no `while` loop in Go. Instead, we can use a `for` loop without the **`INITIAL`** and **`AFTER`** sections to achieve the same effect.
Thus, a `for` loop that only has a `CONDITION`.
Like this:
```go
for CONDITION {
  // do some stuff while CONDITION is true
}
```

Example:
```go
plantHeight := 1
for plantHeight < 5 {
  fmt.Println("still growing! current height:", plantHeight)
  plantHeight++
}
fmt.Println("plant has grown to ", plantHeight, "inches")
```
Or we can omit everything to create an infinite loop:
```go
for {
  // do something forever
}
```

### 3. Loop Control Statements
Go provides `break` and `continue` statements to control loop execution. They work similar to how Python uses them.
- `break` exits the innermost loop immediately.
- `continue` skips the remaining code in the current iteration and moves to the next iteration of the loop.