📘 Data Wrangling & DataFrame Processing Project.

This repository contains a collection of Python scripts focused on data cleaning, currency transformation, and structured DataFrame manipulation using pandas.
The project demonstrates:

Cleaning messy numeric/currency data

Transforming text-based datasets into tidy formats

Subsetting rows & columns

Renaming DataFrame fields

Filtering data using logical conditions

Working with the classic mtcars dataset

📁 Repository Structure

Project/
│
├── question_1.py
├── question_2.py
├── question_3.py
├── question_4.py
├── question_5.py
├── question_6.py
├── question_7.py
├── question_8.py
├── question_9.py
│
├── mtcars.csv
├── sales.txt
├── sales_cleaned.csv
│
└── README.md

📝 Project Overview

This project includes 9 standalone Python scripts, each performing a different data processing task.
All scripts run independently and produce printed or saved output.

🔍 Script Summaries
✔ 1. Currency Data Cleaning (question_1.py)

Reads raw currency values from sales.txt

Cleans symbols, formatting inconsistencies, and mixed decimal separators

Converts GBP → USD (1 GBP = 1.25 USD)

Outputs a new tidy file: sales_cleaned.csv

✔ 2. Remove a Column (question_2.py)

Loads mtcars.csv and prints all columns except hp.

✔ 3. Select Specific Columns (question_3.py)

Displays only:

mpg, hp, vs, am, gear

✔ 4. Create a Renamed Subset (question_4.py)

Creates cars_m_h with:

mpg → miles_per_gallon

hp → horse_power

✔ 5. Rename Columns Back (question_5.py)

Converts the names back to:

mpg

hp

✔ 6. Subset Rows (question_6.py)

Extracts rows 10 to 35 into cars_m_h_s.

✔ 7. Remove Duplicates (question_7.py)

Prints cars_m_h_s without any repeated rows.

✔ 8. Conditional Filtering (question_8.py)

Prints observations where:

mpg > 20 AND hp > 100

✔ 9. Select a Specific Car (question_9.py)

Reliably extracts data for “Lotus Europa”, regardless of how mtcars.csv stores the model name.

▶️ How to Run
1. Install Dependencies
pip install pandas

2. Run any script

Example:

python question_4.py


Each script prints results directly to the terminal.

📂 Included Data Files
mtcars.csv

Classic dataset containing specifications for multiple car models.

sales.txt

Raw unstructured currency values used for data-cleaning operations.

🎯 Skills Demonstrated

Data cleaning & transformation

Working with inconsistent text formats

Creating clean, structured data outputs

Efficient DataFrame manipulation

Conditional filtering and indexing


Safe handling of real-world datasets

