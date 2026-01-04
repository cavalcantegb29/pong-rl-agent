import ale_py
import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack

# Ambiente Atari
env = make_atari_env(
    "ALE/Pong-v5",
    n_envs=1,
    seed=0
)

env = VecFrameStack(env, n_stack=4)

# 🔥 Carrega o modelo já treinado (200k)
model = PPO.load("models/ppo_pong", env=env)

# Continua o treino até 1 milhão de steps
model.learn(total_timesteps=1_000_000)

# Salva novo checkpoint
model.save("models/ppo_pong_1M")

env.close()