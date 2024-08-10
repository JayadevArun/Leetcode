class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = []
                while stack[-1] != '[':
                    substr.append(stack.pop())
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                rep = int(''.join(num[::-1]))
                dec = ''.join(substr[::-1])
                stack.append(rep*dec)
        return ''.join(stack)