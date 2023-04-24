import ctypes as ns
import time

with open('text1_message.txt', 'r') as f:
    lines = f.readlines()

l0 = []
PtR0 = []
r1 = []
delta = 0x9e3779b9
N = 2 ** 32
for line in lines:
    numbers = line.split()
    l0.append(int(numbers[0]) % N )
    PtR0.append(int(numbers[1]) % N )
    r1.append(int(numbers[3]) % N )
    print("L0", l0)
    print("R0",PtR0)
    print("R1",r1)


start_time = time.time()

key = []


time_start = time.time()
for k0 in range(0, 4294967295):

    key1_0 = ((PtR0[0] << 4) + k0 ^ PtR0[0] + delta ^ (r1[0] - l0[0])) - (PtR0[0] >> 5)
    key1_1 = ((PtR0[1] << 4) + k0 ^ PtR0[1] + delta ^ (r1[1] - l0[1])) - (PtR0[1] >> 5)
    key1_2 = ((PtR0[2] << 4) + k0 ^ PtR0[2] + delta ^ (r1[2] - l0[2])) - (PtR0[2] >> 5)
    key1_3 = ((PtR0[3] << 4) + k0 ^ PtR0[3] + delta ^ (r1[3] - l0[3])) - (PtR0[3] >> 5)
    key1_4 = ((PtR0[4] << 4) + k0 ^ PtR0[4] + delta ^ (r1[4] - l0[4])) - (PtR0[4] >> 5)
    key1_5 = ((PtR0[5] << 4) + k0 ^ PtR0[5] + delta ^ (r1[5] - l0[5])) - (PtR0[5] >> 5)
    key1_6 = ((PtR0[6] << 4) + k0 ^ PtR0[6] + delta ^ (r1[6] - l0[6])) - (PtR0[6] >> 5)
    key1_7 = ((PtR0[7] << 4) + k0 ^ PtR0[7] + delta ^ (r1[7] - l0[7])) - (PtR0[7] >> 5)
    key1_8 = ((PtR0[8] << 4) + k0 ^ PtR0[8] + delta ^ (r1[8] - l0[8])) - (PtR0[8] >> 5)
    key1_9 = ((PtR0[9] << 4) + k0 ^ PtR0[9] + delta ^ (r1[9] - l0[9])) - (PtR0[9] >> 5)
    key1_10 = ((PtR0[10] << 4) + k0 ^ PtR0[10] + delta ^ (r1[10] - l0[10])) - (PtR0[10] >> 5)
    key1_11 = ((PtR0[11] << 4) + k0 ^ PtR0[11] + delta ^ (r1[11] - l0[11])) - (PtR0[11] >> 5)
    key1_12 = ((PtR0[12] << 4) + k0 ^ PtR0[12] + delta ^ (r1[12] - l0[12])) - (PtR0[12] >> 5)
    key1_13 = ((PtR0[13] << 4) + k0 ^ PtR0[13] + delta ^ (r1[13] - l0[13])) - (PtR0[13] >> 5)
    key1_14 = ((PtR0[14] << 4) + k0 ^ PtR0[14] + delta ^ (r1[14] - l0[14])) - (PtR0[14] >> 5)
    key1_15 = ((PtR0[15] << 4) + k0 ^ PtR0[15] + delta ^ (r1[15] - l0[15])) - (PtR0[15] >> 5)
    key1_16 = ((PtR0[16] << 4) + k0 ^ PtR0[16] + delta ^ (r1[16] - l0[16])) - (PtR0[16] >> 5)
    key1_17 = ((PtR0[17] << 4) + k0 ^ PtR0[17] + delta ^ (r1[17] - l0[17])) - (PtR0[17] >> 5)
    key1_18 = ((PtR0[18] << 4) + k0 ^ PtR0[18] + delta ^ (r1[18] - l0[18])) - (PtR0[18] >> 5)
    key1_19 = ((PtR0[19] << 4) + k0 ^ PtR0[19] + delta ^ (r1[19] - l0[19])) - (PtR0[19] >> 5)




    # To make sure k1 value is under range of 0 and 2^32 -1
    k1_1 = (key1_1 % 0xffffffff)

    if (
            key1_1 == key1_2 == key1_3 == key1_4 == key1_5 == key1_6 == key1_7 == key1_8 == key1_9 == key1_10 == key1_11 == key1_12 == key1_13 == key1_14 == key1_15):
        print("Key Found !!!")
        print("K0 is", k0)
        print("K1 is", key1_1)
        break


end_time = time.time()
time = end_time - time_start
print("Total run time for finding key for set1 is :", time, "s.")
