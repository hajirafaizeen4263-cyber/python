#Quiz Game
import time

while True:
    score = 0

    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "2. Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "3. Which symbol is used for comments in Python?",
            "options": ["A. //", "B. #", "C. /* */", "D. --"],
            "answer": "B"
        },
        {
            "question": "4. Which data type stores True or False values?",
            "options": ["A. int", "B. float", "C. bool", "D. string"],
            "answer": "C"
        },
        {
            "question": "5. Which loop is used when the number of iterations is known?",
            "options": ["A. while", "B. for", "C. do-while", "D. repeat"],
            "answer": "B"
        }
    ]

    print("\n===================================")
    print("       PYTHON QUIZ GAME")
    print("===================================")
    print("Choose the correct option (A, B, C, or D).")
    print("The quiz begins now!\n")

    start_time = time.time()

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer: ").upper()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!")
            print("Correct Answer:", q["answer"], "\n")

        time.sleep(1)

    end_time = time.time()
    total_time = end_time - start_time

    percentage = (score / len(questions)) * 100

    print("\n===================================")
    print("          QUIZ RESULT")
    print("===================================")
    print("Total Questions :", len(questions))
    print("Correct Answers :", score)
    print("Wrong Answers   :", len(questions) - score)
    print("Percentage      : {:.2f}%".format(percentage))
    print("Time Taken      : {:.2f} seconds".format(total_time))

    if percentage == 100:
        print("Excellent! Perfect Score!")
    elif percentage >= 60:
        print("Good Job!")
    else:
        print("Keep Practicing!")

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for playing the Python Quiz Game!")
        break