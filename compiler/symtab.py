class SymTab:
    def __init__(self, variables, functions):
        self.variables = variables
        self.functions = functions

    def draw(self):
        data = self.variables
        data.extend(self.functions)

        print("Symbol")
        print("--------------------")
        for value in data:
            print(value)