from pydantic import BaseModel, Field, model_validator


class QuizQuestion(BaseModel):

    question: str = Field(
        description="The multiple-choice question"
    )

    options: list[str] = Field(
        description="Exactly four answer options",
        min_length=4,
        max_length=4
    )

    correct_answer: str = Field(
        description="The correct answer"
    )

    explanation: str = Field(
        description="Explanation of the correct answer"
    )

    @model_validator(mode="after")
    def validate_answer(self):

        if len(set(self.options)) != 4:
            raise ValueError("Options must be unique")

        if self.correct_answer not in self.options:
            raise ValueError("Correct answer must be one of the options")

        return self


class Quiz(BaseModel):

    topic: str

    questions: list[QuizQuestion] = Field(min_length=1)