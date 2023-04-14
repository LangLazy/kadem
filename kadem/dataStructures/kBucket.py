class kBucket:
    def __init__(self, k : int, id : int):
        self.k = k
        self.nodes : list[str] = [id] #should be sorted by access time