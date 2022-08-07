# BGG Telegram Bot

A simple Telegram bot for getting information about board games using Board Game Geek API.

## Create Telegram Bot

BGG Bot was created by using [BotFather](https://telegram.me/BotFather) - a bot used to create other bots.

## Requirements

### Operating system
Program was created on Windows 10 Home.

### Environment
The whole environment was set up with [conda](https://docs.conda.io/en/latest/) which can be downloaded and installed from [this link](https://docs.conda.io/en/latest/miniconda.html).

### Python

This bot was built with `Python 3.10` and `python-telegram-bot`. 

To run this project, you have to install python and other necessary libraries.

You can do it by following these steps:

1. Clone this repo and go to the main folder (`bgg-telegram-bot`) in your terminal.
2. Run below command: it will create a conda environment with all dependencies. Installation can take a few minutes.
    ````commandline
    conda create --name <env> --file requirements
    ````
3. Change conda environment with below command:
    ```commandline
    conda activate <env>
    ```
4. Install `python-telegram-bot` version 20:
    ```commandline
    pip install python-telegram-bot -U --pre
    ```