class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def get_optimal_compression_length(idx, prev_char, length, k):
            if k < 0:
                return float('inf')
            if idx >= len(s):
                return 0
            delete = get_optimal_compression_length(idx+1, prev_char, length, k-1)
            keep = 0
            if s[idx] == prev_char:
                if length in [1, 9, 99]:
                    keep = 1
                keep += get_optimal_compression_length(idx+1, prev_char, length+1, k)
            else:
                keep = 1 + get_optimal_compression_length(idx+1, s[idx], 1, k)
            return min(delete, keep)

        return get_optimal_compression_length(0, '', 0, k)