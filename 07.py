# -*- coding: utf-8 -*-
class Solution:
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        # if str1 == '':
        #     return 0
        str1 = str1.lstrip()
        flag_num = flag_flag = 0
        flag = num = ''
        for c in str1:
            # if c == ' ':
            #     continue
            if (c == '+' or c == '-') and (not flag_flag) and (not flag_num):
                flag = c
                flag_flag = 1
                continue
            if c >= '0' and c <= '9':
                num += c
                flag_num = 1
            if flag_num == 0 :
                return 0
            if not (c >= '0' and c <= '9') :
                break
        if flag_num:
            num = int(num)
            if flag_flag:
                num *= int(flag + '1')
            if num < -2**31:
                return -2**31
            if num > 2**31 - 1:
                return 2**31 -1
            return num
        else :
            return 0
print(Solution().myAtoi('-42'))