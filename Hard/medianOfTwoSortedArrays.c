// Link to problem: https://leetcode.com/problems/median-of-two-sorted-arrays/

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int size = nums1Size + nums2Size;
    int *mergedArray = (int *) malloc((size) * sizeof(int));
    for (int i = 0; i < size; i++) {
        if (i < nums1Size)
            mergedArray[i] = nums1[i]; 
        else
            mergedArray[i] = nums2[i - nums1Size];
    }
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - 1 - i; j++) {
            if (mergedArray[j] > mergedArray[j + 1]) {
                int temp = mergedArray[j];
                mergedArray[j] = mergedArray[j + 1];
                mergedArray[j+1] = temp; 
            }
        }
    }
    if ((nums1Size + nums2Size)%2 == 0) {
        return (mergedArray[size/2 - 1] + mergedArray[size/2]) / 2.0;
    } else {
        return mergedArray[size/2];
    }
}