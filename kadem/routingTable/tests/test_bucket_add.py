import routingTable.routingTable as rt

def findLongestCommonSuffix(s1 : str, s2 : str) -> str:
    s1 = s1[::-1]
    s2 = s2[::-1]
    pos = 0
    while pos < min(len(s1), len(s2)):
        if s1[pos] != s2[pos]:
            break
        pos += 1
    return s1[:pos][::-1]

def getLastBitStr(num : int) -> str:
    return bin(1&num)[2:] #ignore the 0b prefix for binary numbers

def test_add():
    tableId = 0b1111111111
    newId = 0
    table = rt.RoutingTable(tableId,3)
    table.insertNewNode(newId)
    assert str(table) == (findLongestCommonSuffix(bin(tableId), bin(newId)) + getLastBitStr(tableId))
    newId = 0b101111
    table.insertNewNode(newId)
    assert str(table) == (findLongestCommonSuffix(bin(tableId), bin(newId)) + getLastBitStr(tableId))