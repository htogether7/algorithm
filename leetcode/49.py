from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 정렬
        # 시간복잡도 : O(N)
        # 공간복잡도 : O(N)
        
        dict = defaultdict(list)

        for str in strs:
            str_to_list = list(str)
            str_to_list.sort()
            sorted_str = "".join(str_to_list)
            dict[sorted_str].append(str)

        result = []
        for key in dict:
            result.append(dict[key])
        return result
