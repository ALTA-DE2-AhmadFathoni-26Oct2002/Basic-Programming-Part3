def palindrome(input_string):
    lenght = len(input_string)
    for i in range (0, lenght//2):
        if input_string[i] == input_string[lenght -i -1]:
            return True
        
    return False

if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False