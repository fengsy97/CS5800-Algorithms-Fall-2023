# in python3

def getevents(nums,t):
    print("Input array is:",nums)
    print("Threshold is ",t)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] > t * nums[j]):
                print("Excute event E because a[%d] > %d * a[%d]"%(i,t,j))
nums = [8, 7, 2, 2, 0, 9, 6]
t = 2
getevents(nums,t)