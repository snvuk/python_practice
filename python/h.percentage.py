didn't complete need to complete

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        line = input().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        student_marks[name] = scores

    query_name = input()

    if query_name in student_marks:
        avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])

