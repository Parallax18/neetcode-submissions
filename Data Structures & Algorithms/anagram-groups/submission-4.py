class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted( word.lower() ) )
            # grouped[sorted_word] = [word.lower()] + grouped.get(sorted_word, [])
            grouped[sorted_word].append(word)

        print(grouped.values())
        return list(grouped.values())