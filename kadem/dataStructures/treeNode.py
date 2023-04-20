from dataStructures import kBucket

class TreeNode:
    def __init__(self, leafHuh : bool, k : int):
        self.__bucket = None
        self.leafHuh = leafHuh
        self.__k = k
        if leafHuh:
            self.__bucket = kBucket.kBucket(k)
        self.left = None
        self.right = None
    
    def insert(self, id : int):        
        if not self.leafHuh:
            raise Exception(f"Trying to insert {id} into non leaf node")
        self.__bucket.insert(id)