#if __name__ == "__main__":
list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

min_value_index = [0]
min_value = list_[min_value_index]

for i in range(list_):
        current_value = min_value
        if current_value < min_value:
            min_value = current_value
            min_value_index = i

print("Минимальный элемент =", min_value)  # TODO