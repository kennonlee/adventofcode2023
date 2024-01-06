import sys

class Workflow:
    def __init__(self, name, cmds):
        self.name = name
        self.cmds = []
        # just save as strings for now; will eval() later
        for cmd in cmds[:-1]:
            self.cmds.append(cmd.split(':'))
        self.end_cmd = cmds[-1]

    def __repr__(self):
        s = 'wf{' + self.name + ', '
        s += str(self.cmds) + ', '
        s += self.end_cmd + '}'
        return s


wfs = {}
parts = []
for line in sys.stdin.readlines():
    line = line.strip()
    # skip the blank newline
    if not line:
        continue
    # read in instructions
    elif line[0] != '{':
        name, cmds = line.strip().split('{')
        cmds = cmds[:-1].split(',')
        wfs[name] = (Workflow(name, cmds))
    else:
#        print(line[1:-1])
        instrs = line[1:-1].split(',')
        parts.append(instrs)

#print(wfs)
#print(parts)

ret = 0
for part in parts:
    # initialize x,m,a,s vars
    for instr in part:
        exec(instr, globals(), globals())

#    print(x, m, a, s)
    name = 'in'
    while name not in ['A', 'R']:
#        print(name)
        wf = wfs[name]
        match = False
        for cmd in wf.cmds:
            instr, next = cmd
#            print(x,m,a,s, instr, eval(instr))
            if eval(instr):
                name = next
                match = True
                break
        if not match:
            name = wf.end_cmd    
#    print(name)
    if name == 'A':
        ret += x + m + a + s

print(ret)