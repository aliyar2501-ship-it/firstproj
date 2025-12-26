def KthAppearance(A: list[int], a: int, k: int) -> int:
    count = 0
    for i in range(len(A)):
        if A[i] == a:
            count += 1
            if count == k:
                return i
    return -1
input_list_str = input("Введите список чисел через пробел (например, 1 3 2 3): ")
A_list = [int(x) for x in input_list_str.split()]
a_num = int(input("Введите искомое число 'a': "))
k_val = int(input("Введите порядковый номер  вхождения 'k': "))
result = KthAppearance(A_list, a_num, k_val)
print(f"\nИсходный список A: {A_list}")
print(f"Искомое число a: {a_num}, порядковый номер k: {k_val}")
print(f"Output: {result}")