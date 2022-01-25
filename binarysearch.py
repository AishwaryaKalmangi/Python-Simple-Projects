def binarysearch(nums, x):
    least=0
    high=len(nums)-1
    #print(mid)
    while least<=high:
        mid = least + high // 2
        print(mid)
        if nums[mid] > x:
            high=mid-1
        elif nums[mid] < x:
            least=mid+1
        else:
            return mid
    print('Not found')
    return -1


binarysearch([1,2,3,4,5,6,7,8],2) #This will return the index of element we want to search