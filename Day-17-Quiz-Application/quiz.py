
questions = [
    {
        "question": "Which language is used for AI and Machine Learning?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["A. Stack", "B. Tree", "C. Queue", "D. Graph"],
        "answer": "C"
    },
    {
        "question": "Which company developed Python?",
        "options": [
            "A. Microsoft",
            "B. Google",
            "C. Apple",
            "D. Python Software Foundation community (originally created by Guido van Rossum)"
        ],
        "answer": "D"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D. **"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0

    print("\nPYTHON QUIZ APPLICATION ")
    print("Answer the following questions!")
    print("Enter A, B, C, or D.\n")

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:
            user_answer = input("Your answer: ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Invalid choice! Enter A, B, C, or D.")

        if user_answer == question["answer"]:
            print("Correct answer! 🎉")
            score += 1
        else:
            print(
                f"Wrong answer! Correct answer: {question['answer']}"
            )

    total = len(questions)
    percentage = (score / total) * 100

    print("\n====== QUIZ RESULT ======")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {total - score}")
    print(f"Final Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent performance! 🏆")
    elif percentage >= 50:
        print("Good job! Keep practicing.")
    else:
        print("Keep learning and try again!")

run_quiz()