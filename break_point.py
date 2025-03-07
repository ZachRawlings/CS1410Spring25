def remove_dup(lst):
    output = []
    for i in lst:
        if i not in output:
            output.append(i)
    return output

input = [1,8,5,9,1,2,1,3,4,2,3]

result = remove_dup(input)