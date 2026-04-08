"""Rule-Based Baseline Agent - No API Required"""
from env.environment import SupportEnv
from env.models import Action

def rule_based_agent(query):
    """Simple keyword-based agent that actually reads the query"""
    query_lower = query.lower()
    
    # Category detection based on keywords
    if any(word in query_lower for word in ['payment', 'deducted', 'charge', 'card', 'failed', 'transaction']):
        category = 'payment'
    elif any(word in query_lower for word in ['password', 'login', 'access', 'account', 'sign', 'email']):
        category = 'account'
    elif any(word in query_lower for word in ['refund', 'return', 'money back', 'reimburs']):
        category = 'refund'
    elif any(word in query_lower for word in ['hack', 'stolen', 'security', 'breach', 'unauthorized']):
        category = 'security'
    elif any(word in query_lower for word in ['crash', 'slow', 'loading', 'error', 'camera']):
        category = 'technical'
    elif any(word in query_lower for word in ['cancel', 'subscription']):
        category = 'account'
    elif any(word in query_lower for word in ['discount', 'code']):
        category = 'payment'
    else:
        category = 'unknown'
    
    # Priority detection
    if any(word in query_lower for word in ['urgent', 'emergency', 'hacked', 'stolen', 'critical', 'immediate', 'twice', 'duplicate']):
        priority = 'high'
    elif any(word in query_lower for word in ['later', 'whenever', 'not urgent', 'low priority']):
        priority = 'low'
    else:
        priority = 'medium'
    
    # Solution detection based on query content
    if 'refund' in query_lower or 'return' in query_lower or 'twice' in query_lower or 'duplicate' in query_lower:
        solution = 'initiate refund process'
    elif 'password' in query_lower or 'login' in query_lower:
        solution = 'send password reset link'
    elif 'email' in query_lower:
        solution = 'guide through email change process'
    elif 'cancel' in query_lower or 'subscription' in query_lower:
        solution = 'process subscription cancellation'
    elif 'crash' in query_lower or 'slow' in query_lower or 'camera' in query_lower:
        solution = 'clear cache and reinstall app'
    elif 'discount' in query_lower or 'code' in query_lower:
        solution = 'verify and apply discount code'
    elif 'hack' in query_lower or 'stolen' in query_lower or 'security' in query_lower:
        solution = 'lock account and escalate to security team'
    elif 'payment' in query_lower or 'deducted' in query_lower or 'failed' in query_lower or 'error' in query_lower:
        solution = 'verify transaction status and investigate payment'
    else:
        solution = 'gather more information and escalate to human agent'
    
    return Action(category=category, priority=priority, solution=solution)

def run_baseline():
    """Run rule-based baseline on all tasks"""
    env = SupportEnv()
    total_reward = 0
    results = []
    
    print("="*60)
    print("RULE-BASED BASELINE AGENT")
    print("="*60)
    print(f"Running on {len(env.tasks)} tasks...\n")
    
    for i in range(len(env.tasks)):
        obs = env.reset()
        action = rule_based_agent(obs)
        _, reward, _, info = env.step(action)
        total_reward += reward
        
        # Store results
        results.append({
            'task_num': i+1,
            'query': obs[:60],
            'predicted': action.category,
            'expected': info.get('expected_category', 'unknown'),
            'reward': reward
        })
        
        print(f"Task {i+1}: {obs[:50]}...")
        print(f"  → Predicted: {action.category} (Expected: {info.get('expected_category', 'unknown')})")
        print(f"  → Reward: {reward:.2f}")
        print()
    
    # Calculate statistics
    print("="*60)
    print("BASELINE RESULTS")
    print("="*60)
    
    avg_reward = total_reward / len(env.tasks)
    correct_predictions = sum(1 for r in results if r['predicted'] == r['expected'])
    accuracy = (correct_predictions / len(env.tasks)) * 100
    
    print(f"Total Reward: {total_reward:.2f} / {len(env.tasks)}")
    print(f"Average Reward: {avg_reward:.2f}")
    print(f"Category Accuracy: {correct_predictions}/{len(env.tasks)} ({accuracy:.1f}%)")
    print("="*60)
    
    return avg_reward

if __name__ == "__main__":
    run_baseline()
def main():
    """Main function for OpenEnv entry point"""
    env = SupportEnv()
    print("Running rule-based baseline...")
    obs = env.reset()
    total_reward = 0
    
    for i in range(env.total_tasks):
        # Simple rule-based action
        query_lower = obs.lower()
        if any(w in query_lower for w in ['payment', 'deducted', 'charge']):
            action = Action(category='payment', priority='high', solution='initiate refund')
        elif any(w in query_lower for w in ['password', 'login']):
            action = Action(category='account', priority='medium', solution='password reset')
        else:
            action = Action(category='general', priority='medium', solution='general support')
        
        obs, reward, done, info = env.step(action)
        total_reward += reward
        print(f"Task {i+1}: Reward {reward}")
    
    print(f"\nTotal Reward: {total_reward}/{env.total_tasks} = {total_reward/env.total_tasks:.2%}")

if __name__ == "__main__":
    main()
