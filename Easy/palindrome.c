// Link to problem: https://leetcode.com/problems/palindrome-number/

bool isPalindrome(int x) {
    int digit;
    long long num = x, reversedNum = 0;
    if (num < 0)
        return false;
    while(num != 0) {
        digit = num%10;
        reversedNum = (reversedNum * 10) + digit;
        if (reversedNum > INT_MAX || reversedNum < INT_MIN)
            return false;
        num /= 10;
    }
    return (reversedNum == x);
}