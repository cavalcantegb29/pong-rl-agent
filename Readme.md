# 🏓 PPO Agent Playing Atari Pong

This project trains a reinforcement learning agent to play **Atari Pong**
using **Proximal Policy Optimization (PPO)** and the
**Arcade Learning Environment (ALE)**.

The agent learns directly from pixels and is able to sustain long rallies
and demonstrate non-random behavior after extended training.

---

## 🎮 Demo

After **1 million timesteps**, the agent:
- Tracks the ball consistently
- Maintains long rallies
- Demonstrates learned paddle control

![Pong PPO Agent](docs/pong_demo.gif)

---

## 🧠 Method

- Algorithm: **PPO (Proximal Policy Optimization)**
- Observation space: stacked grayscale frames (84×84)
- Action space: discrete Atari actions
- Training environment: `ALE/Pong-v5`

---

## 🛠️ Tech Stack

- Python 3.11
- Gymnasium
- Arcade Learning Environment (ALE)
- Stable-Baselines3
- PyTorch
- NumPy
- OpenCV

---

## 🚀 Training

```bash
python train_pong.py

📂 Project Structure
pong-rl-agent/
├── train_pong.py
├── eval_pong.py
├── models/
│   └── ppo_pong_1M.zip
├── docs/
│   └── pong_demo.gif
└── README.md



