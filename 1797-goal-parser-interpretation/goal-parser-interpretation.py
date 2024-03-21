class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")

    #     s=""
    #     for i in range(len(command)):
    #         if command[i]=="G":
    #             s+=command[i]
    #         if command[i]=="(":
    #             if command[i+1]==")":
    #                 s+="o"
    #             else:
    #                 s+="al"
    #     return s
