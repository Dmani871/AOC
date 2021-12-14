class InstructionSet:
    def __init__(self):
        self.horizontal_pos = 0
        self.depth = 0
    def exec_forward(self,units):
        self.horizontal_pos+=units
    def exec_down(self,units):
        self.depth+=units
    def exec_up(self,units):
        self.depth-=units

    def solve_for(self, name: str,units:int):
        do = f"exec_{name}"
        if hasattr(self, do) and callable(func := getattr(self, do)):
            func(units)

def parseInstructions():
    instructionsHandler=InstructionSet()
    with open("input.txt") as instructions:
        instructions=instructions.readlines()
        for instruction in instructions:
            cmd,units=instruction.split(sep=" ")
            instructionsHandler.solve_for(cmd,int(units))
    return  instructionsHandler.depth*instructionsHandler.horizontal_pos


if __name__ == '__main__':
    print(parseInstructions())
