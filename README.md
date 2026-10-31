AI-Powered Data Cleaning System Using MySQL & Streamlit


This project is an interactive web-based data cleaning tool built using
Python, Streamlit, MySQL, Pandas, and Machine Learning (Isolation Forest).
It helps detect and clean common data-quality issues such as:


Missing values


Duplicate records


Anomalies (using IsolationForest)


Incorrect or inconsistent values


This project is made as part of the Data Management & AI Integration (ABAI2009L) course.


🚀 Features


✔ Connects directly to MySQL
✔ Shows missing values
✔ Detects duplicates (with column selection)
✔ ML-based anomaly detection
✔ Cleans data with multiple options
✔ Saves cleaned data back to MySQL
✔ Allows user to download cleaned CSV
✔ Streamlit-based UI (very easy to use)


🛠️ Tech Stack


Python 3.10


Streamlit


MySQL Workbench


Pandas


Scikit-Learn


mysql-connector-python


Anaconda Environment

## Local setup

Install dependencies in a virtual environment:

```bash
python -m pip install streamlit pandas numpy scikit-learn mysql-connector-python
```

Set `MYSQL_PASSWORD` in your shell before launching the app. Optional settings are `MYSQL_HOST` (default `localhost`), `MYSQL_USER` (default `root`), and `MYSQL_DATABASE` (default `data_cleaning_system`). Do not commit passwords.

```bash
python -m streamlit run app.py
```

## Repository guide

- `app.py`: Streamlit application.
- `data_base.sql`: demo database setup; it drops and recreates `data_cleaning_system`, so run it only against a disposable local database.
- CSV files: input/output examples.
- DOCX and PDF files: course report and presentation.

Use a dedicated local database account for development. The database password previously present in the source must be rotated if it was used; removing it from the current file does not remove it from Git history.
