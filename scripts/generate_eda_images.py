import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def main():
    data_path = os.path.join('Notebook', 'data', 'stud.csv')
    out_dir = os.path.join('static', 'eda')
    ensure_dir(out_dir)

    if not os.path.exists(data_path):
        print(f"Data file not found: {data_path}")
        return

    df = pd.read_csv(data_path)

    # Basic derived features
    if 'total score' not in df.columns:
        df['total score'] = df.get('math_score', 0) + df.get('reading_score', 0) + df.get('writing_score', 0)
    if 'average' not in df.columns:
        df['average'] = df['total score'] / 3

    # 1) Average distribution (hist + KDE)
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='average', bins=30, kde=True, color='skyblue')
    plt.title('Average Score Distribution')
    plt.tight_layout()
    avg_path = os.path.join(out_dir, 'average_hist.png')
    plt.savefig(avg_path, dpi=150)
    plt.close()
    print(f'Wrote {avg_path}')

    # 2) Violin plots for each subject
    subjects = []
    if 'math_score' in df.columns:
        subjects.append('math_score')
    if 'reading_score' in df.columns:
        subjects.append('reading_score')
    if 'writing_score' in df.columns:
        subjects.append('writing_score')

    if subjects:
        plt.figure(figsize=(10, 6))
        sns.violinplot(data=df[subjects], palette='Set2')
        plt.title('Score distributions by subject')
        plt.tight_layout()
        violin_path = os.path.join(out_dir, 'violin_scores.png')
        plt.savefig(violin_path, dpi=150)
        plt.close()
        print(f'Wrote {violin_path}')

    # 3) Pairplot for numeric scores (can be slow on large datasets)
    numeric_cols = [c for c in ['math_score', 'reading_score', 'writing_score', 'average'] if c in df.columns]
    if numeric_cols:
        try:
            g = sns.pairplot(df[numeric_cols].sample(min(len(df), 500)), corner=True)
            pair_path = os.path.join(out_dir, 'pairplot.png')
            g.savefig(pair_path)
            plt.close()
            print(f'Wrote {pair_path}')
        except Exception as e:
            print('Failed to create pairplot:', e)


if __name__ == '__main__':
    main()
