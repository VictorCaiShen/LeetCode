nums1 = [1, 2]
nums2 = [3, 4]
num3 = nums1 + nums2
num3.sort()
a = len(num3)/2
if num3 != []:
    if a == int(a):
        print(float((num3[int(a)]+num3[int(a)-1])/2))
    else:
        print(num3[int(a)])

