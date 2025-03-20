
numbers = [9,80,7,0,1]
numbers.sort()
#print(numbers)

t1 = (9,80,7,0,1)
result = sorted(t1, reverse=True)

str_lst = ["c", "z", "a", "p"]
# print(type(result))
# print(result)
# print(sorted(str_lst))

lst1= [[1,"z"], [7, "b"], [2, "p"], [0, "q"]]

def get_key(item):
    return item[1]

# print(sorted(lst1, key=lambda x: x[1])) # sort by second element of each sublist
# print(sorted(lst1, key=get_key)) # sort by second element of each sublist

d1 = {1: "z", 7: "b", 2: "p", 0: "q"}
print(sorted(d1.items(), key=lambda x: x[1])) # sort by value of each key-value pair
