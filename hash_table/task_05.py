from math import sqrt

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class  HashTable:
    PRIME_NUM = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 2999,  299993]
    POWER_2 = [ 2, 4, 8, 16,  2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
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
        elif self.hash_type == 4:
            self.add_element_4()
        elif self.hash_type == 5:
            self.add_element_5()


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

            self.hash_table[ind] = Node(el)

    def add_element_4(self):
        self.m = self.nearest(3 * len(self.val))
        self.hash_table = [None] * self.m
        for el in self.val:
            ind = self.hash_1(el)
            if self.hash_table[ind] is not None:
                i = 1
                while self.hash_table[ind] is not None:
                    ind = self.hash_4(el, i)
                    i = (1 + i)

            self.hash_table[ind] = Node(el)

    def add_element_5(self):
        self.m = self.nearest(3 * len(self.val))
        self.hash_table = [None] * self.m
        for el in self.val:
            ind = self.hash_1(el)
            if self.hash_table[ind] is not None:
                i = 1
                while self.hash_table[ind] is not None:
                    ind = self.hash_5(el, i)
                    i = (1 + i)
            self.hash_table[ind] = Node(el)


    def hash_1(self, el):
        return el % self.m

    def hash_2(self, el):
        return int(self.m * ((el * self.A) % 1))

    def hash_3(self, hash_el, i = 0):
        return (hash_el + i) % self.m

    def hash_4(self, el, i = 0):
        return (self.hash_1(el) + 5 * i + 3 * (i**2)) % self.m

    def hash_5(self, el, i = 0):
        return (self.hash_1(el) + i *self.hash_4(el, i) ) % self.m

    def get_collisions_amount(self):
        return self.counterCollis

    def find_sum(self, s):
        sums = []
        for el_same_hash in self.hash_table:
            if el_same_hash is not None:
                while el_same_hash is not None:
                    el = el_same_hash

                    elAdd = s - el.value
                    if elAdd < 0:
                        break
                    if self.hash_type == 1 :
                        if self.hash_1(el.value) < self.hash_1(elAdd):
                            b = self.find_number_to_add(elAdd)
                            if b:
                                sums.append(( elAdd, el.value))
                    elif self.hash_type == 2:
                        if self.hash_2(el.value) < self.hash_2(elAdd):
                            b = self.find_number_to_add(elAdd)
                            if b:
                                sums.append(( elAdd, el.value))
                    elif self.hash_type == 3 or self.hash_type == 4 or self.hash_type == 5:
                        b = self.find_number_to_add(elAdd)
                        if b:
                            sums.append((elAdd, el.value))

                    el_same_hash = el_same_hash.next


        if len(sums) == 0:
            return None

        return sums[0][0], sums[0][1]


    def find_number_to_add(self, numAdd):
        index = self.hash_1(numAdd)
        cur = self.hash_table[index]
        if self.hash_type == 1:

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

            if cur is None:
                return False
            while cur != None and cur.value != numAdd:
                index = self.hash_3(numAdd, index)
                cur = self.hash_table[index]
            return cur != None and cur.value == numAdd
        if self.hash_type == 4:
            i = 0
            while cur != None and cur.value != numAdd:
                index = self.hash_4(numAdd, i)
                cur = self.hash_table[index]
                i = (i + 1)
            return cur != None and cur.value == numAdd
        if self.hash_type == 5:
            if cur is None:
                return False
            i = 0
            while cur != None and cur.value != numAdd:
                index = self.hash_5(numAdd, i)
                cur = self.hash_table[index]
                i = (i + 1) % self.m
            return cur != None and cur.value == numAdd






m = [8, 4, 6, 8, 19, 7, 4, 13, 13, 12, 9, 20, 20, 18, 1, 18, 13, 10, 6, 10, 16, 18, 19, 4, 3, 19, 14, 9, 16, 3, 15, 1, 5, 15, 10, 16, 19, 1, 2, 16, 16, 4, 3, 14, 4]
#m = [8, 12, 6, 9, 19]
#m = [19833, 7843, 10784, 13773, 864, 3981, 12303, 8631, 14725, 1836, 1569, 9365, 3055, 5873, 5002, 11934, 731, 18691, 14110, 11949, 9034, 15442, 11086, 4349, 5497, 8559, 3722, 9374, 4516, 4877, 8309, 12907, 16764, 19847, 9875, 18935, 7628, 4739, 5177, 588, 6812, 2531, 805, 18460, 15712]
#m = [237, 4, 103, 161, 109, 108, 270, 115, 1, 157, 109, 14, 17, 290, 266, 172, 73, 192, 293, 67, 121, 231, 66, 244, 94, 156, 95, 52, 284, 231, 43, 45, 229, 25, 194, 30, 47, 7, 55, 55, 142, 79, 185, 140, 16, 89, 135, 44, 199, 216]
#m = [6, 13, 20, 42, 44, 26, 19, 49, 19, 42, 16, 5, 45, 1, 35, 11, 16, 12, 37, 20, 44, 34, 25, 25, 48, 34, 36, 13, 32, 42, 35, 15, 3, 37, 16, 7, 17, 25, 38, 1, 24, 48, 33, 10, 6, 35, 44, 27, 43, 25]
h = HashTable(3, m)
k = HashTable(4, m)
print(k.get_collisions_amount())
for i in range(5866, 5875):
    h_f = h.find_sum(i)
    k_f = k.find_sum(i)
    if h_f is not None and k_f is not None:
        if h_f != k_f:
            #print(i, h_f, k_f)
            r = 2
    elif h_f is not None or k_f is not None :
        if h_f is not None:
            print("problem h_f ", i, h_f)
            r = 3
        else:
            print("problem k_f ", i, k_f)
            r = 5