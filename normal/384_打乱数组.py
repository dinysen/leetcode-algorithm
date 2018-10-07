import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.output = nums;
        self.origin = nums[:];

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin;
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        """
        运用Knuth shuffle
        """
        output = self.output;
        for i in range(len(output)):
            index = random.randint(0,i);
            output[i],output[index] = output[index],output[i];
        # return random.shuffle(output);
        return output;
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()