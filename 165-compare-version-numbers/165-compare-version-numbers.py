class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vm = version1.split('.')
        v1 = [int(i) for i in vm]
        vn = version2.split('.')
        v2 = [int(i) for i in vn]
        if len(v1) > len(v2):
            for i in range(len(v2)):
                if v1[i] > v2[i]:
                    return 1
                elif v1[i] < v2[i]:
                    return -1
            if sum(v1) > sum(v2):
                return 1
            return 0
        else:
            for i in range(len(v1)):
                if v1[i] > v2[i]:
                    return 1
                elif v1[i] < v2[i]:
                    return -1
            if sum(v1) < sum(v2):
                return -1
            return 0