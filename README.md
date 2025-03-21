
This main intention of the project is to build an idea of how agents can explore any given application and perform tests using reinforcement learning.

Step by step guide setting up this project
1. git clone https://github.com/harikrishnaburma/rl_web_testing.git
2. Update pip
    1. python3 -m pip install --upgrade pip 
3. Create a virtual environment
    * python3 -m venv venv
4. Activate virtual environment
    * source venv/bin/activate
5. Install required libraries
    * pip3 install selenium stable-baselines3 scikit-learn beautifulsoup4 gym
    * pip3 install 'shimmy>=2.0'
6. Download chrome driver that suits your browser https://googlechromelabs.github.io/chrome-for-testing/ 
    1. Keep the chrome driver in project environment and make it executable
    2. chmod +x chromedriver
7. Make sure project structure looks like below

<img width="788" alt="Screenshot 2025-03-21 at 2 50 45 PM" src="https://github.com/user-attachments/assets/04009b3f-2ade-4ae5-bec0-47bb11d71f75" />

8. Run main.py
   *  python3 main.py
