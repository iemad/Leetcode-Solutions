class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_list = []
        for i in operations:
            if i == "C" and final_list:
                final_list.pop(len(final_list)-1)
            elif i == "D" and final_list:
                final_list.append(int(final_list[-1])*2)
            elif i == "+" and final_list:
                final_list.append(int(final_list[-1])+int(final_list[-2]))
            else:
                final_list.append(int(i))
        return sum(final_list)
