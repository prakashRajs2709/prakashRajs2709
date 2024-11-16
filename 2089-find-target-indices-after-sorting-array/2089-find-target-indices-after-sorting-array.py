class Solution:
    def targetIndices(self, a: List[int], target: int) -> List[int]:
        a.sort()
        result = []
        for i in range(len(a)):
            if a[i]==target:
                result.append(i)
        return result