class Solution:
    def maskPII(self, s: str) -> str:
        phone = "***-***-"
        mail = ""
        counter = 0
        if '@' not in s: # this is a phone number
            last_digit = ""
            idx = -1
            while len(last_digit) < 4:
                if s[idx].isnumeric():
                    last_digit += s[idx]
                idx -= 1
            for i in range(len(s)):
                if s[i].isnumeric():
                    counter += 1
            if counter == 10: # only local number
                return phone + last_digit[::-1]
            elif counter > 10:
                return '+' + ('*'*(counter-10)) + '-' + phone + last_digit[::-1]
        else: # this is an email address
            pos = s.index('@')
            mail += s[0]
            mail += "*****"
            mail += s[pos-1:len(s)]
            return mail.lower()
