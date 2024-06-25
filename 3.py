# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print(i,'-th color of rainbow is ', color, sep = '')
#     i += 1


n=int(input())

sum=0
for i in range(1, n+1):
    sum += i ** 2

print(sum)
