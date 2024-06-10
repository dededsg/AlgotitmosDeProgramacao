

class Solution(object):

    
    def twoSum():
          
        nums = [2,7,11,15]
        target = 9
        h = {}
        for i in range(len(nums)):
            j = [target - nums[i]] 
            h[target - nums[i]] = i
            print(j)
        
            print(h)
        for i in range(len(nums)):
            val = h.get(nums[i])
            print(val)
            if val != None and val != i:
                return [val, i]
    print(twoSum())