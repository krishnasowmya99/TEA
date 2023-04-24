# TEA


Tiny Encryption Algorithm (TEA)

TEA is an iterated block cipher that encrypts 64 bit blocks using a 128 bit key. It uses a relatively weak nonlinear mixing function over many rounds. The suggested number of rounds in 32, though fewer would probably suffice. There are no precomputed tables, key schedules, etc. TEA is not a Feistel cipher. 


The program takes input from the text1_message.txt & text2_message.txt file, which contains several lines of numbers. It reads each line and splits it into four integers. The first two integers in each line are used as the initial values of the L0 and Pseudo-random number generator (PRNG) R0 variables, respectively. The third integer is ignored, and the fourth integer is used as the initial value of the R1 variable.

The program then performs a brute-force search to find the encryption key that can decrypt the given data. The key is a 32-bit integer, and the program checks all possible values for the key. For each key value, the program calculates a new set of 16 keys using the XTEA algorithm and compares them with the given set of keys. If the new set of keys matches the given set of keys, the program prints the key value and stops.
