# Http package in Go

The `net/http` package in Go provides HTTP client and server implementations. It is widely used for building web applications, RESTful APIs, and handling HTTP requests and responses.

### Client Code Example
```go
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

const usersUrl = "https://api.boot.dev/v1/courses_rest_api/learn-http/users"

func main() {
	users, err := getUserData(usersUrl)
	if err != nil {
		log.Fatalf("error getting user data: %v", err)
	}
	fmt.Println(string(users))
}

func getUserData(url string) ([]byte, error) {
	res, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("error making request: %w", err)
	}
	defer res.Body.Close()

	data, err := io.ReadAll(res.Body)
	if err != nil {
		return nil, fmt.Errorf("error reading response: %w", err)
	}

	return data, nil
}
```
- `http.Get` uses the `http.DefaultClient` to make a request to the given `url`
- `res` is the HTTP response that comes back from the server
- `defer res.Body.Close()` ensures that the response body is properly closed after reading. Not doing so can cause memory issues.
- `io.ReadAll` reads the response body into a slice of bytes `[]byte` called `data`