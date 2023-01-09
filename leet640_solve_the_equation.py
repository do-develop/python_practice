class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate(expression):
            tokens = expression.replace('+', "#+").replace('-', "#-").split('#')
            result = [0] * 2 # two parts[terms, number]
            for token in tokens:
                if not token:
                    continue
                if token == "x" or token == "+x":
                    result[0] += 1
                elif token == "-x":
                    result[0] -= 1
                elif "x" in token:
                    result[0] += int(token[:token.index("x")])
                else:
                    result[1] += int(token)
            return result
        
        sides = equation.split("=")
        left = evaluate(sides[0])
        right = evaluate(sides[1])
        var = left[0] - right[0]
        num = right[1] - left[1]
        if var == 0 and num == 0:
            return "Infinite solutions"
        if var == 0:
            return "No solution"
        return "x={}".format(num // var)
