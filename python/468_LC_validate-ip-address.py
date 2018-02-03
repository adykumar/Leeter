"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

"""
Things to look for:
ipv4:  -0 in a segment like 10.-0.1.1
ipv4:  starts with 0 like 10.02.11.11
ipv4:  non numerics in the segments 1a2.100.34.1
ipv6:  characters beyond hex
ipv6:  no chars between ::  like 0a:11:1234:::1d:6b:cab


Complexity: O(n) where n in length of the address
"""

class Solution(object):
    def validate4(self,parts):
        if len(parts)!=4: return False
        #lis= ['0','1','2','3','4','5','6','7','8','9']
        #st= set(lis)
        for each in parts:
            if each =="0": 
                continue
            if each=="" or each[0]=="0":
                return False
            try:
                if int(each)>=1 and int(each)<=255: 
                    continue
            except:
                pass
            return False
        return True
    
    def validate6(self,parts):
        if len(parts)!=8: return False
        lis= ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        st= set(lis)
        for part in parts:
            if part=="" or len(part)>4: return False
            for ch in part:
                if ch.lower() not in st:
                    return False
        return True
    
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        if "." in IP:
            parts= IP.split(".")
            if self.validate4(parts):
                return "IPv4"
            
        if ":" in IP:
            parts= IP.split(":")
            if self.validate6(parts):
                return "IPv6"
            
        return "Neither"
            

if __name__=="__main__":
	obj= Solution()
	testcases= ["1a2.11..1","1...1","10.71.119.118","256.256.256.256","1.1.-0.0","2001:0db8:85a3:0:0:8A2E:0370:7334", "2001:0db8:85a3:0::8A2E:0370:7334"]       
	for test in testcases:
		print test, "->", obj.validIPAddress(test)     
