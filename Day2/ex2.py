#傳蕃薯
from lib.queue import Queue

q=Queue()
def hot_potato(name_list, num):
    for i in name_list:
        q.enqueue(i)
   
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    print(q.dequeue())

hot_potato(["Susan","Brad","Kent","David"], 6)               # 回傳 "Brad"
hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7) # 回傳 "Susan"