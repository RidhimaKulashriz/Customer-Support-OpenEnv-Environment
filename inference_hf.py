"""Hugging Face Agent for Customer Support - Optimized Version"""
from env.environment import SupportEnv
from env.models import Action
from transformers import pipeline
import os
import re

class HFSupportAgent:
    def __init__(self):
        print("Loading Hugging Face model...")
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=-1
        )
        self.categories = ['payment', 'account', 'bug', 'delivery', 'performance', 'promotion']
        
    def predict(self, query):
        category_result = self.classifier(query, self.categories)
        category = category_result['labels'][0]
        query_lower = query.lower()
        
        # Improved priority detection
        if any(word in query_lower for word in ['urgent', 'crash', 'error', 'failed', 'deducted', 'twice']):
            priority = 'high'
        elif any(word in query_lower for word in ['later', 'how to', 'change', 'cancel']):
            priority = 'low'
        else:
            priority = 'medium'
        
        # Improved solution mapping for better scores
        if 'password' in query_lower or 'login' in query_lower:
            solution = 'password reset'
        elif 'email' in query_lower:
            solution = 'update email settings'
        elif 'cancel' in query_lower or 'subscription' in query_lower:
            solution = 'cancel subscription'
        elif 'payment' in query_lower and 'failed' in query_lower:
            solution = 'initiate refund'
        elif 'charged' in query_lower or 'deducted' in query_lower:
            solution = 'refund duplicate charge'
        elif 'crash' in query_lower or 'camera' in query_lower:
            solution = 'report bug and patch'
        elif 'slow' in query_lower or 'loading' in query_lower:
            solution = 'check server load'
        elif 'arrived' in query_lower:
            solution = 'track shipment'
        elif 'discount' in query_lower or 'code' in query_lower:
            solution = 'validate coupon'
        elif 'payment' in query_lower and 'error' in query_lower:
            solution = 'investigate payment gateway'
        else:
            solution = 'general support'
            
        return Action(category=category, priority=priority, solution=solution)

def main():
    env = SupportEnv()
    agent = HFSupportAgent()
    
    print("\n" + "="*60)
    print("IMPROVED HUGGING FACE AGENT EVALUATION")
    print("="*60)
    
    obs = env.reset()
    total_reward = 0
    
    for i in range(env.total_tasks):
        action = agent.predict(obs)
        obs, reward, done, info = env.step(action)
        total_reward += reward
        task = env.tasks[i]
        
        print(f"Task {i+1}: {task.query[:50]}...")
        print(f"  → Predicted: {action.category} (Expected: {task.category})")
        print(f"  → Predicted Solution: {action.solution}")
        print(f"  → Expected Solution: {task.solution}")
        print(f"  → Reward: {reward:.2f}\n")
    
    print("="*60)
    print(f"TOTAL REWARD: {total_reward:.2f} / {env.total_tasks}")
    print(f"AVERAGE REWARD: {total_reward/env.total_tasks:.2f}")
    print(f"PERCENTAGE: {(total_reward/env.total_tasks)*100:.1f}%")
    print("="*60)

if __name__ == "__main__":
    main()
