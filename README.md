# 🏀 NBA Predictions Project

## Overview
Welcome to the NBA Predictions Project! This project aims to predict various NBA awards and the finals winner for each season using statistical analysis and machine learning techniques. The project involves data collection, preprocessing, model training, and evaluation to make accurate predictions.

## Project Structure
```plaintext
nba-predictions/
├── data/                   # 📁 Folder to store raw and processed data
├── notebooks/              # 📓 Jupyter notebooks for data exploration and analysis
├── src/                    # 📂 Source code for data collection, preprocessing, and modeling
│   ├── __init__.py
│   ├── data_collection.py  # 📝 Scripts for collecting data from various sources
│   ├── data_preprocessing.py # 🧹 Scripts for cleaning and preprocessing data
│   ├── model_training.py   # 🤖 Scripts for training machine learning models
│   ├── model_evaluation.py # 📊 Scripts for evaluating model performance
├── venv/                   # 🛠 Virtual environment for the project
├── .gitignore              # 🚫 Git ignore file
├── requirements.txt        # 📜 List of required Python packages
├── README.md               # 📖 Project description and setup instructions
```

# Setup Instructions

## Prerequisites

- 🐍 Python 3.x
- 🌐 Git

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/nba-predictions.git
cd nba-predictions
```
### Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Install Required Packages

```bash
pip install -r requirements.txt
```
## Open the Project in VS Code

1. Open Visual Studio Code.
2. Go to `File > Open Folder...` and select the cloned repository folder.

## Configure Python Interpreter in VS Code

1. Press `Ctrl+Shift+P` and select `Python: Select Interpreter`.
2. Choose the interpreter from your virtual environment (`venv`).

## Data Collection

To collect player statistics using the `nba_api`, run the script in `src/data_collection.py`:

```python
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players

def get_player_info(player_name):
    player = players.find_players_by_full_name(player_name)[0]
    player_id = player['id']
    
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_stats = player_info.get_data_frames()[0]
    
    return player_stats

if __name__ == "__main__":
    player_name = "LeBron James"
    stats = get_player_info(player_name)
    print(stats)
```
