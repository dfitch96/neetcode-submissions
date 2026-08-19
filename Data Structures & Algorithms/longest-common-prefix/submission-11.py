class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        longest_prefix = strs[0]
        j = len(longest_prefix)

        for row in range(1, len(strs)):
            j = min(len(strs[row]), j)
            print(row)
            for col in range(j):
                print(f'col {col}')
                if strs[row][col] != longest_prefix[col]:
                    j = col
                    break

        return longest_prefix[:j]

