class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n);
        if len(b) < 34:
            b = "0b" + "0"*(34-len(b)) + b[2:];
        b_rev = "0b" + b[2:][::-1];
        return int(b_rev,2);