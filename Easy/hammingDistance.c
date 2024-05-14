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