from dataStructures import kBucket

class TreeNode:
    def __init__(self, leafHuh : bool, k : int,  prefix : int):
        self.bucket = None
        if leafHuh:
            self.bucket = kBucket.kBucket(k, prefix)
        self.left = None
        self.right = None
        
