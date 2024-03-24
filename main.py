def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the chemical symbol for water?": "H2O"
    }
    score = 0

    print("Welcome to the Quiz!")
    for question, answer in questions.items():
        user_answer = input(question + "\nYour Answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer)
        print("Your current score is:", score)
        print("-" * 30)

    print("Quiz Complete!")
    print("Your final score is:", score)
    if score == len(questions):
        print("Congratulations! You got all questions correct!")
    elif score >= len(questions) // 2:
        print("Well done! You did a good job.")
    else:
        print("Better luck next time.")

quiz()