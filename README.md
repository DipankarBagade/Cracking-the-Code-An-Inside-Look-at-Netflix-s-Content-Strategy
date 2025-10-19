## 📺 Cracking the Code: An Inside Look at Netflix's Content Strategy

### 🎯 Overview

This project explores Netflix's vast catalog of movies and TV shows to uncover **insights behind its content strategy** — including patterns in production countries, popular genres, release trends, and more.
By analyzing the **Netflix Titles dataset** from Kaggle, we apply **data cleaning, visualization, and storytelling** techniques to understand how Netflix curates and balances its global content portfolio.

---

### 🧠 Project Objectives

* Understand the **distribution of content** (Movies vs TV Shows).
* Analyze **content growth over time** — how Netflix has evolved.
* Identify **top countries and directors** contributing to Netflix’s library.
* Explore **genre popularity trends** across different years.
* Build an **interactive Streamlit dashboard** for visual exploration.

---

### 🧰 Tech Stack

| Category        | Tools Used                                                                               |
| --------------- | ---------------------------------------------------------------------------------------- |
| Language        | Python 3.10+                                                                             |
| Data Handling   | Pandas, NumPy                                                                            |
| Visualization   | Matplotlib, Seaborn, Plotly                                                              |
| Dashboard       | Streamlit                                                                                |
| Data Source     | [Netflix Titles Dataset (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows) |
| Version Control | Git, GitHub                                                                              |

---

### 🗂️ Project Structure

```
netflix-content-strategy/
│
├── venv/                     # Virtual environment
├── data/                     # Dataset (Netflix_titles.csv)
├── notebooks/                # Jupyter notebooks for analysis
│   └── Netflix_EDA.ipynb
├── src/                      # Source code for dashboard/app
│   └── netflix_dashboard.py
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore
```

---

### ⚙️ Setup Instructions

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DipankarBagade/Cracking-the-Code-An-Inside-Look-at-Netflix-s-Content-Strategy.git
cd Cracking-the-Code-An-Inside-Look-at-Netflix-s-Content-Strategy
```

#### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate   # On Windows
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Dashboard

```bash
streamlit run src/netflix_dashboard.py
```

---

### 📊 Exploratory Data Analysis Highlights

* **Content Type Distribution:** Ratio of Movies vs TV Shows.
* **Top Genres:** Most produced genres by count.
* **Country Insights:** Leading countries contributing to Netflix’s catalog.
* **Release Trends:** Year-wise growth of new titles.
* **Ratings Distribution:** Viewer classification insights.

---

### 🚀 Next Steps

* Apply **machine learning models** to predict content popularity.
* Explore **recommendation systems** using collaborative filtering.
* Analyze **language-wise** or **duration-based** viewing trends.

---

### 🧑‍💻 Author

**Dipankar Bagade**
📍 Passionate about Data Science, ML, and AI-driven insights
🔗 [GitHub Profile](https://github.com/DipankarBagade)
