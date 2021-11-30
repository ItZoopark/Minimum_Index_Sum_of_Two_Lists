# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["KFC", "Shogun", "Burger King"]
# list2 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]

# 599
def findRestaurant(list1, list2):
    dict1 = dict(zip(list1, range(len(list1))))
    dict2 = dict(zip(list2, range(len(list2))))
    res1 = sorted(dict1.items(), key=lambda item: item[0])
    res2 = sorted(dict2.items(), key=lambda item: item[0])
    if len(res1) != len(res2):
        min_res = min(res1, res2, key=len)
        max_res = max(res1, res2, key=len)
    else:
        min_res = res1
        max_res = res2
    i, j = 0, 0
    out = []
    min_value = len(res1) + len(res2)
    while i < len(min_res):
        if min_res[i][0] == max_res[j][0]:
            out.append([min_res[i][0], min_res[i][1] + max_res[j][1]])
            min_value = min(min_value, min_res[i][1] + max_res[j][1])
            i += 1
        if i < len(min_res) and j < len(max_res) and max_res[j][0] < min_res[i][0]:
            if j != len(max_res) - 1:
                j += 1
            else:
                i += 1
        else:
            i += 1
    res = []
    for item in out:
        if item[1] == min_value:
            res.append(item[0])
    return res


# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["KFC", "Shogun", "Burger King"]
list1 = ["Shogun", "Piatti", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(list1, list2))
# print(out)
# print(min_value)

# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         res = []
#         for i in range(len(list1)):
#             for j in range(len(list2)):
#                 if list1[i] == list2[j]:
#                     res.append([list1[i], i + j])
#         res = sorted(res, key=lambda x: x[1])
#         out = []
#         max_num = res[0][1]
#         out.append(res[0][0])
#         i = 1
#         while i < len(res):
#             if res[i][1] > max_num:
#                 break
#             out.append(res[i][0])
#             i+=1
#         return out
