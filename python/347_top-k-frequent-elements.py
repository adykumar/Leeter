"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topk(self, nums, k):
        res= []
        dic = {}
        for each in nums:
            if each in dic:
                dic[each]+=1
            else:
                dic[each]=1
        bucket=[]
        for i in range(len(nums)+1):
            bucket.append([])
        for each in dic:
            bucket[ dic[each] ].append(each)
        for i in range(len(bucket)-1,0, -1):
            res.extend(bucket[i])
            if len(res)>=k: break
        return res

if __name__=="__main__":
    testcases= [[[1,1,1,2,2,3],2], [ [1,2], 2],[ [1,1,1,2,2,2,3,3,3],2 ] ]
    obj= Solution()
    for test in testcases:
        print test[0],test[1], " -> ", obj.topk(test[0], test[1])
