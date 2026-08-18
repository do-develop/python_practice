func maxProfit(prices []int, strategy []int, k int) int64 {
    N := len(prices)
    profitSum := make([]int64, N + 1)
    priceSum := make([]int64, N + 1)

    for i := 0; i < N; i++ {
        profitSum[i+1] = profitSum[i] + int64(prices[i])*int64(strategy[i])
		priceSum[i+1] = priceSum[i] + int64(prices[i])
    }

    mxProfit := profitSum[N]
    for i := k - 1; i < N; i++ {
        leftProfit := profitSum[i-k+1]
        rightProfit := profitSum[N] - profitSum[i+1]
        changeProfit := priceSum[i+1] - priceSum[i-k/2+1]
        mxProfit = max(mxProfit, leftProfit+changeProfit+rightProfit)
    }
    return mxProfit
}