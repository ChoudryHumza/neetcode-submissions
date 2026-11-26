class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count = defaultdict(int)
        length = len(students)
        for stu in students:
            count[stu] +=1
        
        for sw in sandwiches:
            if count[sw]:
                count[sw] -=1
                length -=1
            else:
                break
        
        return length