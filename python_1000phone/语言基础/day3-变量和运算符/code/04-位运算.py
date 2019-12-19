"""__author__=吴佩隆"""

# 所有的位运算都是针对数字的补码进行操作的;特点:效率高，快
# 位运算: &(与),|(或),~(取反),^(异或),<<(左移),>>(右移)

# 1.&
"""
运算规则:补码每一位上的数都是1结果就是1,如果有一个0就是0
1110 & 0111 = 0110
应用:高效的判断数字的奇偶性 - 让数字和1进行按位与运算,判断结果是0(偶数)还是1(奇数)
"""
a = 3 & 2
print(a)

"""
3的补码:00000011
2的补码:00000010
00000011 & 00000010 = 00000010 == 2
"""

b = -7 & 3
print(b)
"""
-7补码:10000111(原) -> 11111001(补)
3的补码:
-7 & 3 = 00000001(补) == 1
"""

print(7 & 1, 123 & 1, 111 & 1)
print(8 & 1, 18 & 1, 96 & 1)

# 2.|
"""
运算规则:每一位上的数如果都是0结果就是0，只要有1结果就是1
1110|0111 -> 1111
"""

print(3 | 2)
print(-7 | 3)   # 11111001(补) | 00000011(补)
"""
-7:11111001(补)
3:00000011(补)
11111011(补) -> 11111010(补) -> 10000101 == -5
"""

# 3.~
"""
运算规则:将每一位上的0变成1,1变成0
~ 1101 -> 0010
"""
print(~-7)
"""
11111001(补) -> 00000110 == 6
"""

# 4.^
"""
运算规则:每一位上的数相同为0，不同为1
11011 ^ 10010 -> 01001
"""

# 5.<<
"""
数字<<N  ->  指定的数字的补码整体向左移动N位 - 计算:数字 * 2 ** N
"""
print(2 << 1)
print(3 << 2)

# 6.>>
"""
数字>>N  ->  指定的数字的补码整体向右移动N位 - 计算:数字 // 2 ** N
"""
print(4 >> 1)
print(9 >> 2)
print(-8 >> 2)
print(-9 >> 1)