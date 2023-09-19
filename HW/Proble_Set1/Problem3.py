# in python3

def getevents(nums,t):
    answer = 0
    print("Input array is:",nums)
    print("Threshold is ",t)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] > t * nums[j]):
                print("Excute event E because a[%d] > %d * a[%d]"%(i,t,j))
                answer += 1
    print("The total number of events is %d"%answer )
nums = [4, 2, 11, 5, 7, 8]
t = 1
getevents(nums,t)