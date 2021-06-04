from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] 

for q in question_data:
    text = q['text']
    answer = q['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

still_q = True
while still_q:
    quiz.next_question()
    still_q = quiz.still_has_question()

