class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        result = ''
        carry = 0
        
        for i in range(max_len - 1, -1, -1):
            total_sum = carry
            total_sum += int(a[i])
            total_sum += int(b[i])
            
            bit = total_sum % 2
            carry = total_sum // 2
            
            result = str(bit) + result
        
        if carry != 0:
            result = '1' + result
        
        return result