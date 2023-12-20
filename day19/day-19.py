# Advent of code day 19 in python
import re
f = open("./day-19.txt", "r")
instuctions = []
metalObjects = []
instructionMap = {}
acceptedObjects = []

for x in f:
    if (x[0] =="{"):
        inst = x.removesuffix("\n")
        dictifyMetalObjects = inst.replace("=", ":")
        metalDict = re.sub(r"([a-zA-Z]+)", r'"\1"', dictifyMetalObjects)
        metalObjects.append(eval(metalDict))
    else:
        rules = x.removesuffix("\n")
        instuctions.append(rules)
f.close()
instuctions.pop()
nf = open("instructions_19.py", "a")

for i in range(len(instuctions)):
    parsedCondition = instuctions[i].removesuffix("}")
    nameCondition = instuctions[i].split("{")
    instructionMap[nameCondition[0]] = nameCondition[1].split(",")

for key in instructionMap:
    for x in range(len(instructionMap[key])):
        instructionMap[key][x] = instructionMap[key][x].split(":")
        if x == 0 and len(instructionMap[key][x]) > 1:
          lastCondition = instructionMap[key][x][1]
          if len(lastCondition) == 1:
            dictName = re.sub(r"([a-zA-Z]+)", '["' + r'\1' + '"]', instructionMap[key][x][0])
            nf.write(f'\ndef {key.upper()}(metal):\n\tif(metal{dictName}):\n\t\treturn "{instructionMap[key][x][1]}"\n')
          else:
            dictName = re.sub(r"([a-zA-Z]+)", '["' + r'\1' + '"]', instructionMap[key][x][0])
            nf.write(f'\ndef {key.upper()}(metal):\n\tif(metal{dictName}):\n\t\treturn {instructionMap[key][x][1].upper()}(metal)\n')
        elif len(instructionMap[key][x]) > 1:
          lastCondition = instructionMap[key][x][1]
          if len(lastCondition) == 1:
            dictName = re.sub(r"([a-zA-Z]+)", '["' + r'\1' + '"]', instructionMap[key][x][0])
            nf.write(f'\n\tif(metal{dictName}):\n\t\treturn "{instructionMap[key][x][1]}"\n')
          else:
            dictName = re.sub(r"([a-zA-Z]+)", '["' + r'\1' + '"]', instructionMap[key][x][0])
            nf.write(f'\n\tif(metal{dictName}):\n\t\treturn {instructionMap[key][x][1].upper()}(metal)\n')
        else:
          lastCondition = instructionMap[key][x][0].removesuffix("}")
          if len(lastCondition) > 1:
            nf.write(f'\telse:\n\t\treturn {lastCondition.upper()}(metal)')
          else:
            nf.write(f'\telse:\n\t\treturn "{lastCondition.upper()}"\n')


nf.close()
import instructions_19 as inst
b = []
x = 0
m = 0
a = 0
s = 0
for z in metalObjects:
  b.append(inst.IN(z))
for o in range(len(b)):
   if b[o] == "A":
     x += metalObjects[o]['x']
     m += metalObjects[o]['m']
     a += metalObjects[o]['a']
     s += metalObjects[o]['s']
print(x + m + a + s)

