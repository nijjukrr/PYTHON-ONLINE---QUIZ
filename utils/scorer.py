def calculate_score(questions, answers, index=0):
    """
    Recursive function to calculate the score.
    Base case: If index equals the length of questions, all questions have been processed.
    Recursive case: Add 1 if the answer at current index is correct, then call itself for the next index.
    """
    if index == len(questions): 
        return 0
    
    # Check if answer exists for this index
    if index >= len(answers) or answers[index] is None:
        correct = 0
    else:
        # Comparison logic
        correct = 1 if str(answers[index]) == str(questions[index]['answer']) else 0
        
    return correct + calculate_score(questions, answers, index + 1)

def calculate_bonus(time_limit, time_taken):
    """Award time bonus points: bonus = max(0, (time_limit - time_taken) // 30)"""
    return max(0, (time_limit - int(time_taken)) // 30)
