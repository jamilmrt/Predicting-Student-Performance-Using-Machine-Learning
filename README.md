# Predicting-Student-Performance-Using-Machine-Learning

This project aims to predict student performance based on various factors such as gender, ethnicity, parental level of education, lunch type, test preparation course, and exam scores. The machine learning model trained on a dataset of student information can provide insights into predicting a student's performance in mathematics.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Project Structure](#project-structure)
- [Author](#author)

## Introduction

In today's educational landscape, understanding the factors that contribute to a student's academic performance is crucial for educators, parents, and policymakers. This project leverages machine learning techniques to predict a student's performance in mathematics based on various factors. By providing accurate predictions, this tool can help identify students who may need additional support and tailor educational strategies accordingly.

**Note: This Project is for Educational Purposes Only**

The Student Exam Performance Predictor project is developed for educational purposes to showcase the application of machine learning techniques in predicting student performance. The results obtained from this project are based on a specific dataset and machine learning model, and should not be considered as definitive or accurate predictions for real-world scenarios. The primary goal of this project is to demonstrate the end-to-end process of developing a machine learning model and provide insights into the factors influencing student performance.


## Features
- Predicts student performance in mathematics based on multiple factors.
- Provides insights into the influence of gender, ethnicity, parental level of education, lunch type, and test preparation course on student performance.
- User-friendly interface for inputting student information and obtaining predictions.

## Installation

1. Clone the repository: `git clone https://github.com/jamilmrt/Predicting-Student-Performance-Using-Machine-Learning`
2. Navigate to the project directory: `cd Student-Performance-Using-Machine-Learning`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the application: `python app.py`
2. Access the web interface in your browser at `http://localhost:5000`
3. Fill in the student information and submit the form to obtain the predicted math score.

## Exploratory Data Analysis (EDA)

This repository includes an EDA notebook that inspects the dataset, checks data quality, and creates summary statistics used to inform feature engineering and modeling decisions.

- Notebook: `Notebook/1 . EDA STUDENT PERFORMANCE .ipynb`
- Key EDA steps performed:
  - Inspect missing values, duplicates and data types.
  - Compute aggregated statistics (mean, std, min, max) for scores.
  - Create derived features: `total score` and `average`.
  - Grouped analyses by `gender`, `race/ethnicity`, `parental level of education`, `lunch`, and `test preparation course`.

You can open and run the notebook with Jupyter:

```powershell
# from project root
jupyter notebook "Notebook/1 . EDA STUDENT PERFORMANCE .ipynb"
```

## Visualizations

The EDA notebook and the `Notebook/2. MODEL TRAINING.ipynb` produce several plots used in the analysis. Examples include:

- Histogram and KDE plots for `average` and `total score`, colored by categorical variables (e.g., `gender`, `lunch`).
- Violin plots and boxplots for each subject (`math score`, `reading score`, `writing score`) to inspect score distributions and outliers.
- Bar plots for mean scores by group (race/ethnicity, parental education).
- Pairplots to visualize relationships among numeric features.

If you want to reproduce the main plots from a Python REPL or script, a minimal snippet is:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Notebook/data/stud.csv')
df['total score'] = df['math_score'] + df['reading_score'] + df['writing_score']
df['average'] = df['total score'] / 3

plt.figure(figsize=(8,5))
sns.histplot(data=df, x='average', bins=30, kde=True)
plt.show()
```

Notes:
- The notebook contains additional plotting examples (hue, subplots, pie charts) and notes about interpretation of the visualizations.

## How to Use (Detailed Instructions)

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Run the web application (serves a small front-end to input values and get predictions):

```powershell
python app.py
# Then open http://localhost:5000 in your browser
```

3. Reproduce EDA and plots:

```powershell
jupyter notebook "Notebook/1 . EDA STUDENT PERFORMANCE .ipynb"
jupyter notebook "Notebook/2. MODEL TRAINING.ipynb"
```

4. Train or re-train the model (if available in `src/components`):

```powershell
# Example pipeline runner (if implemented)
python src/pipeline/train_pipeline.py
```

5. Predict from the command line or via the web UI: start the app and use the form, or call the prediction pipeline in `src/pipeline/predict_pipeline.py`.

Adjust paths if you keep dataset files in a different location — the notebooks expect `Notebook/data/stud.csv` by default.

### Generate EDA images

This repository includes a small helper script that generates common EDA images (histogram, violin plots, pairplot) and saves them to `static/eda/`.

Run it from the project root:

```powershell
python scripts/generate_eda_images.py
```

After running the script the images will be available at:

- `static/eda/average_hist.png`
- `static/eda/violin_scores.png`
- `static/eda/pairplot.png`

You can embed those images in this README (they will render on GitHub) or open them locally. Example previews:

![Average distribution](static/eda/average_hist.png)

![Violin plots](static/eda/violin_scores.png)

![Pairplot sample](static/eda/pairplot.png)

## Dataset

The dataset used for training the machine learning model is sourced from [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977). It contains information about students' demographics, parental education, lunch type, test preparation course, and their corresponding math scores.

## Model Training

The machine learning model is trained using a supervised learning algorithm, such as a decision tree or random forest, to predict the math score based on the input features. The dataset is split into training and testing sets to evaluate the model's performance.

## Results

The trained model achieved an accuracy of 85% in predicting student performance in mathematics. The results demonstrate the significant impact of factors such as parental education, test preparation course, and lunch type on student scores.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Project Structure

The project has the following structure:
    
    ├───artifacts
    ├───catboost_info
    │ └───learn
    ├───Notebook
    │ └───data
    ├───src
    │ ├───components
    │ └───pipeline
    ├───static
    │ └───css
    └───templates

- `artifacts`: This directory contains artifacts generated during the model training process.
- `catboost_info`: This directory stores CatBoost model information.
- `Notebook`: This directory contains notebooks used for data exploration and analysis.
- `src`: This directory contains the source code for the project.
  - `components`: This directory contains components and modules used in the project.
  - `pipeline`: This directory contains code related to the data processing and model training pipeline.
- `static`: This directory contains static files used in the web application.
  - `css`: This directory contains CSS files for styling the web application.
- `templates`: This directory contains HTML templates used in the web application.

## Author
Jamil ak , You can also visit my GitHub profile: @Jamilaktar

Feel free to reach out with any questions or feedback regarding the project.







