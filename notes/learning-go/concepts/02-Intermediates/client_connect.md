# Server-Client In Go

```go
package main

import (
	"fmt"
	"io"
	"net/http"
	"encoding/json"
)

func getIPAddress(domain string) (string, error) {
	url := fmt.Sprintf("https://1.1.1.1/dns-query?name=%s&type=A", domain)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "", fmt.Errorf("error creating request: %w", err)
	}
	req.Header.Set("accept", "application/dns-json")

	client := http.Client{}
	res, err := client.Do(req)
	if err != nil {
		return "", fmt.Errorf("error sending request: %w", err)
	}
	defer res.Body.Close()

	body, err := io.ReadAll(res.Body)
	if err != nil {
		return "", fmt.Errorf("error reading response body: %w", err)
	}

	var dnsRes DNSResponse
	err = json.Unmarshal(body,&dnsRes)
	if err != nil{
		return "",err
	}
	if len(dnsRes.Answer)==0{
		return "",nil
	}
	return dnsRes.Answer[0].Data, nil
}
```
Step by step:

    Made the HTTP request and read the body

    ```go
    res, err := client.Do(req)
    body, err := io.ReadAll(res.Body)
    ```

    This gives us the response as a []byte of JSON, but it’s still just text.

    Defined a Go struct (DNSResponse) that matches the JSON

    That struct (in dns.go) has fields like Answer []Answer, and Answer has a Data string field that holds the IP address.

    Unmarshaled the JSON into that struct

    ```go
    var dnsRes DNSResponse
    err = json.Unmarshal(body, &dnsRes)
    ```

    json.Unmarshal parses the JSON bytes and fills in dnsRes, so we can work with normal Go fields instead of manually parsing strings.

    Checked that we actually got at least one answer

    ```go
    if len(dnsRes.Answer) == 0 {
        return "", nil // (this should ideally return an error)
    }
    ```

    If there’s no answer, there’s no IP to return.

    Returned the first IP address

    ```go
    return dnsRes.Answer[0].Data, nil
    ```

    Data is the IP address string for that DNS answer, and the tests only need the first one.
