## Go Programming language : 
- Statically typed language :
    - you have to declare type explicitly, or the have to be inferred
    ```go
    var myVariable = "myString"
    var myvariable string
    ```
- Strongly Type language :
    - operation you can perform on a varible depend on its type
    - for exemple we can't add int and string like in javascript
- Go is compiled:
    - go come with a compiler
    - translate the code into a machine code (binary)
    - in contrast with python (interpreter), is execute one line by one
    - most slower than execution of precompile execution go
- Fast Compile Time
    - we can go from the code to a runnable binary
    - make testing process fast and nice
- Built in Concurrency (goroutine)
- Simplicity (design philosophy) - garbage collection - concise syntax - do a lot with less code
- To check installation :
```bash
    go --version
```

### Modules
- a module is define as a collection of package(units that conatins files)
- a module is the unit that defines and manages a Go project’s dependencies, version, and packages.
- Think of it roughly like a Maven project in Java or a Python project with pyproject.toml / requirements.txt
- A module allows Go to know: "This directory is a Go project, and these are the external libraries it depends on."

### Packages
- folder that contains a collections of go files
- A package is a collection of Go source files.
- package user
- inside user/user.go

### Command 
```bash
    go mod init <module-name>
    # Create a new module
    go get <package>
    # Add/update a dependency.
    go mod tidy
    # Clean up go.mod and go.sum, adding missing dependencies and removing unused ones.
    go mod download
    # Download dependencies.
    go list -m all
    # go list -m all

    # after Init 
    go get ...
    go mod tidy
    go build
    go run .
```


### Initialise
- go mod init <module-name>
- It is used to create a new Go module in your project. 
- It mainly generates the go.mod file, which describes your module and its dependencies.
- The go.mod file then becomes the reference point for your Go project.
- <module-name> : It is the name/path of the module.
- exemple : **go mod init myapp**  or **go mod init github.com/benito/myapp** 


### Go.Mod
- go.mod is the identity card + dependency manifest of a Go project.
- The go.mod file mainly tells Go four important things:
    - the name/path of this module
    - versions of Go this module require
    - external dependencies this  project use
    - versions of those dependencies should be used
- Basic structure of go.mod : 
```go
    module example.com/myproject

    go 1.24
```
- Dependencies : 
```go
    import "github.com/gin-gonic/gin"
```
```bash
    go get github.com/gin-gonic/gin
```
```go
    module github.com/benito/myproject

    go 1.24

    require github.com/gin-gonic/gin v1.10.0
```
- Multiple dependencies :
```go
    module github.com/benito/myproject

    go 1.24

    require (
        github.com/gin-gonic/gin v1.10.0
        github.com/google/uuid v1.6.0
        github.com/stretchr/testify v1.9.0
    )
```
- go.sum :
    - Contains cryptographic checksums for module versions that Go has downloaded.
    - It helps Go verify that the downloaded dependency is the expected content.
    - "Are the downloaded dependencies exactly what they should be?"
- Indirect dependencies : 
    - // indirect means your project doesn't directly import that module, but one of your dependencies needs it.
    ```go
        require (
            github.com/gin-gonic/gin v1.10.0
            github.com/some/library v1.2.0 // indirect
        )
    ```
- go.mod can contain more directives :
    - module
    - go
    - require
    - replace
    - exclude
    ```go
        module github.com/benito/myproject

        go 1.24

        require (
            github.com/gin-gonic/gin v1.10.0
            github.com/google/uuid v1.6.0
        )

        require (
            github.com/some/dependency v1.2.0 // indirect
        )

        replace github.com/old/package => github.com/new/package v1.0.0
    ```


### First go file
- we first type package 
- we identify the package the file belong to by typing package <name_package> at the top of the file
- the package have to be the same for all files in the package
- package main is a special package name
- it tell the compiler to look to entry point here
- we then have to create a main function that is required for this package
- for a different package we don't have to create a function of the same name as the package
- to create a function we use func key word (func)
```go
package main
func main(){

}
```
- we will import the fmt package to print something on the console
```python
package main
import "fmt"

func main(){
    fmt.Println("Hello World !")
}
```
- to run program :
    ```python
    go build path/main.go
    go run path/main.go
    ```

### DataTypes
- Integer : int, int8, int16, int32, int64, uint, uint8, uint16, uint32, uint64
- largest number int16 : 32767
- when trying to add a value larger than that at affectation will render an error
- when it is after the assignation , it will do byte calculation giving negative value
- int8(-128, 127), uint(0, 255)
- Float : float32, float64
- String : string
- Boolean : bool
- rune
- error
- you can't perform operation with mixed type :
    - we can't :
    ```go
        var floatNum32 float32 = 10.1
        var intNum32 int32 = 2
        var result float32 = floatNum32 + intNum32
    ```
    - we can :
    ```go
        var floatNum32 float32 = 10.1
        var intNum32 int32 = 2
        var result float32 = floatNum32 + float32(intNum32)
    ```
- integer division result in integer
- default value for int and flaot and rune is 0
- default for string is '' and bool is false
- default error is nil
- we are not obliged to declare variable it with a value, it will be set to default value 
```go
var intNum3 int
```
- we can infered the type and not write it
```go
    var mytext = "text"
    mytext:="text"
```
- we an also do multiple declaration
```go
    var var1, var2 int = 1,2
```
- it is recommand to specify the type when the type is not obvious
- Constant are alternative to variable
- evry things that we said for variables is same except that we can't change the value
- len(string) give us the number of bytes and not the numbers of string


### Functions
- we use func to define structure
- we can define a parameters in that function
- to return a value we have to specify the type it is returning
- we can return many value
```go
func intDivision(numerator int, denominator int) int {
    var result int = numerator/denominator
    return result
}
func intDivision(numerator int, denominator int) (int,int) {
    var result int = numerator/denominator
    var remainder int = numerator%denominator
    return result, remainder
}
```
- with printf we can format string a bit easier than with println
- handle error:
```go
import(
    "errors"
    "fmt"
)
var err error 
if denominator == 0 {
    err = errors.New("Cannot divided By Zero")
    return err
}

```
- checking error and returning error with other varible is a general design pattern

### If else Switch 


### Arrays
- fixed lenght collection of data
- all the same type
- Indexable
- contiguous memory
```go
var intArr [3]int32
intArr[1]=123
fmt.println(intArr[0])
fmt.println(intArr[1,3])
```
- this array has only three elements
- int32 is four bytes of memeory, go allocate 12 bytes of contiguous memory when we initialise the array
- we can have memory location of each elements
```go
fmt.println(&intArr[0])
fmt.println(&intArr[1])
fmt.println(&intArr[2])

```
- we can also initialise and affecting a value using this syntax 
- in that situation , it can also infered the number of element in the table
```go
    var intArr [3]int32 = [3]int32{1,2,3}
    intArr := [3]int32{1,2,3}
    intArr := [...]int32{1,2,3}
    fmt.Println(intArr)
```

### Slices
- wrappers arounds arrays
- slices wraps arrays to give a more general and poweful and convenient interface to sequences of data
- by ommiting the lenght value we now have the slices
- when we use append we add a value at the end of array
```go
func main(){
    intArr := [...]int32{1,2,3}
    fmt.Println(intArr)

    var intSlice []int32 =[]int32{3,2,4}
    fmt.Println(intSlice)
    intSlice = append(intSlice, 7)
}
```
- when we call append , if we are over the initial capacity of intSlice a new array is create where the capacity increase
- the new array (intSlice is at a total different location than the previous inSlice)
- note that the new lenght is different from the capacity
- we can also append multiple value to the slice using spread operator : 
```go
var intSlice []int32 = []int32{9,8}
intSlice = append(intSlice, intSlice2...)
fmt.println(intSlice)
```
- to create a slice we can also use make function
- we specify type, lengnt and capacity
- by default lenght == capacity
```go
var intSlice []int32 = make(int32, 3,5)
```
- defining large number for capacity avoid reallocation
- this can have direct impacton performance

### Maps
- Map is a set of key - value pair
- we can create a map using make function
```go
    var myMap map[string]uint8 = make(map[string]uint8)
    // we can innitialise a map
    var myMap2 = map[string]uint8{"adam":23,"sarah":45}
```
- if i tried to get value of a map that not exist , we will get default value of that type
- in this case map return the default value of the type of value element of map
- for exemple : 
```go
    // John key don't exist
    // here we will have 0 as value
    fmt.Println(myMap2["john"]) // it will print 0, default value of uint8
```
- Map always return something even if key doesn't exist
- Map also return an optional second value which is boolean
```go
    var age,ok = myMap2["Jason"]
    // if ok then "jason" exist
    // if not ok then "json don't exist"
    delete(myMap2, "Jason")
```
- they return false when key don't exist
- delete remove a reference and don't return anything
- 


### Looping controls
- if we want to iterate over something :
```go
    for name := range myMap2{
        fmt.Printf("Name : %v\n",name)
    }
    for name, age := range myMap2{
        fmt.Printf("Name : %v Age : %v\n",name, age)
    }
    for i, v := range myMap2{
        fmt.Printf("Index :%v Value: %v", i, v)
    }
    for i:=0; i<10, i++ {
        fmt.PrintLn(i)
    }
```
- i++ ( increment by one)
- i-- ( decrement by one)
- i+=10 increment by ten
- i-=10 decrement by ten
- i*=10 multiply by ten
- i/=10 divide by ten
- we can stop loops with break

### String
- "é" is part of Non - ASCII caracters
- when you print an element of the string you will get a number , that will be unsigned Int 8 ( how go represent charachter)
- we can print value and type of an element using  Printf, %v, %f
- for exemple : 
```go
    fmt.Printf("%v %T", indexed, indexed)
```
- They can be indexed like array
- **UFT-8 Encoding :**
    - this is how go represent string on your computer
    - of type uint8
    - to represent extend set of character( emoji, chinese characters)
    - we will use more bytes 
    - ASCII caracters is (7 bytes) (128 chars)
    - we will use UTF-32 (32 bytes) but it have a lot of unused caraters
    - so we will use variable lenght encoding allowing by Utf-8
    - for that utf8 use a predefined encoding pattern
    - it encode informations abouts how many bytes a character uses
    - for exemple it use one byte if it start with 0, two byte if it start with 110
    - when we have special character, some following element of arry will store part of bytes of this elements
    - when you are dealing with string in go, you are dealing with an array that have an undelying representation of bytes
    - taking the lenght of an string give you the number of bytes
    - if you want to interact with string like getting index of letters or itereting or indexing
    - you have to cast it in Runes rather than dealing with byte array of string
    ```go
        var mystring = []rune("résumé")
    ```
    - Runes are unicode number that represent characters
    - Runes are an alias for int32, we will still have number representation but it will be easier to deal with
    - we can declare rune type using single quotes
    - string are imutable in go (cannot be modified when created)
    - we can concatenate string using + symbol
    ```go
        var strSlice = []string{'s', 'j'}
        var catStr = ""
        for i:= range strSlice{
            catStr += strSlice[i]
        }
    ```
    - like string are immutable, this concatenation create for each loop a new string which is pretty inneficient
    - to make it more fast we can import  string package and use stringBuilders
    ```go
        import (
            "fmt"
            "strings"
        )
        var strSlice = []string{'s', 'j'}
        var strBuilder strings.Builder
        for i:= range strSlice{
            strBuilder.writeString( strSlice[i])
        }
        var catStr = strBuilder.String()
    ```

- when we interact directly with string we interact with bytes representation
- when we want to directly interact with elements of the string like lenght or it value, we use Rune


### Structs
- a way to create your own type
- we have type keyword, then name of the struct and then struct keyword
- struct can hosted mixed types in forms of fields, we can define by name
```go
    type gazEngine struct{
        mpg uint8
        gallons uint8
    }
    func main(){
        // default value
        var myEngine gazEngine
        var myEngine2 gazEngine = gazEngine{mpg:25, gallons:8}
    }
```
- when we just define myEngine, default value are default value of the fields
```go
    myEngine{
        mpg: 0
        gallons: 0
    }
```
- one way to set these fields is to use struct litteral syntax like below
- we can also ommit the fields name like below
- w can also set the value by name direcly like below
```go
    var myEngine2 gazEngine = gazEngine{mpg:25,gallons:8}
    var myEngine3 gazEngine = gazEngine{25,8}
    myEngine2.mpg = 20
```
- the structs can be any thing you want even another struct
```go
    type gazEngine struct{
        mpg uint8
        gallons uint8
        ownerInfo owner
    }
    type owner struct{
        name string 
    }
    func main(){
        var myEngine gazEngine = gazEngine{mpg:25, gallons:8, ownerInfo:owner{name:"junior"}}
        fmt.Println(myEngine.mpg, myEngine.gallons, mEngine.ownerInfo.name )
    }
```
- instead of adding owner under gazengine, we can direcly add owner and any type like that :
    - we can use sub field directly
    ```go
        type gazEngine struct{
            mpg uint8
            gallons uint8
            owner
            int
        }
        ...
        fmt.Println(myEngine.mpg, myEngine.gallons, mEngine.name )

    ```
### Anonymous structs
- have to be define and initialised in the same location
- can be used once, not reusable
- if i want to create another struct like this i have to rewrite definition
```go
var myEngine = struct{
    mpg uint8
    gallons uint8
}{25,25}

```

### Structs Methods
- struct have concept of methods,
- there are functions that are tied to struct and cand directly have access to struct instances itself
- except the struct part methods are just like functions
- we assign the method to the struct (e gazEngine)
- this function have now acess to the fields of a struct
```go
    package main
    import "fmt"
    type gazEngine struct{
        mpg uint8
        gallons uint8
    }
    func (e gazEngine) milesLeft() uint8{
        return e.gallons * e.mpg
    }
    func canMakeIt(e gazEngine, miles uint8){
        if miles <= e.milesLeft(){
            fmt.Println("You can make it there !")
        }else{
            fmt.Println("You need to fuel it up ! ")
        }
    }
```

### Interfaces
- interface help to handle the same way function that has the same signature
- help handle in a general way function
```go
    type engine interface{
        milesLeft() uint8
    }
```
```go
    package main
    import "fmt"
    type gazEngine struct{
        mpg uint8
        gallons uint8
    }
    type electricEngine struct{
        mpkwh uint8
        kwh uint8
    }
    type engine interface{
        milesLeft()
    }
    func (e gazEngine) milesLeft() uint8{
        return e.gallons * e.mpg
    }
    func (e electricEngine) milesLeft() uint8{
        return e.mpkwh * e.kwh
    }
    func canMakeIt(e engine, miles uint8){
        if miles <= e.milesLeft(){
            fmt.Println("You can make it there !")
        }else{
            fmt.Println("You need to fuel it up ! ")
        }
    }

```

### Pointers
- pointers are specials types
- these variables store memoy location
- to create a pointer we use * syntaxt
```go
    var p *int32
    var i int32
```
- this line state that p will hold the memory adress of an int32 value
- default valure of int32 is 0 while default value of p(an adress) will be nil
- p is going to store a pointer or a memory adress , which itself take up 32 or 64 bits depending on your os
- to give pointer an address we can use a built in new functions
```go
    var p *int32 = new(int32)
```
- it give us back a free memory location which is 32 bits wide  which p can use to store an int32 value
- p store a memory location that point to a place in the memory
- p = 0x1b0c
- they still have a lot in common with regular varibles
- they still have a memory adress themselves and they store a value(an adress) at that adress
- if we want to get the value stored at this memory location we can use the * symbol
```go
    fmt.Printf("The value p point to is : %v",*p)
``` 
- this is called dereferencing the pointers
- when you initialise a pointer with a memory location, its 0 , or default value(in function of type) at that location (0, "", false)
- to change the value store at that location we use * follow by affectation
```go
    *p = 10
```
- this line set the value at the memory location p is referencing to 10
- start (*) notation have double duty
- which may be a little confusing
    - here we use it to say to the compiler that we want to initialise the pointer
    ```go
        var p *int32 = new(int32)

    ```
    - here we use it to tell the compiler that we want to reference the value of the pointer
    ```go
        fmt.Printf("The value p point to is : %v",*p)
        *p = 10
    ```
    - we should keepin mind the two diferent roles
- Trying to get or set the value of null( nil) pointer
    - if we run with a null value , we will get a runtime error
    - we can get a value at a memory that does't exist

- We can also create a pointer from the adress of another variable
    - using the ampersand symbol
    - like this :
    ```go
        p = &i
    ```
    - ampersand mean we want memory adress of the variable not its values
    - if we change the value of p using star notaton , i value is also change
    - this is different when you are using variable
    - when you create a new varible k, and do k = i, your program will copy the value of i at the memory location of i
    - the main exception of this behavior is slice
    - if we copy a slice in regular way without calling a pointer
    - if we modify the slice copy value, the original slice value will change
    - under the hood slice contains pointers to an underlying array
    - by coping slices we copy pointers that refers to same data

- Pointers in functions
    - when we want to apply a function to an array it apply to each element of array and send back an second array
    - we use more memory than we need
    - with pointer we can modify directly at array location, we mo
    - the function take the pointer to an array
    - pointer are very useful when passing large parameters so you don't have to creat copy of this parameters
    

### Goroutines
- Go routines are way to launch multiple functions and have them execute concurrently
- Concurency is not the same as parrallel executions
- Concurency mean we have multiple task in progess at the same time
- one way to d this is jumping back and working from one task tio another
- parallele execution mean, mutliple executions is hapening simultaneisly
- if we add **go** key word to the function we want to execute concurently 
- now the programm wont wait the function to complete, it will go to next step of the loop
- now if we just do that we will see that nothing happen
- the programm spawned the task in the background and did'nt wait for them to complete
- so we need our program to wait until all task have been completed
- We will use **Wait.group**
- can be imported through sync package
- wait.group are counter
- whenever we spaned a go routine, we make sure we add a counter
- and inside the function we call the done method , it will decrement the function
- finally at the end we call the end methods
- the wait functiongonna wait the functio to go back to zero
- Meaning that all the function is completed and the rest of he code will executed

- Now lets says we want to retrieve results  from dbcalls in the main functions
- we create a slice call result 
- we will add result into each goroutine dbcalls
- it will lead to having many function modifing the same memory adress at the same time
- It could lead to corrupt memory
- we can use a mutex to control the writing to our slice in a way that make it safe
- we can create a mutex from a sync package
- the two main methods are lock and unlock methods
- this is sort of mutual exclusion
- we will place them in the code tha try to access the result
- It really matters where you put your lock and unlock statements
- if you put it too early, it will detroy the concurency of the code

- one drawback of this mutext is that it completly block other go routines from accessing our result slice
- There are another type of Mutex call read , write mutex(Read lock, Read Unlock) 
- this pattern allow multiples go routines to read at the same time, only blocking when writing is happening

- when the function we call in the go routines is not computationally expensive, the duration af execution of all he task correspond to the duration of execution of one task, the cpu can move on to start the next go routine easily
- go is natively parallelize in function of number of cores in cpi
- when we have a lot of computationally expensive task , the parformance we get is going to be limited by the numbers of core
- if i have eight core on my machine , i will run eight of thos computationally expensive task
- the rest of go routines need to wait an availaible cpu

- when the functin in go routines are expensives , the amont of improvement you will get is a function o the number of cores in the cpu

```go
    package main
    import (
        "fmt"
        "math/rand"
        "time"
        "sync"
    )
    var wg = sync.WaitGroup{}
    var dbData = []string{"id1", "id2", "id3", "id4", "id5"}
    var results = []string{}
    var m = sync.Mutex()
    func main(){
        t0 := time.Now()
        for i :=0; i<len(dbData); i++ {
            wg.add(1)
            go dbCall(i)
        }
        wg.wait()
        fmt.Printf("\n Total execution Time :%v", time.Since(t0))
        fmt.Printf("\n The results are %v", results)
    }
    func dbCall(i int){
        var delay flaot32 = rand.Flaot32()*2000
        time.sleep(time.Duration(delay)*time.Millisecond)

        save(dbData[i])
        log()
        wg.done()
    }
    func save(result string){
        m.Lock()
        results = append(results, result)
        m.Unlock()
    }
    func log(){
        m.Rlock()
        fmt.Println("The result from the Database is :",dbData[i])
        m.Runlock()

    }
```

### Channels
- Channels are the way go routines pass around informations
- Main featues :
    - they holds data (integer, slice, anythings)
    - they threads safe ( we avoids data races when we are reading and writing from memory)
    - listen for data ( wa can listen when data is add or remove from channels, or we can block code execution until one of this event happens)
- to make a channel we use **make** function and **chan** key words folloed by type
- we use an arrow to add a value to a channel
- we can think to a channel as containing an undelying array
- In this case we have what call an unbeffered channels which has enough room for one value
- we can retrieve the value from the channels using similar syntax and set that to a variable
- the value will get popped out from the channel

- we will get an unbefferd error
- when writing to an unbefferd channel, the code will, block into another thing reading from it
- we will be waiting and unable to reach the line where we read from channel
- channels are mean to be use in conjuction with goroutines
- we can direcly print out the varible in the channels rather than put it in a varibale 
- when we the program arrive at go routine, it move to the next function

- now what happen if we add multiple value in the channel using a for loop
- we can iterate over the channel itself by using range keyword
- we have to close the channel to notify any other process using this channel that we are done
- and our main function will break out the loop and exit
- for that we can use a defer statement , in go it say to a function to do something right before the function exit

- Buffered channels are similar to channels , except that we can store multiple value at the same time
- we can create a buffered channels that store 5 eLements
- the process function stay active until main function is done with the channels
- there no need fo that , process can exit and let main function continue
- by using a buffered of 5, the process function can add up to five valuesin the channels without having to wait for the main function to make a room in the channel by popping out a value
- running like this we see that process function finish immediatly
```go
    package main
    func main() {
        var c = make(chan int)
        var buff_c = make(chan int,5)
        go process(c)
        for i:= range c{
            fmt.Println(i)
        }
        fmt.Println(<-c)
    }
    func process(c chan int){
        defer close(c)
        for i=0; i<10; i++ {
            c<-i
        }
    }
```
- make a more realistic program and see how channels are actually useful
    - a program that mock checking on chiken fingers at walmart, costco and wholefood
    - if it find a sale it alert me
    ```go
        package main
        import (
            "fmt"
            "math/rand"
            "time"
        )
        const MAX_CHIKEN_PRICE float32 = 5
        const MAX_TOFU_PRICE float32 = 3

        func main(){
            var chikenChannel = make(chan string)
            var tofuChannel = make(chan string)
            var websites = []string("walmart.com", "costo.com", "wholefoods.com")
            for i := range websites {
                go checkChikenPrices(websites[i], chikenChannel)
                go checkTofuPrices(websites[i], tofuChannel)
            }
            sendMessage(chikenChannel, tofuChannel)
        }
        func checkTofuPrices(websites string, tofuChannel chan string ){
            for {
                time.Sleep(time.Second*1)
                var tofuPrice = rand.Float32()*20
                if tofuPrice <= MAX_TOFU_PRICE{
                    tofuChannel <- website
                    break
                }
            }
        }

        func checkChikenPrices(websites string, chickenChannel chan string ){
            for {
                time.Sleep(time.Second*1)
                var chickenPrice = rand.Float32()*20
                if chickenPrice <= MAX_CHICKEN_PRICE{
                    chickenChannel <- website
                    break
                }
            }
        }
        func sendMessage(chikenChannel chan string, tofuChannel chan string){
            select{
                case website := <- chickenChannel:
                    fmt.Printf("\n Found a deal on chiken at %s", chikenChannel)
                case website := <- tofuChannel:
                    fmt.Printf("\n Found a deal on Tofu at %s", tofuChannel)

            }
        }
    ```


### Generics
- Generics in Go are a feature that allows you to write functions, structures, and interfaces using placeholder types instead of specific, hardcoded data types.
- Generics make your code significantly more reusable, flexible, and clean without forcing you to sacrifice compile-time type safety.
- generics sum slice function
- this is a way for accepting additionals parametters
```go
    package main
    import "fmt"

    func main(){
        var intSlice = []int{1, 2, 3}
        fmt.Println(sumSlice[int](intSlice))

        var float32Slice = []float32{1,2,3}
        fmt.Println(sumSlice[float32](float32Slice))
    }
    func sumSlice[T int | float32 | float64](slice []T) T {
        var sum T
        for _, v := range slice{
            sum += v
        }
        return sum
    }
```
- we also have **any** type that we can use in certain conditions
- we can't for exemple use it in our function to allow all variable types
- not all type are compatible with additional operator
- type of generic parameter can be inffered thought type of varible we pass in
- there are type where generic parameters types can't be inferred
- for exemple when we load a json and unmarshaling it into a struct
- in this case we need to pass the struct to the generic function other wise our function won't know what struct to pass or json to

### An API 
- 