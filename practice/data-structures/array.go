package datastructures

import (
	"errors"
	"fmt"
)

// IntArray -> an int array
type IntArray struct {
	Arr      []int
	len      int
	capacity int
}

// NewIntArray -> create a new int array with capacity
func NewIntArray(capacity int) (*IntArray, error) {
	if capacity < 0 {
		return nil, fmt.Errorf("Illegal Capacity: %d", capacity)
	}
	return &IntArray{Arr: make([]int, capacity), len: 0, capacity: capacity}, nil
}

// Size -> get the array size
func (arr IntArray) Size() int {
	return arr.len
}

// IsEmpty -> find out the array is empty or not
func (arr IntArray) IsEmpty() bool {
	return arr.len == 0
}

// GetValue -> get the array value from index
func (arr IntArray) GetValue(index int) (int, error) {
	if (arr.len - 1) < index {
		return arr.Arr[index], nil
	}
	return 0, errors.New("The index out of range")
}

// Append -> add value to the array
func (arr IntArray) Append(val int) {
	if (arr.len + 1) >= arr.capacity {
		if arr.capacity == 0 {
			arr.capacity = 1
		} else {
			arr.capacity *= 2
		}
		newArray := make([]int, arr.capacity)
		copy(newArray, arr.Arr)
		arr.Arr = newArray
	}
	arr.Arr[arr.len+1] = val
	arr.len++
}

// Pop -> remove last int from the array
func (arr IntArray) Pop() (int, error) {
	if arr.len > 0 {
		arr.len--
		val := arr.Arr[arr.len]
		arr.Arr[arr.len] = 0
		return val, nil
	}
	return 0, errors.New("The array is already empty")
}
