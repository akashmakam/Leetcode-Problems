bool isPowerOfThree(int n) {
    double logarithm = log(n) / log(3);
    int integerPart = (int)(logarithm + 0.5); // Round to the nearest integer
    printf("%1f\n%d\n", logarithm, integerPart);
    double fractionalPart = logarithm - integerPart;
    return (fractionalPart == 0);
}