import os
from openai import OpenAI

from env.environment import SupportEnv
from env.models import Action


# Read environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")


# Initialize OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def generate_action(query: str):

    prompt = f"""
You are a customer support AI.

Classify the query and propose a solution.

Return exactly:

category: <category>
priority: <priority>
solution: <solution>

Query:
{query}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    lines = text.split("\n")

    category = lines[0].split(":")[1].strip()
    priority = lines[1].split(":")[1].strip()
    solution = lines[2].split(":")[1].strip()

    return Action(
        category=category,
        priority=priority,
        solution=solution
    )


def main():

    env = SupportEnv()

    task_name = "support_task"
    benchmark = "customer-support-env"

    state = env.reset()

    rewards = []
    step = 0
    done = False

    print(f"[START] task={task_name} env={benchmark} model={MODEL_NAME}")

    try:

        while not done:

            step += 1

            action = generate_action(state)

            action_str = f"{action.category}|{action.priority}|{action.solution}"

            next_state, reward, done, info = env.step(action)

            rewards.append(f"{reward:.2f}")

            print(
                f"[STEP] step={step} action={action_str} reward={reward:.2f} done={str(done).lower()} error=null"
            )

            state = next_state

    except Exception as e:

        print(
            f"[STEP] step={step} action=null reward=0.00 done=true error={str(e)}"
        )

    success = done

    rewards_str = ",".join(rewards)

    print(
        f"[END] success={str(success).lower()} steps={step} rewards={rewards_str}"
    )


if __name__ == "__main__":
    main()