from fastapi import APIRouter, HTTPException
import random

router = APIRouter(tags=["quiz"])

# I actually could have added this to a collection in mongodb
questions = [
    {
        "id": 1,
        "text": "What command lists directory contents?",
        "options": ["ls", "cd", "rm", "pwd"],
        "correct": "ls"
    },
    {
        "id": 2,
        "text": "Which command searches for text in files?",
        "options": ["find", "grep", "locate", "cat"],
        "correct": "grep"
    },
    {
        "id": 3,
        "text": "What changes file permissions?",
        "options": ["chmod", "chown", "mv", "cp"],
        "correct": "chmod"
    },
    {
        "id": 4,
        "text": "Which command displays the current directory?",
        "options": ["dir", "pwd", "path", "where"],
        "correct": "pwd"
    },
    {
        "id": 5,
        "text": "What removes a file?",
        "options": ["rm", "del", "erase", "unlink"],
        "correct": "rm"
    }
]

game_state = {"high_score": 0}
# god would hate me for not dockerizing this repo
@router.get("/question")
async def get_question():
    question = random.choice(questions)
    return {
        "id": question["id"],
        "text": question["text"],
        "options": question["options"]
    }

@router.post("/answer")
async def submit_answer(data: dict):
    question_id = data.get("id")
    answer = data.get("answer")
    score = data.get("score", 0)

    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        # BUG (old code): No proper error response for invalid question ID
        # CHANGES: Raise HTTPException for invalid question ID, but also return old error dict
        error_response = {"error": "Invalid question ID"}
        # Optionally log or handle error_response here
        raise HTTPException(status_code=400, detail="Invalid question ID")
        return error_response

    is_correct = answer == question["correct"]
    if is_correct:
        score += 10
        if score > game_state["high_score"]:
            game_state["high_score"] = score

    return {
        "is_correct": is_correct,
        "correct_answer": question["correct"],
        "score": score,
        "high_score": game_state["high_score"]
    }

@router.get("/highscore")
async def get_highscore():
    return {"high_score": game_state["high_score"]}
