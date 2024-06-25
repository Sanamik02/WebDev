# def hanoi(n, from_rod, to_rod, aux_rod):
#     if n == 1:
#         print(from_rod, to_rod)
#         return
#     hanoi(n-1, from_rod, aux_rod, to_rod)
#     print(from_rod, to_rod)
#     hanoi(n-1, aux_rod, to_rod, from_rod)

# n = int(input().strip())

# # Вызываем функцию Ханойских башен для n дисков
# hanoi(n, 1, 3, 2)



def hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        print(f"1 {from_pole} {to_pole}")
        return
    hanoi(n-1, from_pole, aux_pole, to_pole)
    print(f"{n} {from_pole} {to_pole}")
    hanoi(n-1, aux_pole, to_pole, from_pole)

n = int(input())
hanoi(n, 1, 3, 2)