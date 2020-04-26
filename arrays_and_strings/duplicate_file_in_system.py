#https://leetcode.com/problems/find-duplicate-file-in-system/
import collections
class Solution:
    def findDuplicate(self, paths):
        content_to_files = collections.defaultdict(list)
        for p in paths:
            data = p.split()
            d = data[0]
            for f in data[1:]:
                c = f.rfind("(")
                file_data = f[c+1:len(f)-1]
                file_name = f[:c]
                content_to_files[file_data].append(d+'/'+file_name)
        return [v for v in content_to_files.values() if len(v) > 1]

s = Solution()
s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])


