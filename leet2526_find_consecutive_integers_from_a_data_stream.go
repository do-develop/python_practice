type DataStream struct {
    value int
    needRepeat int
    currRepeat int
}


func Constructor(value int, k int) DataStream {
    return DataStream {
        value: value,
        needRepeat: k,
        currRepeat: 0,
    }
}


func (this *DataStream) Consec(num int) bool {
    if num == this.value {
        this.currRepeat++
        return this.currRepeat >= this.needRepeat
    }
    this.currRepeat = 0
    return false
}


/**
 * Your DataStream object will be instantiated and called as such:
 * obj := Constructor(value, k);
 * param_1 := obj.Consec(num);
 */