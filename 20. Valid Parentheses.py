class Solution:
    def isValid(self, s: str) -> bool:
        a_stack = []
        a_dict = { "(": ")", "{": "}", "[": "]" }

        for item in s:
            if item in a_dict:
                a_stack.append(item)
            elif item in a_dict.values():
                if not a_stack or a_dict[a_stack.pop()] != item:
                    return False

        return len(a_stack) == 0
