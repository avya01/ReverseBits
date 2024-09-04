def reverse_bits(n, bitsize):
    reversed_num = 0
    for i in range(bitsize):
        reversed_num = (reversed_num << 1) | (n & 1)
        n >>= 1
    return reversed_num

# Example usage
number = int(input("Enter a number: "))
bitsize = int(input("Enter the bit-size of the number(If wrong, code will malfunction): "))
reversed_number = reverse_bits(number, bitsize)
print("Original number:",number, "Reversed bits: ", reversed_number)