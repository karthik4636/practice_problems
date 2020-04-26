#https://leetcode.com/problems/find-duplicate-file-in-system/
import collections
class Solution:
    def findDuplicate(self, paths):
        content_to_files = collections.defaultdict(list)
        for p in paths:
            data = p.split()
            d = data[0]
            for f in data[1:]:
                file_data = f.split('(') # the left over ')' doesn't matter
                content_to_files[file_data[1]].append(d+'/'+file_data[0])
        return [v for v in content_to_files.values() if len(v) > 1]

s = Solution()
s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])


