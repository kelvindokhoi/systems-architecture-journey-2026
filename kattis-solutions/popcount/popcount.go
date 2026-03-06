package main 

import (
	"fmt"
)

func main(){
	var kernel string
	fmt.Scan(&kernel)
	count := 0
	for i:=0;i<len(kernel);i++{
		if kernel[i]=='1'{
			count ++
		}
	}
	fmt.Print(count)
}