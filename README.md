
# Customer Support OpenEnv Environment

## Overview
An AI-powered customer support environment built for the Meta OpenEnv Hackathon. This environment simulates real-world customer service scenarios where AI agents classify queries, determine priority, and suggest appropriate solutions.

**Baseline Score: 86% (8.6/10)**

## Links
- **Live Demo**: https://huggingface.co/spaces/RidhimaKulashriz/openenv-customer-support-ai
- **GitHub Repository**: https://github.com/RidhimaKulashriz/Customer-Support-OpenEnv-Environment
- **OpenEnv Validation**: PASSED

## Features
- 10 Real-World Customer Support Tasks
- OpenEnv Compliant Interface
- Hugging Face BART Model for Zero-Shot Classification
- Gradio Web Interface for Easy Testing
- Deterministic Grading System (0.0-1.0 scale)
- Docker Container Ready

## Performance Results

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

## Task Categories
- payment - Payment and billing issues
- account - Account management and access
- bug - Technical problems and crashes
- delivery - Order and shipping status
- performance - Speed and loading issues
- promotion - Discount codes and offers

## Installation

### Prerequisites
- Python 3.11+
- Hugging Face account with API token

### Setup
```bash
git clone https://github.com/RidhimaKulashriz/Customer-Support-OpenEnv-Environment.git
cd Customer-Support-OpenEnv-Environment
pip install -r requirements.txt
```

### Set Environment Variable
```bash
# Windows PowerShell
$env:HF_TOKEN="your_token_here"

# Linux/Mac
export HF_TOKEN="your_token_here"
```

## Usage

### Run Hugging Face Agent
```bash
python inference_hf.py
```

### Run Baseline Agent
```bash
python inference.py
```

### Launch Web Interface
```bash
python server/app.py
```
Then open http://localhost:7860

### Validate OpenEnv Compliance
```bash
openenv validate
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
- **Inference**: CPU (configurable to GPU)

## Project Structure
```
Customer-Support-OpenEnv-Environment/
├── env/
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

## Deployment

### Deployed on Hugging Face Spaces
The environment is live at: https://huggingface.co/spaces/RidhimaKulashriz/openenv-customer-support-ai

### Local Docker Build
```bash
docker build -t customer-support-env .
docker run -p 7860:7860 -e HF_TOKEN="your_token" customer-support-env
```

## Results Summary

The Hugging Face agent achieves:
- 86% average reward across all tasks
- Perfect classification on 8 out of 10 tasks
- Accurate priority detection
- Appropriate solution suggestions

## OpenEnv Compliance
- [x] Real-world task simulation
- [x] OpenEnv specification compliance
- [x] Minimum 3 tasks with graders
- [x] Meaningful reward function
- [x] Baseline inference script
- [x] Containerized execution
- [x] Complete documentation

## License
MIT

## Author
Ridhima Kulashri

## Acknowledgments
- Meta OpenEnv Hackathon
- Hugging Face for transformers library
- Facebook AI for BART model
