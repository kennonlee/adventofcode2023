import sys

class Workflow:
    def __init__(self, name, cmds):
        self.name = name
        self.cmds = []
        # just save as strings for now; will eval() later
        for cmd in cmds[:-1]:
            self.cmds.append(cmd.split(':'))
        self.end_cmd = cmds[-1]
        self.trace = []

    def __repr__(self):
        s = 'wf{' + self.name + ', '
        s += str(self.cmds) + ', '
        s += self.end_cmd + '}'
        return s
    
    def add_trace(self, wf): 
        self.trace.append(wf)
    

wfs = {}
ends = []
for line in sys.stdin.readlines():
    line = line.strip()
    # skip the blank newline
    if not line:
        continue
    # read in instructions
    elif line[0] != '{':
        name, cmds = line.strip().split('{')
        cmds = cmds[:-1].split(',')
        wf = Workflow(name, cmds)
        wfs[name] = wf
        if 'A' in line:
            ends.append(wf)

#print(wfs)
#print(parts)
print(ends)

prev = None
for end in ends:
    while prev != 'in':
        for wf in wfs.values():
            for cmd in wf.cmds:
                if cmd[1] == end.name:
                    end.add_trace(wf)
            if wf.end_cmd == end.name:
                end.add_trace(wf)

for wf in wfs:
    print(wf.trace)
