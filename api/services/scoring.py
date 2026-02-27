def score_answers(detected, answer_key):

    correct = 0
    wrong = 0

    for q, ans in answer_key.items():

        if str(detected.get(int(q))) == ans:
            correct += 1
        else:
            wrong += 1

    total = len(answer_key)

    score = (correct / total) * 100 if total else 0

    return {
        "correct": correct,
        "wrong": wrong,
        "score": score
    }
