def print_line(char="-", times=50):
    print(char * times)

def print_header(title, char="=", times=50):
    print(char * times)
    print(title.center(times))
    print(char * times)

def total_marks(*marks):
    return sum(marks)
