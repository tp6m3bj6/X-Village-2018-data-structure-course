import json
with open('ptt_0726_s.json','r',encoding='utf-8') as f:
a=json.load(f)
# abc = []
# for i in range(len(a)):
#     b = a[i]["h_推文總數"]
#     all = b.get("all", None)
#     if all is not None:
#         print(all)
#     else:
#         b['all'] = 0