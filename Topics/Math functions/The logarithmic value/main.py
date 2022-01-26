import math

int_1 = int(input())
int_2 = int(input())

print(round(math.log(int_1, int_2) if int_2 > 1 else math.log(int_1), 2))