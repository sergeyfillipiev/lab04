def count_common_elements(*lists):
    """Функция для подсчёта количества одинаковых элементов в N списках."""
    if not lists:
        return 0

    # Используем множества для нахождения пересечений
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements &= set(lst)  # Находим пересечение с текущим списком

    return len(common_elements)

# Пример использования
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3, 6, 7]
    list3 = [3, 2, 8, 9]

    result = count_common_elements(list1, list2, list3)
    print(f"Количество одинаковых элементов: {result}")
