package main

import (
  "crypto/md5"
  "fmt"
  "bytes"
  "strconv"
)

func main() {
  var current int
  var b bytes.Buffer
  testSlice := make([]byte, 3, 3)
  current = 0
  for {
    current++
    bs := []byte(strconv.Itoa(current))
    b.Write([]byte("iwrupvqb"))
    b.Write(bs)
    helloHash := GetMD5Hash(b.String())
    if current % 100000 == 0 {
      fmt.Printf("Current %s\n", b.String())
      fmt.Printf("Hash is %x\n", helloHash)
    }
    if bytes.HasPrefix(helloHash, testSlice) {
      fmt.Printf("FOUND %x", helloHash)
      fmt.Printf("Current %s\n", b.String())
      break
    }
    b.Reset()
  }
}

func GetMD5Hash(text string) []byte {
  hasher := md5.New()
  hasher.Write([]byte(text))
  return hasher.Sum(nil)
}

