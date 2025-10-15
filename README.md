# 🌾 Jiji Agriculture & Foodstuff Analysis

A data analysis project that scrapes and analyzes agricultural product listings from [Jiji.ng](https://jiji.ng), Nigeria's leading online marketplace. Gain insights into pricing patterns, market distribution, and regional trends.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=flat&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Live Demo

[View Live App](https://jiji-agriculture-foodstuff-233.streamlit.app/)

![Demo GIF](https://user-images.githubusercontent.com/yourusername/demo.gif)  
*Interactive demo of the Streamlit app showcasing analysis and visualizations.*

---

## 📊 Features

- **Web Scraping**: Automated data collection from Jiji.ng
- **Price Analysis**: Total, max, min prices with outlier detection
- **Regional Insights**: Price variations across Nigerian locations
- **Interactive Visualizations**: Treemaps, bar charts, pie charts
- **Multi-page App**: Clean Streamlit interface with dark theme

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Netlution/Jiji-Agriculture-Foodstuff.git
cd Jiji-Agriculture-Foodstuff

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py

# 📁 Project Structure

Jiji-Agriculture-Foodstuff/
├── app.py                 # Main application
├── pages/                 # App sections
│   ├── About.py           # Project overview
│   ├── Analysis.py        # Data insights
│   ├── Visualization.py   # Charts & graphs
│   └── Contact.py         # Contact form
├── Data/                  # Scraped dataset
└── static/                # Images & assets

# 🛠️ Tech Stack

<details> <summary>Click to expand</summary>
🚀Frontend: Streamlit
🚀Data Processing: Pandas, NumPy
🚀Web Scraping: BeautifulSoup, Requests
🚀Visualization: Plotly
🚀Data Source: Jiji.ng Agriculture & Foodstuff category
</details>

# 📈 Analysis Sections
📁Table Analysis: Summary statistics and outlier detection
📁Price Analysis: Product and location-based grouping
📁Visualizations: Interactive charts and graphs
📁Market Insights: Regional comparisons and trends
