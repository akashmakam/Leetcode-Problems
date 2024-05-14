// Link to problem: https://leetcode.com/problems/string-to-integer-atoi/

int myAtoi(char* s) {
    while (isspace(*s))
        s++;

    int sign = 1;
    if (*s == '-' || *s == '+') {
        if (*s == '-')
             sign = -1;
        s++;
    }

    long long sum = 0;
    while (isdigit(*s)) {
        sum = sum * 10 + (*s - '0');
        if (sum * sign > INT_MAX) return INT_MAX;
        if (sum * sign < INT_MIN) return INT_MIN;
        s++;
    }

    return sum * sign;
}