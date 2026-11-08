class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    
        ones = students.count(1)
        zeros = students.count(0)
        for i in range(len(sandwiches)):
            if sandwiches[i] == 0 and zeros:
                zeros -=1
            elif sandwiches[i] == 1 and ones:
                ones -= 1
            else:
                return ones + zeros
        return ones + zeros
        


            
            
