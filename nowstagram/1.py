def stringToInt(string):
    if not string:
        return None
    if string[0] == '-':
        flag = 1
        string  = string[1:]
    else:
        flag = 0
    s = string.lstrip('0')
    res = 0
    lenth = len(s)
    fac = 0
    for i in range(lenth-1,-1,-1):
        if not s[i].isdigit():
            return None
        res += (ord(s[i]) - ord('0'))*10**fac
        fac += 1
    if not flag and res > 2**31-1:
        return 2**31-1
    elif flag and -res < (-2)**31:
        return (-2)**31
    else:
        return res if not flag else -res



class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class olution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        prehead = ListNode(float('-inf'))
        prehead.next = head
        pre = prehead
        cur = head.next
        while cur:
            tmp = cur.next
            while pre.next and cur.val > pre.next.val:
                pre =pre.next
            cur.next = pre.next
            pre.next = cur
            pre = prehead
            cur = tmp
        return prehead.next
    def traverse(self,head):
        if not head:
            return []
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

import random
'''def randBonus(min, total, num):
    print(min, total, num)
    # print "{:.2f}".format(3.1415029)
    total = float(total)
    num = int(num)
    min = 0.01
    if num < 1:
        return
    if num == 1:
        print("第%d个人拿到红包数:%.2f" % (num, total))
        return
    i = 1
    totalMoney = total
    while (i < num):
        max = totalMoney - min * (num - i)
        max = max / (num-i+1)*2
        monney = random.randint(int(min * 100), int(max * 100))
        monney = float(monney) / 100
        totalMoney = totalMoney - monney
        print("第%d个人拿到红包为:%.2f, 余额:%.2f" % (i, monney, totalMoney))
        i += 1

    print("第%d个人拿到红包为:%.2f, 余额:%.2f" % (i, totalMoney, 0.00))
randBonus(0.01,20,10)'''

def randBonus(min,total,num):
    print("最小金额：%.2f,总金额:%f,红包数:%d" %(min,total,num))
    if num < 1:
        return
    if num == 1:
        print("抢到红包:%.2f" %(total))
    num = int(num)
    totalMoney = total
    i = 1
    while i < num:
        max = totalMoney - min*(num-i)
        upper = max/(num-i+1)*2
        cur_bonus = random.uniform(min,upper)
        totalMoney -= cur_bonus
        print("第%d个人抢到%.2f元,剩余金额为:%.2f" %(i,cur_bonus,totalMoney))
        i += 1
    print("第%d个人抢到%.2f元,剩余金额为:%.2f" % (i, totalMoney, 00.00))

def nextPermulation(nums):
    def reverse(nums,i ,j):
        while i<j:
            nums[i] , nums[j] = nums[j] , nums[i]
            i += 1
            j -= 1
        return nums
    length = len(nums)
    if length < 2:
        return nums
    i = length -1
    while i > 0 and nums[i] <= nums[i-1]:
        i -= 1
    if i == 0:
        return reverse(nums,0,length-1)
    j = i - 1
    for k in range(length-1,j,-1):
        if nums[k] > nums[j]:
            nums[k] , nums[j] = nums[j] , nums[k]
            break
    a , b = i , length-1
    return reverse(nums,a,b)

'''class Solution(object):
    def calculate(self, s):
        if not s:
            return None
        sign = '+'
        n = len(s)
        num = 0
        stack = []
        for i in range(n):
            if s[i].isdigit():
                num = num*10 + (ord(s[i])-ord('0'))
            if s[i] in ['+','-','*','/'] or i == n-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
            print(stack,sign)
        return sum(stack)'''

def rebuildNum(nums):
    n = len(nums)
    if n <= 1:
        return nums
    positive , negative = [] , []
    for num in nums:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    res = []
    a , b = 0 , 0
    while a < len(positive) and b < len(negative):
        res.append(positive[a])
        a += 1
        res.append(negative[b])
        b += 1
    if a < len(positive):
        res += positive[a:]
    if b < len(negative):
        res += negative[b:]
    return res

def hepify(nums,n,i):
    largest = i
    l = 2*i + 1
    r = l + 1
    if l<n and nums[l] > nums[largest]:
        largest = l
    if r<n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i] , nums[largest] = nums[largest] , nums[i]
        hepify(nums,n,largest)
import collections
queue = collections.deque()
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        if nums[0] > 0:
            return []
        res = []
        print(nums)
        for i in range(n-3):
            j , k = i+1 , n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                if nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k -=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
        return res

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))


