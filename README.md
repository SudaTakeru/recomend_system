# recomend_system

レコメンドシステムとして使われるユーザーベース協調フィルタリングについて二つの手法を実装してみました。

1.近傍法
2.Latent factor models

1.近傍法は通常の近傍法と下記の論文で提案されたECFについてを利用できます。
Wang, Bin, et al. "Recommendation strategy using expanded neighbor collaborative filtering." Control Conference (CCC), 2017 36th Chinese. IEEE, 2017.
(recomend_NCF.py)

2.Latent factor modelsについては最適化の手法として下記の論文で利用されている遺伝的アルゴリズムを用いてみました。
Ono, Isao, Shigenobu Kobayashi, and Koji Yoshida. "Optimal lens design by real-coded genetic algorithms using UNDX." Computer methods in applied mechanics and engineering 186.2-4 (2000): 483-497.
(recomend_GA.py)

# Dependency
Python3, numpy

# Usage
サンプルがrecomend_NCF.pyとrecomend_GA.pyです。こちらを参照してください。

Dataset: MovieLens 100K Dataset
http://grouplens.org/datasets/movielens/

参考:
http://blog.echen.me/2011/10/24/winning-the-netflix-prize-a-summary/
http://www.slideshare.net/hamukazu/introduction-to-behavior-based-recommendation-system 
http://yifanhu.net/PUB/cf.pdf
https://hivecolor.com/id/47
https://www.slideshare.net/takemikami/ss-76817490
https://www.slideshare.net/hoxo_m/ss-53305070?next_slideshow=2 

# Authors
Suda Takeru
