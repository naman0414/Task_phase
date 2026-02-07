from questions import question

question_prompts=[
    "who is a boy\n a)aryan\n b)idant\n c)naman\n",
    "who is hot\n a)idant\n b)aryan\n c)naman\n",
    ]

questions=[
    question(question_prompts[0],"c"),
    question(question_prompts[1],"a"),
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("your score is "+str(score))



run_test(questions)       

