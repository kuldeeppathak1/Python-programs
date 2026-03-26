def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

print(find_duplicates([1,2,3,1,3,6,6]))

#####################

def find_duplicates1(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # return only duplicates
    # duplicates = [num for num, count in freq.items() if count > 1]
    # return duplicates

    #if return count as well
    return {k: v for k, v in freq.items() if v > 1}
    

print(find_duplicates1([1,2,3,1,3,6,6]))  # [1, 3, 6]