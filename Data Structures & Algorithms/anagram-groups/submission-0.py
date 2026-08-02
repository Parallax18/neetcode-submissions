class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # same_length = defaultdict(list)
        # sorted_by_len = []
        # sorted_by_len = sorted(strs, key = len)
        grouped = defaultdict(list)
        for word in strs:
            # print(sorted_by_len)
            # word_length = len(word)


            # same_length[word_length] = [ "".join(sorted(word.lower())) ] + same_length.get(word_length, [])
            # same_length[0] = [ "".join(sorted(word.lower())) ] + same_length.get(0, [])
            # sorted_by_len.append("".join(sorted( word.lower() )))
            sorted_word = "".join(sorted( word.lower()))
            # sorted_by_len.append( sorted_word )

            grouped[sorted_word] = [word.lower()] + grouped.get(sorted_word, [])

            # sorted_by_len = sorted( sorted_by_len, key = len )

        # for w in sorted_by_len:
        #     grouped[w] = [w] + grouped.get(w, [])

        # print(sorted_by_len)
        print(grouped.values())
        return list(grouped.values())

            #   for i in range(len(s)):
            # countS[s[i]] = 1 + countS.get(s[i], 0)
            # countT[t[i]] = 1 + countT.get(t[i], 0)