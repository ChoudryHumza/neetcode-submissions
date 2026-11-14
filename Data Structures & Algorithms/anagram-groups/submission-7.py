class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = defaultdict(list)
        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            track[sortedString].append(strs[i])
        return list(track.values())
