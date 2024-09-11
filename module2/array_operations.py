"""Do Array Operations
"""

import numpy as np

def main():
    """Driven Function
    """

    numbers_list = [2, 4, 6, 8, 10]
    print(f'Before list {numbers_list}')

    # Increment each element by 3
    for item in range(len(numbers_list)):
        numbers_list[item] = numbers_list[item] + 3
    print(f'After list {numbers_list}')     

    # Convert list to a Numpy Array
    numbers_arr = np.array(numbers_list)
    print(f'Before array {numbers_arr}')

    # Increment each element by 3
    numbers_arr += 3
    print(f'After array {numbers_arr}')

if __name__ == '__main__':
    main()