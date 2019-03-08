#!/usr/bin/env python3
#author:Alnk(李成果)
import os
import sys
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
print(base_path)
from  atm.core.payment import PayMent

p = PayMent()
ret = p.payment(1000)
if ret == True:
    print('支付成功')
else:
    print(ret)