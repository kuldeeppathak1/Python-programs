def pallindrom(string):
    return string == string[::-1]

print(pallindrom('Kuldeep'))

print(pallindrom('onno'))

############ 
def pallindrom1(s):
    start = 0
    end = len(s) -1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

print(pallindrom1('Kuldeep'))

print(pallindrom1('onno'))
