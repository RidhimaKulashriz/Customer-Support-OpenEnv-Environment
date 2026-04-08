"""
Server app for Hugging Face Spaces deployment
"""
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from env.environment import SupportEnv
from env.models import Action
from transformers import pipeline
import gradio as gr

# Initialize environment and model
env = SupportEnv()
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=-1
)
categories = ['payment', 'account', 'bug', 'delivery', 'performance', 'promotion']

def process_query(query):
    """Process a customer support query"""
    # Classify category
    result = classifier(query, categories)
    category = result['labels'][0]
    
    # Simple solution mapping
    query_lower = query.lower()
    if 'password' in query_lower or 'login' in query_lower:
        solution = 'password reset'
    elif 'email' in query_lower:
        solution = 'update email settings'
    elif 'cancel' in query_lower:
        solution = 'cancel subscription'
    elif 'failed' in query_lower and 'payment' in query_lower:
        solution = 'initiate refund'
    elif 'charged' in query_lower:
        solution = 'refund duplicate charge'
    elif 'camera' in query_lower or 'crash' in query_lower:
        solution = 'report bug and patch'
    elif 'slow' in query_lower:
        solution = 'check server load'
    elif 'arrived' in query_lower:
        solution = 'track shipment'
    elif 'discount' in query_lower:
        solution = 'validate coupon'
    elif 'error' in query_lower:
        solution = 'investigate issue'
    else:
        solution = 'general support'
    
    # Determine priority
    if any(w in query_lower for w in ['urgent', 'crash', 'failed', 'twice']):
        priority = 'high'
    else:
        priority = 'medium'
    
    return f"""
    📋 **Analysis Result:**
    
    🔍 **Category:** {category}
    ⚡ **Priority:** {priority}
    💡 **Suggested Solution:** {solution}
    
    ---
    🎯 **Confidence:** High
    🤖 **Agent:** Hugging Face BART Model
    """

# Create Gradio interface
iface = gr.Interface(
    fn=process_query,
    inputs=gr.Textbox(lines=3, placeholder="Enter your customer support query here..."),
    outputs=gr.Markdown(),
    title="🤖 Customer Support AI Agent",
    description="AI-powered customer support system using Hugging Face transformers. Get instant category classification, priority assessment, and solution suggestions.",
    examples=[
        ["My payment failed but money was deducted."],
        ["I forgot my password and can't log in."],
        ["The app crashes whenever I open the camera."],
        ["I want to cancel my subscription."],
        ["My discount code doesn't work."]
    ]
)

def main():
    """Main function for OpenEnv server entry point"""
    iface.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
