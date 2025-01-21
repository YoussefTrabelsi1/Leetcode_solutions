from collections import defaultdict


def groupAnagrams(self, strs):
        
        c_map=defaultdict(list)
        for string in strs:
            count=[0]*26
            for c in string:
                count[ord(c)-ord('a')]+=1
            
            c_map[tuple(count)].append(string)
            
        return list(c_map.values())