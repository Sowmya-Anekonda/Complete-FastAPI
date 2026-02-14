from fastapi import FastAPI
from pydantic import BaseModel
from Testing_and_Debugging.integration_testing.app.logic import is_eligible_for_loan


app = FastAPI()


class Applicant(BaseModel):
    income: float
    age: int 
    employment_status: str 


@app.post('/loan-eligibility')
def check_eligibility(applicant: Applicant):
    eligibility = is_eligible_for_loan(
        applicant.income, 
        applicant.age,
        applicant.employment_status
        )
    
    return {'eligible': eligibility}