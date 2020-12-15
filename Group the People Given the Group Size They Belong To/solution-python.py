class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        m = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in m:
                m[groupSizes[i]].append(i)
            else:
                m[groupSizes[i]] = [i]
        res = []
        temp = []
        for element in m.items():
            for j in range(len(element[1])):
                temp.append(element[1][j])
                if len(temp) == element[0]:
                    res.append(temp)
                    temp = []
        return res