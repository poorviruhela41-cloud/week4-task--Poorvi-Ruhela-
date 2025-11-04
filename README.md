# 🧠 Python Mini Projects Collection

This repository contains **four Python mini projects** that demonstrate key programming concepts like **Object-Oriented Programming (OOP)**, **Web Scraping**, **Data Visualization**, and **Data Analysis** using libraries like `pandas`, `matplotlib`, and `requests`.

---

## 🎬 Project 1: Movie Recommendation System

### 🧩 Description
A simple recommendation system that suggests movies based on user preferences such as genre, rating, and year.  
It uses a dataset (CSV) of popular movies and filters them using user input.

### 🧠 Approach
- Loaded movie data using **Pandas DataFrame**.
- Filtered movies based on **genre, rating, and year**.
- Sorted results by IMDb rating.
- Displayed top 5 recommendations.

### ⚙️ Steps to Run
1. Place your `movies.csv` dataset in the project folder.  
2. Run:
   ```bash
   python movie_recommendation.py

3. Enter your preferred genre, minimum rating, and year.



📸 Sample Output

Enter genre: Action
Minimum rating: 7
Movies released after year: 2015

Top Recommendations:
1. Mad Max: Fury Road (8.1)
2. John Wick (7.9)
3. Mission Impossible: Fallout (7.8)

⚡ Challenges Faced

Handling missing or invalid data in the dataset.

Making the filtering logic efficient.

Finding a suitable public movie dataset.



---

🎓 Project 2: Integrated Student Dashboard (OOP + Pandas + CSV + Visualization)

🧩 Description

A menu-driven console app to manage student records, analyze performance, and visualize scores using histograms and bar charts.

🧠 Approach

Designed a Student class to store name, roll number, and marks.

Implemented CSV file storage using Pandas.

Added functions for average calculation, top performer detection, and pass/fail stats.

Used Matplotlib for histogram and subject-wise average bar chart.


⚙️ Steps to Run

1. Navigate to the project folder:

cd student_dashboard


2. Run the main program:

python main.py


3. Follow on-screen menu options.



📸 Sample Plots

Histogram of Scores



Bar Chart of Average Marks



⚡ Challenges Faced

Structuring the project into multiple modules (models/, utils/).

Handling invalid numeric inputs and missing CSV files.

Ensuring data persistence between runs.



---

🌐 Project 3: Social Media Scraper & Analyzer

🧩 Description

A Python program that scrapes posts, hashtags, or tweets from a social media platform (e.g., Twitter or Instagram using API/scraping) and analyzes trending keywords and sentiment.

🧠 Approach

Used BeautifulSoup / Tweepy (for API-based scraping).

Stored data in CSV using Pandas.

Performed text analysis to extract top hashtags, most common words.

Visualized frequency using bar plots and word clouds.


⚙️ Steps to Run

1. Install dependencies:

pip install pandas matplotlib beautifulsoup4 requests wordcloud


2. Run:

python social_media_analyzer.py


3. Input topic/hashtag to scrape.



📸 Sample Outputs

Top Hashtags Bar Chart



Word Cloud of Frequent Words



⚡ Challenges Faced

Handling rate limits of APIs.

Cleaning and normalizing scraped text data.

Dealing with encoding issues in large datasets.



---

💰 Project 4: Expense Tracker (CSV + Visualization)

🧩 Description

A command-line expense management system that tracks daily expenses, stores them in CSV, and visualizes spending patterns.

🧠 Approach

Created a CSV file to store expenses (date, category, amount, description).

Used Pandas to calculate total, category-wise, and monthly expenses.

Used Matplotlib to generate bar and pie charts.


⚙️ Steps to Run

1. Run the script:

python expense_tracker.py


2. Add expenses, view totals, or generate charts.



📸 Sample Outputs

Category-wise Expense Pie Chart



Monthly Trend Bar Graph



⚡ Challenges Faced

Managing file read/write errors gracefully.

Formatting dates consistently.

Making charts readable for all expense ranges.



---

🧮 Common Libraries Used

pandas

matplotlib

requests

beautifulsoup4

wordcloud

csv



---

🚀 How to Run All Projects

1. Clone this repository:

git clone https://github.com/yourusername/Python-Mini-Projects.git


2. Install dependencies:

pip install -r requirements.txt


3. Navigate to each project folder and run the corresponding .py file.


