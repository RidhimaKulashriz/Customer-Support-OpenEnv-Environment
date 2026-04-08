"""
run_baseline.py

Runs a baseline AI agent against the SupportEnv environment
and evaluates its performance.
"""

from env.environment import SupportEnv
from env.models import Action
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_action(query: str) -> Action:
    """
    Sends the customer query to the LLM and converts response to Action.
    """

    prompt = f"""
You are a customer support AI.

Given the following customer query, determine:

1. category
2. priority
3. solution

Return your answer EXACTLY in this format:

category: <category>
priority: <priority>
solution: <solution>

Customer query:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    text = response.choices[0].message.content

    # Parse the response
    lines = text.strip().split("\n")

    category = lines[0].split(":")[1].strip()
    priority = lines[1].split(":")[1].strip()
    solution = lines[2].split(":")[1].strip()

    return Action(
        category=category,
        priority=priority,
        solution=solution
    )


def run_agent():
    """
    Runs the agent through all tasks in the environment.
    """

    env = SupportEnv()

    state = env.reset()

    total_reward = 0
    steps = 0

    done = False

    while not done:

        action = generate_action(state)

        state, reward, done, info = env.step(action)

        total_reward += reward
        steps += 1

        print("\nTask:", steps)
        print("Reward:", reward)

    avg_score = total_reward / steps

    print("\n==============================")
    print("Agent Evaluation Complete")
    print("==============================")
    print("Tasks evaluated:", steps)
    print("Average reward:", round(avg_score, 3))


if __name__ == "__main__":
    run_agent()