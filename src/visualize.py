import matplotlib.pyplot as plt
import pandas as pd

def plot(df: pd.DataFrame):

    fig, axes = plt.subplots(3, 1, figsize = (10,10))
    
    axes[0].plot(df['TIME_PERIOD'], df['HICP'])
    axes[0].set_title('Euro area HICP inflation (YoY)')
    axes[0].set_ylabel('% annual rate of change')

    axes[1].plot(df['TIME_PERIOD'], df['BOP'])
    axes[1].set_title('Euro area current account balance')
    axes[1].set_ylabel('EUR millions')

    axes[2].plot(df['TIME_PERIOD'], df['DFR'], label = 'DFR')
    axes[2].plot(df['TIME_PERIOD'], df['MRR'], label = 'MRR')
    axes[2].plot(df['TIME_PERIOD'], df['MLFR'], label = 'MLFR')
    axes[2].set_title('ECB interest rates')
    axes[2].set_ylabel('% per annum')
    axes[2].legend()

    fig.tight_layout()
    fig.savefig("outputs/dashboard2.png", dpi=150)
    plt.close(fig)