// Link to problem: https://leetcode.com/problems/valid-parentheses/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char pair(char s) {
    switch(s) {
        case ']': return '[';
        case '}': return '{';
        case ')': return '(';
    }
    return '\0';
}

bool isValid(char* s) {
    int length = strlen(s), top = -1;
    char stack[length];
    for (int i = 0; i < length; i++) {
        switch(s[i]) {
            case '[':
            case '{':
            case '(': stack[++top] = s[i]; break;
            case ']':
            case '}':
            case ')': {
                if (top == -1)
                    return false;
                if (pair(s[i]) != stack[top])
                    return false;
                else
                    top--;
            }
        }
    }
    return top == -1;
}

int main() {
    char s1[] = "{[()]}";
    char s2[] = "{[(])}";
    char s3[] = "{{{{{{";
    char s4[] = "}";
    printf("%s is %s\n", s1, isValid(s1) ? "valid" : "invalid");
    printf("%s is %s\n", s2, isValid(s2) ? "valid" : "invalid");
    printf("%s is %s\n", s3, isValid(s3) ? "valid" : "invalid");
    printf("%s is %s\n", s4, isValid(s4) ? "valid" : "invalid");
    return 0;
}