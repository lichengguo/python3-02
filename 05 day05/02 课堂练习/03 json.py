import json

# dumps loads
# dic = {'key': 'vales'}
# ret = json.dumps(dic)
# print(ret, type(ret))
#
# ret2 = json.loads(ret)
# print(ret2, type(ret2))


# dump load
# dic = {'key': 'vales'}
# with open('json_file', 'w', encoding='utf-8') as f:
#     json.dump(dic, f)

with open('json_file', 'r', encoding='utf-8') as f:
    ret = json.load(f)
print(ret, type(ret))
