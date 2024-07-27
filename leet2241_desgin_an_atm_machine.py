class ATM:

    def __init__(self):
        self.have = [0, 0, 0, 0, 0]
        self.notes = {0:20, 1:50, 2:100, 3:200, 4:500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.have[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        N = len(self.have)
        ans = [0 for i in range(N)]

        k = N - 1
        while k >= 0 and amount > 0:
            note = self.notes[k]
            if amount >= note and self.have[k]:
                ans[k] = min(self.have[k], amount // note) 
                amount -= (note * ans[k])
            k -= 1 # next biggest note
        
        if amount == 0:
            for i in range(N):
                self.have[i] -= ans[i]
            return ans
        else:
            return [-1]
