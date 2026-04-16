from fastapi import FastAPI, APIRouter, HTTPException, Query, status

from models import Invoice
from db import SessionDep
from sqlmodel import select
from models import Customer, Transaction, TransactionCreate

router = APIRouter()


@router.post("/invoices", response_model=Customer, tags=["invoices"])
def create_invoice(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_validate())
    session.add()
    session.commit()
    session.reresh(plan_db)
    return invoice_data


"""
@router.post("/plans", tags=["plans"])
def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add()
    session.commit()
    session.reresh(plan_db)
    return
"""