Setup

Step by step guide setting up this project

1. mkdir rl_web_testing
2. cd rl_web_testing
3. git clone https://github.com/harikrishnaburma/rl_web_testing.git
4. Update pip
    1. python3 -m pip install --upgrade pip 
5. Create a virtual environment
    * python3 -m venv venv
6. Activate virtual environment
    * source venv/bin/activate
7. Install required libraries
    * pip3 install selenium stable-baselines3 scikit-learn beautifulsoup4 gym
    * pip3 install 'shimmy>=2.0'
8. Download chrome driver that suits your browser https://googlechromelabs.github.io/chrome-for-testing/ 
    1. Keep the chrome driver in project environment and make it executable
    2. chmod +x chromedriver
9. Make sure project structure looks like below

<img width="788" alt="Screenshot 2025-03-21 at 2 50 45 PM" src="https://github.com/user-attachments/assets/04009b3f-2ade-4ae5-bec0-47bb11d71f75" />
