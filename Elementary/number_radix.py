#!/usr/bin/env checkio --domain=py run number-radix

# https://py.checkio.org/mission/number-radix/

# 
# END_DESC

def checkio(str_number, radix):
    try:
        b = int (str_number,radix)
        return b
    except:
        return -1
    
print (checkio('AB',10))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"