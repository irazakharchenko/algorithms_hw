from math import sqrt

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class  HashTable:
    PRIME_NUM = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061,  3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 299993]
    POWER_2 = [ 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
    A = (sqrt(5) - 1) / 2


    def __init__(self, hash_type, values):
        self.hash_type = hash_type
        self.val = values
        self.counterCollis = 0
        if self.hash_type == 1:
            self.add_element_1()
        elif self.hash_type == 2:
            self.add_element_2()
        elif self.hash_type == 3:
            self.add_element_3()


    def nearest(self, n):
        left = 0
        typeToUse = self.PRIME_NUM
        if self.hash_type == 2:
            typeToUse = self.POWER_2
        right = (len(typeToUse))
        while left < right - 1:
            if n > typeToUse[(right + left)//2]:
                left = (right + left)//2
            else:
                right = (right + left)//2
        return typeToUse[left]

    def add_element_1(self):
        self.m = self.nearest(3 * len(self.val))
        self.hash_table = [None]*self.m
        for el in self.val:
            ind = self.hash_1(el)
            if self.hash_table[ind] is not None:
                # print(ind)
                self.hash_table[ind] = Node(el, self.hash_table[ind])
                self.counterCollis += 1
            else:
                self.hash_table[ind] = Node(el)

    def add_element_2(self):
        self.m = self.nearest(3 * len(self.val))
        self.hash_table = [None] * self.m
        for el in self.val:
            ind = self.hash_2(el)
            if self.hash_table[ind] is not None:
                # print(ind)
                self.hash_table[ind] = Node(el, self.hash_table[ind])
                self.counterCollis += 1
            else:
                self.hash_table[ind] = Node(el)

    def add_element_3(self):
        self.m = self.nearest(3 * len(self.val))
        self.hash_table = [None] * self.m
        for el in self.val:
            ind = self.hash_1(el)
            if self.hash_table[ind] is not None:
                i = 1
                while self.hash_table[ind] is not None:

                    ind = self.hash_3(ind, i)
                    i = (1 + i) % self.m

            else:
                self.hash_table[ind] = Node(el)

    def hash_2(self, el):
        return int(self.m * ((el * self.A) % 1))

    def hash_1(self, el):
        return el % self.m

    def hash_3(self, hash_el, i ):
        return (hash_el + i) % self.m

    def get_collisions_amount(self):
        return self.counterCollis

    def find_sum(self, s):
        sums = []
        for el_same_hash in self.hash_table:
            if el_same_hash is not None:
                while el_same_hash is not None:
                    el = el_same_hash

                    elAdd = s - el.value
                    if self.hash_type == 1:
                        if self.hash_1(el.value) < self.hash_1(elAdd):
                            b = self.find_number_to_add(elAdd)
                            if b:
                                sums.append(( elAdd, el.value))
                    elif self.hash_type == 2:
                        if self.hash_2(el.value) < self.hash_2(elAdd):
                            b = self.find_number_to_add(elAdd)
                            if b:
                                sums.append(( elAdd, el.value))
                    elif self.hash_type == 3:
                        
                        b = self.find_number_to_add(elAdd)
                        if b:
                            sums.append(( elAdd, el.value))
                    el_same_hash = el_same_hash.next

        if len(sums) == 0:
            return None

        return sums[0][0], sums[0][1]


    def find_number_to_add(self, numAdd):
        if self.hash_type == 1:
            index = self.hash_1(numAdd)
            cur = self.hash_table[index]
            if cur is None:
                return False
            while cur.value != numAdd and cur.next != None:
                cur = cur.next
            return cur.value == numAdd
        if self.hash_type == 2:
            index = self.hash_2(numAdd)
            cur = self.hash_table[index]
            if cur is None:
                return False
            while cur.value != numAdd and cur.next != None:
                cur = cur.next
            return cur.value == numAdd
        if self.hash_type == 3:
            index = self.hash_1(numAdd)
            cur = self.hash_table[index]
            if cur is None:
                return False
            while cur != None and cur.value != numAdd:
                index = (1 + index) % self.m
                cur = self.hash_table[index]
            return cur != None and cur.value == numAdd






#m = [8, 4, 6, 8, 19, 7, 4, 13, 13, 12, 9, 20, 20, 18, 1, 18, 13, 10, 6, 10, 16, 18, 19, 4, 3, 19, 14, 9, 16, 3, 15, 1, 5, 15, 10, 16, 19, 1, 2, 16, 16, 4, 3, 14, 4]
#m = [8, 12, 6, 9, 19]
m = [19833, 7843, 10784, 13773, 864, 3981, 12303, 8631, 14725, 1836, 1569, 9365, 3055, 5873, 5002, 11934, 731, 18691, 14110, 11949, 9034, 15442, 11086, 4349, 5497, 8559, 3722, 9374, 4516, 4877, 8309, 12907, 16764, 19847, 9875, 18935, 7628, 4739, 5177, 588, 6812, 2531, 805, 18460, 15712]
h = HashTable(2, m)
print(h.get_collisions_amount())
for i in range(7845,  8968):
    if h.find_sum(i) is not None:
        print(h.find_sum(i))