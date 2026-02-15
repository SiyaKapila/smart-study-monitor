import pandas as pd
import os

FILE = "study_history.csv"
def save_session(duration):

    df = pd.DataFrame([[duration]], columns=["duration"])

    if os.path.exists(FILE):
        df.to_csv(FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(FILE, index=False)
def show_stats():

    if not os.path.exists(FILE):
        print("No study history yet.")
        return

    df = pd.read_csv(FILE)

    print("Total Sessions:", len(df))
    print("Average Duration:", int(df["duration"].mean()), "seconds")

