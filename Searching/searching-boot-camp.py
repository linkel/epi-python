# When objects are comparable, you can use good old library search functions for them.

# But if you make some user-defined types, you've got to implement some kind of comparison.

# Make sure it's got basic bits like being transitive and stuff! Otherwise you WON'T FIND YOUR BABY when searching, even though she's there!
# Horrifying.

# Pretending we have an array of students sorted by descending GPA,
# and we tiebreak on name. 
import bisect

class Student(object):
    def __init__(self, name, gpa = 0.0):
        self.name = name
        self.gpa = gpa

a = Student("Abarth", 3.9)
b = Student("Anansi", 3.9)
c = Student("Ming", 4.0)
d = Student("Roac", 3.5)

sorted_arr = [c,a,b,d]

def comp_gpa(student: Student):
    return (-student.gpa, student.name)

def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target

print(search_student(sorted_arr, d, comp_gpa))

# I'm not sure I like the way this got set up. Looks like it just tells me if the student is in the array or not.
# And I need the student object. Does this work if I make up a new object? Prob not.

obj = Student("Ming", 4.0)
print(search_student(sorted_arr, obj, comp_gpa))

# No I want to search off a student name dammit. 


def search_student_not_same_obj(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i].name == target.name and students[i].gpa == target.gpa

obj = Student("Ming", 4.0)
print(search_student_not_same_obj(sorted_arr, obj, comp_gpa))
# Okay that's a bit better. Bah. This snippet probably made more sense in C++, the original language this book was written in.

