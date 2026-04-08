from env.environment import SupportEnv
from env.models import Action

print('Testing Customer Support Environment...')
print('='*50)

# Create environment
env = SupportEnv()

# Reset and get first task (returns a string - the customer query)
obs = env.reset()
print(f'Task Query: {obs}')
print()

# Create a test action
action = Action(
    category='payment',
    priority='high',
    solution='initiate refund'
)

# Take a step
new_obs, reward, done, info = env.step(action)
print(f'Reward: {reward}')
print(f'Done: {done}')
print(f'Info: {info}')

print('\n✅ Environment works!')