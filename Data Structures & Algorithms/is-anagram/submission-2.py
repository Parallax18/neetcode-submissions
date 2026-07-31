class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # set_s = set(list(s))
        # set_t = set(list(t))
        # print(set_s, set_t)
        # return set_s == set_t

        s_map = {}
        for s_item in list(s):
            if s_item in s_map:
                s_map[s_item] = s_map[s_item] + 1
            else:
                s_map[s_item] = 1
        t_map = {}
        
        for t_item in list(t):
            if t_item in t_map:
                t_map[t_item] = t_map[t_item] + 1
            else:
                t_map[t_item] = 1
            
        print(s_map, t_map)
        return t_map == s_map