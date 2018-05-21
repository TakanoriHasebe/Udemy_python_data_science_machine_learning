# ライブラリ
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline


# Pandas
# 平均値をとったDataFrameを作成
avg = pd.DataFrame(poll_df.mean())

# Pandas
# 標準偏差
std = pd.DataFrame(poll_df.std())
std.drop('Number of Observations', axis=0, inplace=True)

# Pandas
# DataFrameの作成
# pandasから新しいDAtaFrameの作成
poll_avg = pd.concat([avg, std], axis=1)
poll_avg.columns = ["Average", "STD"]

# DataFrame
# 列同士の引き算
poll_df['Difference'] = (poll_df.Obama - poll_df.Romney)/100

# DataFrame
# 無名関数の適用
poll_df[poll_df['Start Date'].apply(lambda x:x.startswith('2012-10'))]

# DataFrame
# 平均, 標準偏差
# 寄付金の平均・標準偏差を見ている
don_mean = donor_df['contb_receipt_amt'].mean()
don_std = donor_df['contb_receipt_amt'].std()
print('平均 {:0.2f} 標準偏差{:0.2f}'.format(don_mean, don_std))

# Pandas
# csvの読み取り
donor_df = pd.read_csv('Election_Donor_Data.csv')

# DataFrame
# 寄付金の人数を出している
donor_df['contb_receipt_amt'].value_counts()

# DataFrame
# コピーする
top_donor = donor_df['contb_receipt_amt'].copy()

# DataFrame
# 値で並び替え
top_donor.sort_values()

# DataFrame
# DataFrameのなかで条件をつける
top_donor = top_donor[top_donor > 0]

# DataFrame
# いくら寄付した人が何人いるかということのTOP 10を見ることができる。
top_donor.value_counts().head(10)

# DataFrame
# 同じ名前を１つにまとめる
candidates = donor_df.cand_nm.unique()

# DataFrame
# 所属政党の辞書
party_map = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

# 辞書をDataFrameに適用する
# 新しい列を作成する
donor_df['Party'] = donor_df.cand_nm.map(party_map)s

# DataFrame
# Groupby
donor_df.groupby('cand_nm')['contb_receipt_amt'].count().sort_values()

# DataFrame
# 寄付の額が100万ドル以上の職業に絞る
occupation_df = occupation_df[occupation_df.sum(1) > 1000000]

# DataFrame
# いらない行を削除
occupation_df.drop(['INFORMATION REQUESTED PER BEST EFFORTS', 'INFORMATION REQUESTED'], axis = 0, inplace=True)

# DataFrame
# CEOとC.E.O.をまとめる
occupation_df.loc['CEO'] = occupation_df.loc['CEO'] + occupation_df.loc['C.E.O.'] 

# DataFrame
# DataFrameに変換する
boston_df = DataFrame(boston.data)

# DataFrame
# 列名をつける
boston_df.columns = boston.feature_names

# DataFrame
# 関数を適用する
def affair_check(x):
    if x != 0:
        return 1
    else:
        return 0
df['Had_Affair'] = df['affairs'].apply(affair_check)

# 列方向に結合する
X = pd.concat([X, dummies], axis=1)

# 多次元配列から１次元配列に変換
Y = Y.values

































