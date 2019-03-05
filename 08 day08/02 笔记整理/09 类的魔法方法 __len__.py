#!/usr/bin/env python3
# author:Alnk(李成果)

class Data(object):

    def __len__(self):
        return 345  # 只能返回数字


d = Data()
print(len(d))
print(d.__len__())
