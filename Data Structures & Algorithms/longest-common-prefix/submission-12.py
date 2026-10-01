class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        longest_prefix = strs[0]

        for i in range(len(longest_prefix) - 1, -1, -1):

            for j in range(1, len(strs)):
                print(i, j)
                if i >= len(strs[j]) or strs[j][i] != longest_prefix[i]:
                    print("decr i")
                    longest_prefix = longest_prefix[:i]
                    break

        return longest_prefix

        




