# Type Assertion in Go

We can check if something stored in an interface is of a specific type using type assertion.
Example:
```go
func getExpenseReport(e expense) (string, float64) {
	c, ok := e.(email)
	if ok {
		return c.toAddress,c.cost()
	}
	d, dok := e.(sms)
	if dok {
		return d.toPhoneNumber,d.cost()
	}
	return "",0.0
}
```
In this example, we check if the `expense` interface `e` is of type `email` or `sms` using type assertion. The `ok` and `dok` variables indicate whether the assertion was successful.