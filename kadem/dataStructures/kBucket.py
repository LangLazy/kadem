class kBucket:
    def __init__(self, k : int):
        self.__k = k
        self.__nodes : list[str] = [] #should be sorted by access time
    
    def __str__(self):
        return str(self.__nodes)

    def insert(self, id):
        self.__nodes.append(id)

    def isPresent(self, queryId):
        return queryId in self.__nodes