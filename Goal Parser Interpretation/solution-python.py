class Solution:
    def interpret(self, command: str) -> str:
        result = "";
        for i in range(len(command)):
            if command[i] == '(' and command[i + 1] == ')':
                result += 'o'
            elif command[i] != '(' and command[i] != ')':
                result += command[i]
        return result