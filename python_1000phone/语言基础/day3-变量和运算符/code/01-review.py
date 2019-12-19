"""__author__=吴佩隆"""
the_number = int(input('输入一个整数:'))

if (the_number % 3 == 0 or the_number % 7 == 0) and the_number % 21 != 0:
    print(the_number,'能被3或7整除,但不能同时被3和7整除')
else:
    print(the_number,'不符合条件')