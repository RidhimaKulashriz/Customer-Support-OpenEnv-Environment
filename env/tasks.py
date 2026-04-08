"""
tasks.py

Contains predefined customer support tasks used by the environment.

Each task contains:
- observation data
- correct category
- correct priority
- correct solution
"""

from typing import List
from env.models import SupportTask


def load_tasks() -> List[SupportTask]:
    """
    Returns a list of predefined tasks with increasing difficulty.
    """

    tasks = [

        SupportTask(
            id=1,
            query="My payment failed but money was deducted.",
            history="User attempted checkout twice.",
            product="E-commerce App",
            category="payment",
            priority="high",
            solution="initiate refund"
        ),

        SupportTask(
            id=2,
            query="I forgot my password and can't log in.",
            history="User attempted login 5 times.",
            product="Web Platform",
            category="account",
            priority="medium",
            solution="password reset"
        ),

        SupportTask(
            id=3,
            query="The mobile app crashes whenever I open the camera.",
            history="Issue started after latest update.",
            product="Mobile App",
            category="bug",
            priority="high",
            solution="report bug and patch"
        ),

        SupportTask(
            id=4,
            query="How do I change my email address?",
            history="User profile active.",
            product="Web Platform",
            category="account",
            priority="low",
            solution="update email settings"
        ),

        SupportTask(
            id=5,
            query="My order hasn't arrived yet.",
            history="Order shipped 5 days ago.",
            product="E-commerce App",
            category="delivery",
            priority="medium",
            solution="track shipment"
        ),

        SupportTask(
            id=6,
            query="I was charged twice for my subscription.",
            history="Billing cycle yesterday.",
            product="Subscription Service",
            category="payment",
            priority="high",
            solution="refund duplicate charge"
        ),

        SupportTask(
            id=7,
            query="The website is loading very slowly.",
            history="Multiple users reporting issue.",
            product="Web Platform",
            category="performance",
            priority="medium",
            solution="check server load"
        ),

        SupportTask(
            id=8,
            query="I want to cancel my subscription.",
            history="User subscribed 2 months ago.",
            product="Subscription Service",
            category="account",
            priority="low",
            solution="cancel subscription"
        ),

        SupportTask(
            id=9,
            query="My discount code doesn't work.",
            history="Code entered during checkout.",
            product="E-commerce App",
            category="promotion",
            priority="low",
            solution="validate coupon"
        ),

        SupportTask(
            id=10,
            query="The payment page shows an error.",
            history="Error code 502.",
            product="Web Platform",
            category="bug",
            priority="high",
            solution="investigate payment gateway"
        ),

    ]

    return tasks