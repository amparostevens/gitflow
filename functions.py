
def top_retweeted(df):
    top = df.sort_values(by='retweetCount')
    top.head(10)