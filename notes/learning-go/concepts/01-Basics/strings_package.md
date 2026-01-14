# NOtes on functions of the strings package in Go

### 1. `strings.Contains`
The `strings.Contains` function checks if a substring is present within a string.
Use:
```go
strings.Contains(str, substr string) bool
```

### 2. ToLower and ToUpper
The `strings.ToLower` and `strings.ToUpper` functions convert a string to lowercase or uppercase respectively.
Use:
```go
strings.ToLower(s string) string
strings.ToUpper(s string) string
```

### 3. Fields
The `strings.Fields` function splits a string into substrings based on whitespace.
Use:
```go
strings.Fields(s string) []string
```

### 4. ReplaceAll
The `strings.ReplaceAll` function replaces all occurrences of a substring with another substring.
Use:
```go
func ReplaceAll(s, old, new string) string
```