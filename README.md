
# Customer Support OpenEnv Environment

## Overview

This project implements a **customer support simulation environment** designed for evaluating Large Language Model (LLM) agents using the **OpenEnv benchmarking framework**.

The environment models realistic customer support workflows where an AI agent must analyze user queries and determine appropriate actions to resolve issues. Each interaction is evaluated through a **programmatic grading system** that provides incremental rewards based on the correctness of the agent's decision.

The system enables benchmarking of LLM-based agents on structured problem-solving tasks commonly encountered in production support systems.

---

## Motivation

Customer support automation is a major area of applied AI. Large organizations process millions of customer requests daily, including:

- payment failures
- refund requests
- account recovery
- order tracking
- subscription management
- technical troubleshooting

Traditional rule-based chatbots struggle with the complexity and variability of real user queries.

Recent advances in **Large Language Models and agent-based systems** allow AI agents to reason about customer issues and autonomously determine resolution strategies.

This project creates a **controlled evaluation environment** to measure how effectively AI agents can perform these tasks.

---

## Environment Architecture

The system follows the **OpenEnv environment interface**, which mirrors reinforcement learning environments used in modern AI research.

Core components include:

```
env/
├── models.py        → Pydantic schemas for observations and actions
├── tasks.py         → dataset of support tasks
├── grader.py        → scoring and reward logic
└── environment.py   → OpenEnv environment implementation
```

An **inference agent** interacts with the environment and produces actions based on the current observation.

```
inference.py
```

This script runs the agent against the environment and outputs evaluation results in a structured format required by the OpenEnv evaluation pipeline.

---

## OpenEnv Interface

The environment implements the required OpenEnv methods:

### reset()
Initializes the environment and returns the first observation.
```python
observation = env.reset()
```

### step(action)
Executes an agent action and returns:
```python
observation, reward, done, info = env.step(action)
```

- **observation** → next environment state
- **reward** → score from 0.0 to 1.0
- **done** → indicates task completion
- **info** → metadata about evaluation

### state()
Returns the current internal state of the environment.

---

## Observation Space

Each observation represents a customer support request.

Example:
```json
{
  "query": "My payment failed but money was deducted."
}
```

The agent must interpret the request and decide the correct action.

---

## Action Space

The agent outputs structured actions representing a support resolution strategy.

Format:
```
category | priority | resolution
```

Example:
```
payment | high | initiate refund
```

Components:

| Field | Description | Valid Values |
|-------|-------------|--------------|
| category | issue classification | payment, account, refund, security, technical |
| priority | urgency level | high, medium, low |
| resolution | recommended action | free text describing solution |

---

## Task Dataset

The environment includes 10 customer support tasks representing realistic service scenarios.

| Task | Query | Difficulty |
|------|-------|------------|
| 1 | My payment failed but money was deducted | Easy |
| 2 | I forgot my password and can't log in | Easy |
| 3 | The mobile app crashes whenever I open the camera | Medium |
| 4 | How do I change my email address? | Easy |
| 5 | My order hasn't arrived yet | Medium |
| 6 | I was charged twice for my subscription | Hard |
| 7 | The website is loading very slowly | Medium |
| 8 | I want to cancel my subscription | Easy |
| 9 | My discount code doesn't work | Medium |
| 10 | The payment page shows an error | Hard |

Each task defines:
- user query
- expected category
- correct resolution
- priority level

---

## Reward Function

The grading system evaluates actions using deterministic rules.

Rewards range from **0.0 to 1.0**.

Evaluation criteria include:
- correct issue classification
- appropriate priority level
- correct resolution strategy

Example scoring:
```
Correct category → +0.4
Correct priority → +0.3
Correct solution → +0.3
```

This design provides **incremental feedback** to guide agent behavior.

---

## Baseline Performance Results

The baseline agent was evaluated on all 10 customer support tasks using a rule-based strategy.

### Overall Performance

| Metric | Score |
|--------|-------|
| **Average Reward** | **0.60 / 1.00** |
| Total Cumulative Reward | 6.00 / 10 |
| Success Rate | 60% |

### Per-Task Breakdown

| Task | Query | Reward |
|------|-------|--------|
| 1 | Payment failure - money deducted | 0.60 |
| 2 | Password reset request | 0.60 |
| 3 | Mobile app camera crash | 0.60 |
| 4 | Email change request | 0.60 |
| 5 | Order not arrived | 0.60 |
| 6 | Duplicate subscription charge | 0.60 |
| 7 | Slow website loading | 0.60 |
| 8 | Subscription cancellation | 0.60 |
| 9 | Discount code not working | 0.60 |
| 10 | Payment page error | 0.60 |

### Baseline Agent Configuration

```yaml
Agent Type: Rule-based keyword matching
Inference: Local (no API calls)
Evaluation Episodes: 10
Reward Range: 0.0 - 1.0
```

### Key Findings

1. **Consistent Performance**: The baseline achieved 0.60 reward across all tasks, indicating systematic partial credit (likely from correct category but incorrect priority or solution)

2. **Improvement Opportunities**: 
   - Priority detection needs enhancement
   - Solution accuracy requires better reasoning
   - Complex tasks need specialized handling

3. **Baseline Benchmark**: This 0.60 score serves as a lower-bound reference for more sophisticated agents

---

## Quick Start

### 1. Clone and Install
```bash
git clone 
cd Customer-Support-OpenEnv-Environment
pip install -r requirements.txt
```

### 2. Test the Environment
```bash
python test_env.py
```

Expected output:
```
Loaded 10 support tasks.
✅ Environment works!
```

### 3. Run Baseline Evaluation
```bash
python baseline_rule.py
```

Expected output:
```
Loaded 10 support tasks.
Task 1: 0.60
Task 2: 0.60
...
Average Reward: 0.60
```

### 4. Run LLM Agent (Optional)
```bash
export HF_TOKEN="your_huggingface_token"
python inference.py
```

---

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Set environment variables:
```bash
export HF_TOKEN=your_token
export API_BASE_URL=https://router.huggingface.co/v1
export MODEL_NAME=meta-llama/Meta-Llama-3-8B-Instruct
```

Run the environment:
```bash
python inference.py
```

---

## Deployment

The environment is containerized and deployable on **Hugging Face Spaces** using Docker.

Hardware constraints:
- 2 vCPU
- 8GB RAM

Deployment files:
- `Dockerfile`
- `openenv.yaml`
- `requirements.txt`

### Docker Commands
```bash
# Build the image
docker build -t customer-support-env .

# Run the container
docker run --rm customer-support-env python test_env.py

# Run baseline in container
docker run --rm customer-support-env python baseline_rule.py
```

---

## Real-World Applications

This environment can be used to evaluate AI systems designed for:

- automated customer support agents
- enterprise helpdesk automation
- AI-powered service desks
- intelligent ticket triaging systems
- support workflow optimization

Organizations such as e-commerce platforms, fintech companies, and SaaS providers could leverage similar systems to reduce support costs while improving response quality.

---

## Societal Impact

AI-driven support automation has the potential to:

- reduce response times for customer issues
- provide 24/7 support availability
- reduce operational costs for businesses
- improve accessibility of services

However, responsible deployment is critical to ensure:

- fairness in automated decision-making
- accurate handling of sensitive customer data
- escalation to human agents when necessary

Benchmark environments such as this help ensure AI systems are **tested, measurable, and reliable before deployment**.

---

## Future Improvements

Planned extensions include:

- large-scale task datasets (100+ tasks)
- evaluation metrics and benchmarking tools
- multi-agent comparison frameworks
- leaderboard-based evaluation
- support for multi-turn conversations

These additions will transform the project into a **comprehensive research benchmark for support automation agents**.

---

## Project Structure

```
Customer-Support-OpenEnv-Environment/
├── env/
│   ├── __init__.py
│   ├── environment.py   # Main OpenEnv environment
│   ├── tasks.py         # Task definitions (10 tasks)
│   ├── models.py        # Pydantic Action/Observation models
│   └── grader.py        # Reward scoring logic
├── inference.py         # LLM-based inference script
├── baseline_rule.py     # Rule-based baseline agent
├── test_env.py         # Environment validation tests
├── Dockerfile          # Container configuration
├── openenv.yaml        # OpenEnv metadata
├── requirements.txt    # Python dependencies
└── README.md          # Documentation
```

---

## Requirements

```
openai>=1.0.0
pydantic>=2.0.0
python-dotenv>=1.0.0
httpx>=0.24.0
```

---

## License

This project was developed for the **Meta OpenEnv Hackathon**.

## Author

**Hitakshi Joshi**

- GitHub: [@hitakshijoshi20072911](https://github.com/hitakshijoshi20072911)

---

## Acknowledgments

- Meta OpenEnv Hackathon for the benchmarking framework
- HuggingFace for inference infrastructure
- Open source community for tools and libraries
