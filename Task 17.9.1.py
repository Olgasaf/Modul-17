L = input('Введите числа от 0 до 100 через пробел: ').split()
L =list(map(int, L))
while True:
    try:
        b =int(input("Введите число: "))
        if b < 0 or b >= 99:
            raise ValueError()
        break
    except ValueError:
        print(f'Неверный ввод. Введите число заданного диапозона: ')
L.append(b)
print((L))
for i in range(1, len(L)):
    x = L[i]
    idx = i
    while idx > 0 and L[idx-1] > x:
        L[idx] = L[idx-1]
        idx -= 1
        L[idx] = x
print((L))

def binary_search(L, b, left, right):
    if left > right:  # если левая граница превысила правую,
        return left-1

    middle = (right + left) // 2  # находимо середину
    if L[middle] == b:  # если элемент в середине,
        return middle - 1
    elif b < L[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(L, b, left, middle-1)
    else:  # иначе в правой
        return binary_search(L, b, middle+1, right)

# запускаем алгоритм на левой и правой границе
print(binary_search(L, b, 0,  len(L)))



