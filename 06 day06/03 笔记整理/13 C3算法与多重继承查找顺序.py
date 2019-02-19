#!/usr/bin/env python3
#author:Alnk(李成果)


# 示例 1
class O:pass
class F(O):pass
class E(O):pass
class D(O):pass
class C(E,F):pass
class B(D,E):pass
class A(B,C):pass

#
for s in A.__mro__:
    print(s)    # A/B/D/C/E/F/O 查找顺序

# 从左往右，依照C3算法进行查找


# 示例 2
class A1: pass
class A2: pass
class A3: pass
class B1(A1,A2): pass
class B2(A2): pass
class B3(A2,A3): pass
class C1(B1): pass
class C2(B1,B2): pass
class C3(B2,B3): pass
class D(C1, C2, C3): pass

print("从D开始查找：")
for s in D.__mro__:
    print(s)    # D/C1/C2/B1/A1/C3/B2/B3/A2/A3/OBJ

print("从C3开始查找：")
for s in C3.__mro__:
    print(s)    # C3/B2/B3/A2/A3