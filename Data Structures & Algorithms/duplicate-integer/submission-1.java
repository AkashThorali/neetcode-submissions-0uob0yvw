class Solution {
    public boolean hasDuplicate(int[] nums) {
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            index++;
            for (int j = index; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
