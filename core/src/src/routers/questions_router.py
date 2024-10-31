from fastapi import Depends, APIRouter

from dependencies import get_db
from src.models.schemas import QuizQuestion
from sqlalchemy.orm import Session

router = APIRouter(prefix="/questions", tags=["questions"],)


@router.get("/", response_model=QuizQuestion)
def get_question_for_user(db: Session = Depends(get_db)):
    return QuizQuestion(question="Какая сложность у сортировки пузырьком?", answer="O(n^2)")