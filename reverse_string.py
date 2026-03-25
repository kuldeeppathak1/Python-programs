def reverse_string(s):
    return s[::-1]

print(reverse_string('Hello'))

############################################
def reverse_string1(s):
    result = ''
    for char in s:
        result = char + result
    return result

print(reverse_string1('Hello'))