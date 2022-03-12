
def main():
    grades ={
        'English':int(input("English grade: ")),
        'Math': int(input('Math grade: ')),
        'Global Studies': int(input('Global Studies grade: ')),
        'Art': int(input('Art grade: ')),
        'Music': int(input('Music grade: ')),
    }
    grades_sum = sum(grades.values())
    courses_count = len(grades)
    average_score = grades_sum / courses_count
    print(f'Your average score is: {average_score}')

main()
