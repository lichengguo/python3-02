#!/usr/bin/env python3
#author:Alnk(李成果)
import json

d1 = {'name':'alex'}

d2 = json.dumps(d1)
print(d2)
print(type(d2))
d3 = d2.encode()

print(d3)




d4 = d3.decode()
print(d4,type(d4))
print(json.loads(d3))