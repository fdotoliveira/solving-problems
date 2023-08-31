class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Function to pair if sequence contains valid parenthesis
        :param s: Sequence of brackets
        :return: True is sequence is valid else False
        '''
        if len(s)%2 != 0:
            return False

        bracket_map = {'(':')','{':'}','[':']'}    
        stack = []

        for char in s:
            # push opening bracket
            if char in bracket_map.keys():
                stack.append(char)
            else:
                # empty stack
                if stack == []:
                    return False
                # closing bracket then pop stack top
                open_brac = stack.pop()
                # matching brackets type
                if char != bracket_map[open_brac]:    
                    return False

        # if the stack is empty here, all opening brackets have been matched with their
        # corresponding closing brackets, ensuring a valid string.
        return len(stack) == 0

if __name__ == '__main__':
   s = '{[()]}'
   print(f'Is {s} valid ? : {Solution().isValid(s)}')
   s = '{((}'
   print(f'Is {s} valid ? : {Solution().isValid (s)}')        