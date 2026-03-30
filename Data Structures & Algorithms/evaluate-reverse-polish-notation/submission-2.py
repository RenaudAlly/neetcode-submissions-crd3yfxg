class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Evaluating expression
        def evaluteExpression(operator, a, b):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == '*':
                return a * b
            else: # Assuming only 4 possible operators
                return (int(a / b))
        
        stack = []

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                operand_b = stack.pop()
                operand_a = stack.pop()
                result = evaluteExpression(token, int(operand_a), int(operand_b))
                stack.append(result)
        
        return stack[-1]