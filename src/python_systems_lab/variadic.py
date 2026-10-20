def sum_numbers(*numbers: int) -> int:
    if not numbers:
        return 0

    return sum(numbers)


# if __name__ == '__main__':
#     def sum_numbers(*numbers: int) -> int:
#         if not numbers:
#             return 0

#         print(sum(numbers))

#     sum_numbers(1,5,6,7,8,9)
    