 """nested Lists

 Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
 student(s) having the second lowest grade.

 note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

 Input Format
 The first line contains an integer, n, the number of students. 
 The 2n subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
 their grade.

 Constraints
 2 <= n <= 5
 There will always be one or more students having the second lowest grade.

 Output Format
 Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
 alphabetically and print each one on a new line.


 Enter your code here. Read input from STDIn. Print output to STDOUT"""

n = int(input())
student = []
for i in range(2 * n):
    student.append(input().split())
grade = {}
for j in range(0, len(student), 2):
    grades[student[j][0]] = float(student[j + 1][0])
results = []
match = sorted(set(grade.values()))[1]
for pupil in grade.keys():
    if grade[pupil] == match:
        results.append(pupil)
for r in sorted(results):
    print (r)