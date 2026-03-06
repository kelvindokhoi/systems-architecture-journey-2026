package main 

import "fmt"

func main(){
	var num_people, dist int
	fmt.Scan(&num_people)
	fmt.Scan(&dist)
	fmt.Print((num_people-1)*dist)
}