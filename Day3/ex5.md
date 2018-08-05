Python提供兩種內建排序的function分別是sort()和sorted()
這兩個function都可以用來排序一個list
差別在於sorted()會回傳一個排序好新的list
sort()會直接修改原始的list並排序完成



直接修改原始的a
a.sort()
print(a)

要指定
a = [2, 4, 3, B, 1]
b=sorted(a)
print(b)


sort()只能用在list上排序，而sorted()可用來排序任何的(string, dictionary, tuple...)

------------------

Python 使用一種叫 Timsort 的混種排序演算法