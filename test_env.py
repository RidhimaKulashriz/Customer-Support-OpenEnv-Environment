from env.environment import SupportEnv
from env.models import Action

# Initialize environment
env = SupportEnv()

# Reset environment
state = env.reset()

print("Initial Query:")
print(state)

# Fake agent action
action = Action(
    category="payment",
    priority="high",
    solution="initiate refund"
)

# Step environment
next_state, reward, done, info = env.step(action)

print("\nReward:", reward)
print("Done:", done)
print("Info:", info)