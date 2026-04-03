import pandas as pd

def load_data(path="gold.csv"):
    df = pd.read_csv(path)

    print("Original columns:", df.columns)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Date
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.sort_values('Date')

    # Detect Close column
    if 'Close' not in df.columns:
        for col in df.columns:
            if 'close' in col.lower() or 'price' in col.lower():
                df.rename(columns={col: 'Close'}, inplace=True)

    # Keep only required columns
    if 'Close' not in df.columns:
        raise ValueError("No Close/Price column found in dataset")

    df = df[['Close']].copy()

    # Clean numbers
    df['Close'] = df['Close'].astype(str).str.replace(',', '')
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    # Drop NaN rows FIRST
    df = df.dropna()

    print("After cleaning:", df.shape)

    return df


def feature_engineering(df):
    # SMALL features (safe)
    df['Lag1'] = df['Close'].shift(1)
    df['Lag2'] = df['Close'].shift(2)

    # Drop NaN
    df = df.dropna().reset_index(drop=True)

    print("After feature engineering:", df.shape)

    return df