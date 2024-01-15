class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # case - after midnight
        if logoutTime < loginTime:
            return self.numberOfRounds(loginTime, '24:00') + self.numberOfRounds('00:00', logoutTime)
        hs, ms = map(int, loginTime.split(':'))
        hf, mf = map(int, logoutTime.split(':'))

        start = hs * 60 + ms
        finish = hf * 60 + mf
        return max(0, finish // 15 - (start // 15 + (start % 15 != 0))) # case - start time can't make full 15min