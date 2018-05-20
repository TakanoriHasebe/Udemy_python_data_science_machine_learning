# ライブラリ
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline

# seaborn
# カウントプロット
sns.countplot('Affiliation', data=poll_df)

# seaborn
# 層別化
sns.countplot('Affiliation', data=poll_df, hue='Population')

# Seaborn
# plot
avg.plot(yerr = std, kind='bar', legend=False)

# Seaborn
# 支持率の変化がグラフによって可視化される。
poll_df.plot(x = 'End Date', y = ['Obama', 'Romney', 'Undecided'], marker='o', linestyle='')

# Seaborn
# 折れ線グラフの描画
fig = poll_df.plot('Start Date', 'Difference', figsize=(12, 4), marker='o', linestyle='-', color='purple')

# Seaborn
# ヒストグラムの描画
com_don.hist(bins=100)

# 横に棒グラフを描く
occupation_df.plot(kind = 'barh', figsize = (10, 12), cmap='seismic')

# lmplot
# 回帰曲線を描く
sns.lmplot('RM', 'Price', data = boston_df)

# タイトルを付与
plt.title('Logistic Function')














