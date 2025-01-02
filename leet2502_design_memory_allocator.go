type Allocator struct {
    memory []int
}


func Constructor(n int) Allocator {
    return Allocator {
        memory: make([]int, n),
    }
}


func (this *Allocator) Allocate(size int, mID int) int {
    count, start := 0, 0
    for i := 0; i < len(this.memory); i++ {
        if this.memory[i] == 0  {
            count++
            if count == size {
                for j := 0; j < size; j++ {
                    this.memory[j + start] = mID
                }
                return start
            }
        } else {
            start = i + 1
            count = 0
        }
    }   
    return -1
}


func (this *Allocator) FreeMemory(mID int) int {
    count := 0
    for i := 0; i < len(this.memory); i++ {
        if this.memory[i] == mID {
            this.memory[i] = 0
            count++
        }
    }
    return count
}


/**
 * Your Allocator object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Allocate(size,mID);
 * param_2 := obj.FreeMemory(mID);
 */