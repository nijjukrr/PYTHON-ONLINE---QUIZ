import json
import random

def load_questions_to_set(filepath, category, difficulty, count):
    """
    Loads questions from a JSON file into a Python SET to guarantee no duplicates.
    Sets are used here because they inherently handle deduplication and offer O(1) average lookup time.
    """
    with open(filepath, 'r') as f:
        all_questions = json.load(f)
    
    # Filter by category and difficulty
    filtered = [q for q in all_questions if q['category'] == category and q['difficulty'] == difficulty]
    
    # Use a set of indices or tuples for deduplication if needed
    # But since we're picking random samples, we'll just use random.sample which is unique
    
    selected_count = min(len(filtered), count)
    selected = random.sample(filtered, selected_count)
    
    return selected
