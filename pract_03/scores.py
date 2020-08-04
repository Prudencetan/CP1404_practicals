from random import randint

def main():
    number_of_scores = int(input("Enter number of scores: "))
    results_file = open("results.txt", 'w')
    for i in range(number_of_scores):
        score = randint(0,101)
        grade = get_grade(score)
        print(score,"is",grade, file=results_file)
    results_file.close()

def get_grade(score):
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")


if __name__ == '__main__':
    main()