def find_parity_On(x):
    """return 1 if # bits equal to 1 is odd, 0 if even
    O(n), loops over all bits"""
    parity = 0  # even (base case, if x = 0)
    while x:  # iterate over x
        parity = parity ^ (x & 1)  # check last digit and flip parity 
        x = x >> 1  # right shift
    return parity


def find_parity_Ok(x):
    """return parity, O(k) where k is number of 1-bits
    (linear with better best-case if input has few 1s and many zeros)"""
    parity = 0
    while x:
        # flip rightmost 1-bit of x
        x = x & (x-1)
        parity = parity ^ 1  # alternate parity whenever bit is flipped
    return parity


def find_parity_hashmap(x, l=2):
    """l = length of sub-words to use as cache
    space complexity: 2**l combinations of l bits each"""
    parity = 0
    mask = sum([2**n for n in range(l)])  #or int("1"*l, base=2)
    cache = {}
    while x:
        last_l_bits = x & mask
        if last_l_bits not in cache:
            cache[last_l_bits] = find_parity_Ok(last_l_bits)
        parity = parity ^ cache[last_l_bits]  # if parity is 0, then ^ 0 = 0 (even + even), ^ 1 = 1 (even + odd). if 1^1, odd+odd=even.
        x = x >> l  # shift
    print(cache)
    return parity


def find_parity_assoc(x, l=64):
    """uses associative property of xor to find the parity by xor'ing 
    groups of bits. l = word size"""
    n = l // 2  # must be power of 2
    while n >= 1:
        x ^= (x >> n)  # 1101 ^ 0111 = 1010
        n //= 2
        print(bin(x), n)
    # return last bit
    return x & 1


def swap_bit(x, a, b):
    """swap bits of x at index a and index b (where index 0 is the LSB.)"""
    # get bits at a and b
    # check if different, if so "swap" by flipping the bits of each
    if (x >> a) & 1 != (x >> b) & 1:
        # mask = (2**a + 2**b)
        mask = (1 << a) | (1 << b) # better way of generating bit mask directly
        x = x ^ mask
    return x