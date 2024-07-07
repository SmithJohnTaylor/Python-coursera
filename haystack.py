import re 

fname = "sampletxt.txt"
handle = open(fname)
print(sum([int(x) for line in open(fname) for x in re.findall('[0-9]+', line)]))

# total = []

# for line in handle:
#     nums = re.findall('[0-9]+',line)
#     if len(nums) > 0:
#         for x in nums:
#             total.append(int(x))

# print(sum(total))
# for x in nums:
#     print(nums[x])

