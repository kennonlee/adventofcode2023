import sys

modules = {}
pq = []

class Module:
    counts = {True: 0, False: 0}

    def __init__(self, name, outs):
        self.name = name
        self.outs = outs
        modules[name] = self
#        print("initializing", name, outs)
    
    def __repr__(self):
        s = self.__class__.__name__ + '{' + self.name + ' ' + str(self.outs) + '}'
        return s

    def pulse(self, src, high):
        Module.counts[high] += len(self.outs)        
        for out in self.outs:
            pq.append((self.name, out, high))

class Button(Module):
    None

class Broadcaster(Module):
    def __init__(self, outs):
        super().__init__('broadcaster', outs)

class Flipflop(Module):
    def __init__(self, name, outs):
        super().__init__(name, outs)
        self.on = False

    def pulse(self, src, high):
        if high:
            return
        if self.on:
            self.on = False
        else:
            self.on = True
        super().pulse(self.name, self.on)

class Conjunction(Module):
    def __init__(self, name, outs):
        super().__init__(name, outs)
        self.ins = {}

    def add_input(self, input):
        self.ins[input] = False

    def pulse(self, src, high):
        self.ins[src] = high
        if all(self.ins.values()):
            super().pulse(self.name, False)
        else:
            super().pulse(self.name, True)

for line in sys.stdin.readlines():
    module, outs = [i.strip() for i in line.split('->')]
    outs = outs.split(', ')
    if module == 'broadcaster':
        modules[module] = Broadcaster(outs)
    else:
        type = module[0]
        name = module[1:].strip()
        if type == '%':
            modules[name] = Flipflop(name, outs)
        elif type == '&':
            modules[name] = Conjunction(name, outs)


# initialize conjunction inputs and identify dummy outputs
dummy_outs = []
for m in modules.values():
    for out in m.outs:
        if out not in modules.keys():
            dummy_outs.append(out)
            continue
        print(modules[out])
        if isinstance(conj := modules[out], Conjunction):
            conj.add_input(m.name)

for o in dummy_outs:
    modules[o] = Module(o, [])

print(modules)

b = Button('button', ['broadcaster'])

def cycle(high):
    b.pulse('', high) 
    while pq:
        src, tgt, high = pq.pop(0)
#        print(src, '-high->' if high else '-low->', tgt, )
        modules[tgt].pulse(src, high)

for i in range(1000):
    cycle(False)
print(Module.counts, Module.counts[True] * Module.counts[False])

