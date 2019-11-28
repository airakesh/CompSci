# Find frequency of each word in a given list.
class Solution:
    ## @params A: a strings
    ## @return: an integer
    def freq(self, A):
        str_list = A.split()
        # gives set of unique words
        unique_words = set(str_list)

        for words in unique_words:
            print('Frequency of ', words , 'is :', str_list.count(words))

# Test code
if __name__ == '__main__':
    s = Solution()
    A ='apple mango apple orange orange apple guava mango mango'

    s.freq(A)
