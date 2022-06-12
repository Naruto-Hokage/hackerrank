# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
for _ in range(int(input())):
    cmd, *arg = str(input()).split()
    getattr(d, cmd)(*arg)
print(*d)
