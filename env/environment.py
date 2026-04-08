"""
Customer Support RL Environment

This environment simulates customer support tasks.
Agents interact with the environment by taking actions
and receiving rewards based on grading.

Structure inspired by OpenAI Gym.
"""

from env.tasks import load_tasks
from env.grader import grade_action
from env.models import Action


class SupportEnv:
    """
    Customer Support Environment
    """
    

    def __init__(self):
        # Load dataset of tasks
        self.tasks = load_tasks()

        # Track current task index
        self.current_index = 0

        # Total number of tasks
        self.total_tasks = len(self.tasks)
        
        print(f"Loaded {len(self.tasks)} support tasks.")

    

    def reset(self):
        """
        Reset environment to first task.
        Returns the first observation.
        """

        self.current_index = 0

        task = self.tasks[self.current_index]

        return task.query

    def get_state(self):
        """
        Return the current customer query.
        """

        task = self.tasks[self.current_index]

        return task.query

    def step(self, action: Action):
        """
        Apply an action and receive reward.

        Returns:
            observation
            reward
            done
            info
        """

        task = self.tasks[self.current_index]

        # Evaluate action
        score = grade_action(action, task)

        reward = score

        # Move to next task
        self.current_index += 1

        done = self.current_index >= self.total_tasks

        if not done:
            observation = self.tasks[self.current_index].query
        else:
            observation = None

        info = {
            "task_id": task.id,
            "expected_category": task.category
        }

        return observation, reward, done, info