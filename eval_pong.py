import ale_py
import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack

# =========================
# AMBIENTE (IGUAL AO TREINO)
# =========================
env = make_atari_env(
    "ALE/Pong-v5",
    n_envs=1,
    seed=0,
    env_kwargs={"render_mode": "human"}  # 👈 AQUI está a diferença
)

env = VecFrameStack(env, n_stack=4)

# =========================
# CARREGAR MODELO
# =========================
model = PPO.load("models/ppo_pong_1M", env=env)

# =========================
# LOOP DE JOGO
# =========================
obs = env.reset()

while True:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)

    if done:
        obs = env.reset()