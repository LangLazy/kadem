from dataStructures import treeNode

class RoutingTable:
    #id - 160 bit sha1 id
    #k - global paramter which represents bucket size
    def __init__(self, id : int, k : int) -> None:
        self.id = id
        self.k = k
        self.root = treeNode.TreeNode(True, k, self.id)
    
    def insertNewNode(self, id : int) -> None:
        if id == self.id:
            print("Why am I adding myself")
            return
        currentNode = self.root
        #need to keep track of parent as that where the break happens, exceptional case for when root gets split
        currentInsertIdBit = id
        currentIdBit = self.id

        #while msb the same
            #if the appropraite direction is availavble (1 -> right, 0 left)
                #move in that direction and shift the bits as needed
            #else
                #this means you are at the lowest kbucket which has not been expanded yet
                #you need to go to the parent change it to be a new intermediary
                #split into 2 buckets
                #move into the appropraite one
        #u are at the first node which is in contention
        #go up to parent
            #if not parent 
                #  you are at the root on first split and it differs at first bit
                # make a new root node and split it, and go there and add ur self
            #else
                #go up to parent and see if k bucklet exists, if yes add yourself if no make it and add yourself


        
    
    def getKClosestNodes():
        pass