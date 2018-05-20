# 回帰直線の係数を求めた
a, b = np.linalg.lstsq(X, Y)[0]

# -6から6まで500点作成
t = np.linspace(-6, 6, 500)





