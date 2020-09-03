import random
OUT_FILE = "results.txt"


def main():
    score_count = int(input("Number of scores: "))
    out_file = open(OUT_FILE, "w")
    for i in range(score_count):
        score = random.randint(0, 100)
        result = determine_result(score)
        print("{} is {}".format(score, result))
        print("{} is {}".format(score, result), file=out_file)
    out_file.close()


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
