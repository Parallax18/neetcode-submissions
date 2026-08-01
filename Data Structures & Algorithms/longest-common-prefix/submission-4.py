class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tokens = {}
        result = ""
        # if len(strs) == 1:
        #     return strs[0]

        for word in strs:
            for index, char in enumerate(word):
                t = f"{char}{index}"
                if t in tokens:
                    tokens[t] += 1
                else:
                    tokens[t] = 1

        print(f"Tokens: {tokens}")
        for token in tokens:
            if tokens[token] == len(strs):
                result += list(token)[0]
            else:
                return result
        return result