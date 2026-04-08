"""
models.py

Defines the structured Observation and Action models used by the RL environment.
"""

from pydantic import BaseModel
from typing import Literal


class SupportTask(BaseModel):
    """
    Represents a single customer support task.
    """

    id: int
    query: str
    history: str
    product: str
    category: str
    priority: str
    solution: str


class Action(BaseModel):
    """
    Action taken by the AI support agent.
    """
    category: str  # Can be: payment, account, bug, delivery, performance, promotion
    priority: str  # high, medium, low
    solution: str
