// Link to problem: https://leetcode.com/problems/power-of-two

bool isPowerOfTwo(int n) {
    double logarithm = log2(n);
    int integerPart = logarithm / 1.0;
    double fractionalPart = logarithm - integerPart;
    return (fractionalPart == 0);
}

bool isPowerOfTwo(int n) {
     return n>0 && (!(2147483648%n));
}