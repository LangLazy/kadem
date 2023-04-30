import routingTable.routingTable as rt
import hashlib

def findLongestCommonSuffix(s1 : str, s2 : str) -> str:
    s1 = s1[::-1]
    s2 = s2[::-1]
    pos = 0
    while pos < min(len(s1), len(s2)):
        if s1[pos] != s2[pos]:
            break
        pos += 1
    return s1[:pos][::-1]

def getNthLastBitStr(num : int, n : int) -> str:
    return bin(1&(num>>n))[2:] #ignore the 0b prefix for binary numbers

def arbitrary_add(tableId : int, newId : int):
    table = rt.RoutingTable(tableId,3)
    table.insertNewNode(newId)
    commonSuffix = findLongestCommonSuffix(bin(tableId|(1<<160)), bin(newId|(1<<160)))
    # print(commonSuffix)
    # print(table)
    assert str(table) == (getNthLastBitStr(tableId, len(commonSuffix)) + commonSuffix)

def test_bucket_adding():
    arbitrary_add(0b1111111111, 0)
    arbitrary_add(0b1111111111, 0b11111111)
    arbitrary_add(0b101010101010101010000101010101001010100101000101010101010, 0b10)
    tableId = int.from_bytes(hashlib.sha1("server1".encode()).digest(), "little")
    newId = int.from_bytes(hashlib.sha1("server2".encode()).digest(), "little")
    arbitrary_add(tableId, newId)