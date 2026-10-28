class Solution:
    def isPalindrome(self, s: str) -> bool:
        # An empty string is a palindrome
        #If there a non-alphanumeric char they need to be remove
        # the strings should be stripped of spaces

        #Strip the whitespaces from the string and convert to lowercase
        #Check if the chars in the string are alphanumeric: if not remove them from the string
        #the technique to use:Two pointers. 
        #Intialze 2 different pointers one at the beginning of the string and the other at the end
        #A while loop that runs as long as the left pointer is greater than the right
        #check if the chars at both pointers are equal, if not, i will return false:
        #else keep updating the pointers
        
        if s=="":
            return True
        new_string=''.join([char.lower() for char in s if char.isalnum()])
        left_ptr=0
        right_ptr=len(new_string)-1
        while left_ptr < right_ptr:
            if new_string[left_ptr] !=new_string[right_ptr]:
                return False
            else:
                left_ptr+=1
                right_ptr-=1
                
        return True

