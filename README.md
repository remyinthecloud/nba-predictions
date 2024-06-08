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
## Usage

### 📊 Data Collection
- Use the `data_collection.py` script to fetch and store player and team data.
- Store the collected data in the `data/` folder.

### 🧹 Data Preprocessing
- Use `data_preprocessing.py` to clean and preprocess the collected data for analysis and modeling.

### 🤖 Model Training and Evaluation
- Use `model_training.py` to train machine learning models on the preprocessed data.
- Use `model_evaluation.py` to evaluate the performance of the trained models.

### 📓 Jupyter Notebooks
- Use the notebooks in the `notebooks/` folder for exploratory data analysis and visualization.

## Contributing

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`git checkout -b feature-branch`).
3. 💻 Make your changes.
4. ✅ Commit your changes (`git commit -m 'Add some feature'`).
5. 🚀 Push to the branch (`git push origin feature-branch`).
6. 🔁 Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- 🙏 Thanks to the NBA API team for providing the tools and resources to access NBA data.
- 💡 Inspired by the ongoing advancements in machine learning and data science in sports analytics.
