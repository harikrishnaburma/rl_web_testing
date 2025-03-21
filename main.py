from stable_baselines3 import PPO
from amazon_env import AmazonTestingEnv

# Initialize environment
env = AmazonTestingEnv()

# Train the RL agent
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Save the trained model
model.save("amazon_tester")

# Test the trained agent
obs = env.reset()
for _ in range(20):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    print(f"Action: {action}, Reward: {rewards}")
    if done:
        break

env.close()