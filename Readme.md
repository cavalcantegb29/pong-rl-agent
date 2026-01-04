# 🏓 PPO Agent Playing Atari Pong

This project trains a reinforcement learning agent to play Atari Pong
using Proximal Policy Optimization (PPO) and the Arcade Learning Environment (ALE).

## 🎮 Demo
After 1M timesteps, the agent is able to sustain long rallies and
demonstrates non-random behavior.

## 🛠️ Tech Stack
- Python 3.11
- Gymnasium
- Arcade Learning Environment (ALE)
- Stable-Baselines3 (PPO)
- PyTorch

## 🚀 Training
```bash
python train_pong.py

Evaluation

python eval_pong.py

Results

~2900 steps per episode

Learned paddle control and ball tracking

## 📦 requirements.txt

gymnasium[atari]
ale-py
stable-baselines3
opencv-python
numpy









