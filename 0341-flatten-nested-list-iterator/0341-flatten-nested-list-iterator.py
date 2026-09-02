class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat = []
        self._flatten(nestedList)
        self.idx = 0

    def _flatten(self, nestedList):
        for ni in nestedList:
            if ni.isInteger():
                self.flat.append(ni.getInteger())
            else:
                self._flatten(ni.getList())

    def next(self) -> int:
        val = self.flat[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.flat)