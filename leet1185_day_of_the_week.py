class Solution:class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Sakamoto Algorithm
        # 1/1/1 is Monday. Put Monday at index 1 for easier modulus manipulation
        day_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # 0, 31%7 = 3, 3+(28%7)-1 = 2, 2+(31%7) = 5, 5+(30%7) = 0, 0+(31%7) = 3, 3+(30%7) = 5, 5+(31%7) = 1, 1+(31%7) = 4, 4+(30%7) = 6, 6+(31%7) = 2, 2+(30%7) = 4
        days_by_month_mod7 = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        # the current year should not be counted for the leap day calculation for the first two months
        if(month < 3): year = year - 1
        # Add year because non-leap years have 365 days, and 365 % 7 = 1
        return day_in_week[(year + (year//4 - year//100 + year//400) + days_by_month_mod7[month - 1] + day) % 7]
