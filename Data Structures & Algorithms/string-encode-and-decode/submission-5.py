class Solution:

    def __init__(self):
        self.delimiter = ':;'

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += string
            result += self.delimiter
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        stack = deque()
        result = []
        for char in s:
            stack.append(char)
            self.append_current(stack, self.delimiter, result)
        return result
    
    def append_current(self, stack, delimiter, result):
        if len(stack) >= len(self.delimiter):
                # check if delimiter
                if stack[-2] + stack[-1] == self.delimiter:
                    stack.pop()
                    stack.pop()
                    stack_len = len(stack)
                    temp = ''
                    for char in range(stack_len):
                        temp += stack.pop()
                    result.append(temp[::-1])
