class Solution:
    def diffWaysToCompute(self, inp):
        def helper(l, r):
            ans = []
            for i in range(l, r):
                if inp[i] not in ops:
                    continue
                ans += [ops[inp[i]](le, ri) for le in helper(l, i)
                                            for ri in helper(i + 1, r)]
            return ans if len(ans) != 0 else [int(inp[l:r])]
        ops = {
                '-': lambda x, y: x - y,
                '+': lambda x, y: x + y,
                '*': lambda x, y: x * y,
                }
        return helper(0, len(inp))
                    