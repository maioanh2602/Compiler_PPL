class SymTab:
    def __init__(self, variables, functions):
        self.variables = variables
        self.functions = functions

    def draw(self):
        data = []

        for var in self.variables.keys():
            instance = []
            instance.append(var)
            instance.append('Number')
            data.append(instance)
        for func in self.functions.keys():
            instance = []
            instance.append(func)
            instance.append('Function')
            data.append(instance)

        print("+" + '-'*22 + "+" + '-'*22 + "+" + '-'*22 + "+")
        print("| {:<20} | {:<20} | {:<20} |".format('Symbol', 'Type', 'Scope'))
        print("+" + '-'*22 + "+" + '-'*22 + "+" + '-'*22 + "+")
        for res in data:
            print("| {:<20} | {:<20} | {:<20} |".format(res[0], res[1], 'Global'))
        print("+" + '-'*22 + "+" + '-'*22 + "+" + '-'*22 + "+")