
class Tool:
    def __init__(self, name,weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name}, {self.weight})'

tools = [
    Tool('level',3.5),
    Tool('hammer',1.25),
    Tool('hammer', -1),
    Tool('DanVa', 1.25),
    Tool('screwdriver',0.5),
    Tool("chisel",-0.25),
]

# tools = sorted(tools, key=lambda tool: (tool.weight,tool.name),reverse=True )
tools.sort(key=lambda tool: (tool.weight,tool.name.lower()),reverse=True)
# tools.sort(key=lambda tool: tool.name)

print(tools)