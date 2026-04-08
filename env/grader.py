"""
grader.py

Contains the deterministic grading function.

The grader compares the agent's action with the ground truth task.
"""

from env.tasks import SupportTask
from env.models import Action


def grade_action(action: Action, task: SupportTask) -> float:
    """
    Grades an agent action against the correct task solution.

    Reward design:
    category correctness = 0.4
    priority correctness = 0.2
    solution correctness = 0.4
    """

    score = 0.0

    if action.category.lower() == task.category.lower():
        score += 0.4

    if action.priority.lower() == task.priority.lower():
        score += 0.2

    if action.solution.lower() == task.solution.lower():
        score += 0.4

    return score