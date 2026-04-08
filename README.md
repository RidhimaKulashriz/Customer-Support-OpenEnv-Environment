
# Customer Support OpenEnv Environment

[![OpenEnv](https://img.shields.io/badge/OpenEnv-Compatible-green)](https://github.com/facebookresearch/openenv)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow)](https://huggingface.co)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)

## Overview

An AI-powered customer support environment built for the Meta OpenEnv Hackathon. This environment simulates real-world customer service scenarios where AI agents must classify queries, determine priority, and suggest appropriate solutions.

**Baseline Score: 86% (8.6/10)**

## Features

- 10 Real-World Tasks - Payment issues, account management, technical bugs, delivery tracking, and more
- OpenEnv Compliant - Fully implements the OpenEnv interface specification
- Hugging Face Integration - Uses BART model for zero-shot classification
- Web Interface - Gradio-powered UI for easy testing
- Deterministic Grading - Clear reward system (0.0-1.0 scale)
- Docker Ready - Deployable to Hugging Face Spaces

## Performance

| Metric | Score |
|--------|-------|
| Total Reward | 8.6 / 10 |
| Average Reward | 0.86 |
| Accuracy | 86% |
| Perfect Tasks | 8 / 10 |

### Task Breakdown

| Task | Query Type | Score |
|------|-----------|-------|
| 1 | Payment failed | 1.00 |
| 2 | Forgot password | 1.00 |
| 3 | App crashes | 1.00 |
| 4 | Change email | 1.00 |
| 5 | Order not arrived | 1.00 |
| 6 | Charged twice | 0.60 |
| 7 | Slow loading | 1.00 |
| 8 | Cancel subscription | 1.00 |
| 9 | Discount code | 0.40 |
| 10 | Payment page error | 0.60 |

## Tasks Description

The environment includes 10 customer support tasks with increasing difficulty:

- **Easy**: Payment failure, password reset, email change
- **Medium**: Delivery tracking, slow loading, subscription cancellation
- **Hard**: Double charges, discount code issues, payment page errors

## Installation

### Prerequisites
- Python 3.11+
- Hugging Face account and API token

### Setup

1. Clone the repository:
```bash
git clone https://github.com/RidhimaKulashriz/Customer-Support-OpenEnv-Environment.git
cd Customer-Support-OpenEnv-Environment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your Hugging Face token:
```bash
# Windows PowerShell
$env:HF_TOKEN="your_token_here"

# Linux/Mac
export HF_TOKEN="your_token_here"
```

## Usage

### Run the Hugging Face Agent
```bash
python inference_hf.py
```

### Run the Baseline Agent
```bash
python inference.py
```

### Launch Web Interface
```bash
python server/app.py
```
Then open http://localhost:7860 in your browser

### Test Environment
```bash
python test_env.py
```

### Validate OpenEnv Compliance
```bash
openenv validate
```

## Project Structure

```
Customer-Support-OpenEnv-Environment/
├── env/
│   ├── __init__.py
│   ├── environment.py    # Main environment class
│   ├── models.py         # Pydantic models
│   ├── tasks.py          # 10 support tasks
│   └── grader.py         # Reward function
├── server/
│   └── app.py            # Gradio web interface
├── inference.py          # Rule-based baseline
├── inference_hf.py       # Hugging Face agent
├── test_env.py           # Environment tests
├── quick_test.py         # Quick validation
├── pyproject.toml        # OpenEnv configuration
├── requirements.txt      # Dependencies
├── Dockerfile            # Container configuration
└── README.md
```

## Grading System

The reward function evaluates three aspects:
- Category correctness: 0.4 points
- Priority correctness: 0.2 points
- Solution correctness: 0.4 points

Maximum reward per task: 1.0

## Model Details

- **Model**: facebook/bart-large-mnli
- **Type**: Zero-shot classification
- **Categories**: payment, account, bug, delivery, performance, promotion
- **Inference**: CPU (can be switched to GPU)

## Deployment

### Deploy to Hugging Face Spaces

1. Create a new Space at https://huggingface.co/new-space
2. Select Docker as SDK
3. Connect your GitHub repository
4. Add HF_TOKEN as a secret
5. Click Create Space

### Docker Build
```bash
docker build -t customer-support-env .
docker run -p 7860:7860 -e HF_TOKEN="your_token" customer-support-env
```

## Results

The Hugging Face agent achieves:
- 86% average reward across all tasks
- Perfect classification on 8 out of 10 tasks
- Accurate priority detection
- Appropriate solution suggestions

## Contributing

This project was created for the Meta OpenEnv Hackathon.

## License

MIT

## Links

- GitHub Repository: https://github.com/RidhimaKulashriz/Customer-Support-OpenEnv-Environment
- Hugging Face Space: https://huggingface.co/spaces/RidhimaKulashriz/customer-support-openenv
- OpenEnv Documentation: https://github.com/facebookresearch/openenv
