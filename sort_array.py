def sort_array(data_list=[]):
    new_list = []
    for i in data_list:
        pivot = i
        left = [x for x in new_list if x< pivot]
        right = [x for x in new_list if x >= pivot]
        new_list = left + [i] + right
    return new_list

print(sort_array([5,8,2,9,7,7]))

####### another approch #####



def sort_array1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
    
print(sort_array1([5,8,2,9,7,7]))