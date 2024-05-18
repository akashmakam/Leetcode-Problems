// Link to problem: https://leetcode.com/problems/reverse-integer/description/

int reverse(int x) {
    int num = 0;
    int factor = 1, digit = 0;
    while (x != 0) {
        digit = x % 10;
        x /= 10;
        if (num > INT_MAX / 10 || num < INT_MIN / 10) {
            return 0;
        }
        num = (num * 10) + diff;
    }
    return num;
}