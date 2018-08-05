from lib.stack import Stack
s=Stack()
def dec_to_bin(dec):
    n=dec
    while n!=0:
        n=dec//2
        l=dec%2#
        dec=n
        s.push(l)
        #print(l)
    #print('Stack size:', s.size())

    for i in range(s.size()):
        print(s.pop(),end='')
    print('')
dec_to_bin(42)
dec_to_bin(100)
dec_to_bin(1023)
dec_to_bin(1024)
