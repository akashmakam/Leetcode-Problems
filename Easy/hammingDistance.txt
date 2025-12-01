// Link to problem: https://leetcode.com/problems/hamming-distance/

int hammingDistance(int x, int y) {
    int max_val = x | y;
    int range = 0;
    while (max_val > 0) {
        max_val >>= 1;
        range++;
    }
    int distance = 0, result = 0;
    x ^= y;
    for (int i = 0; i < range; i++)
        distance += ((x & (1 << i)) != 0)? 1 : 0;
    return distance;
}


class Solution(object):
    def hammingDistance(self, x, y):
        count = 0
        for i in range(32):
            a = x >> i
            b = y >> i
            if a & 1 != b & 1:
                count += 1
        return count

class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count("1")
