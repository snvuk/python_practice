from operator import itemgetter

def sort_tuples(tuples_list):
    sorted_tuples = sorted(tuples_list, key=itemgetter(0, 1, 2))
    return sorted_tuples

input_tuples = [
    ('Tom', 19, 80),
    ('John', 20, 90),
    ('Jony', 17, 91),
    ('Jony', 17, 93),
    ('Json', 21, 85)
]

sorted_tuples = sort_tuples(input_tuples)
print(sorted_tuples)
