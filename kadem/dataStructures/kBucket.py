class kBucket:
    def __init__(self, k : int):
        self.__k = k
        self.__nodes : list[str] = [] #should be sorted by access time
    
    def insert(self, id):
        self.__nodes.append(id)