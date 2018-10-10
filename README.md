# recomend_system 
I have implemented two methods on user base collaborative filtering used as a recommendation system.

1.neighbor collaborative filtering
2.Latent factor models

1.neighbor collaborative filtering can be used two types. One method is a normal nieghbor CF. The other is expanded neighbor collaborative filtering proposed by Wang, Bin, et al.
"Recommendation strategy using expanded neighbor collaborative filtering." Control Conference (CCC), 2017 36th Chinese. IEEE, 2017.
(recomend_NCF.py)

2.For the Latent factor models, we used the genetic algorithm used in the following paper as an optimization method.
Ono, Isao, Shigenobu Kobayashi, and Koji Yoshida. "Optimal lens design by real-coded genetic algorithms using UNDX." Computer methods in applied mechanics and engineering 186.2-4 (2000): 483-497.
(recomend_GA.py)

# Dependency
Python3, numpy

# Usage
samples are recomend_NCF.py and recomend_GA.py.

# References
Dataset: MovieLens 100K Dataset
http://grouplens.org/datasets/movielens/


http://blog.echen.me/2011/10/24/winning-the-netflix-prize-a-summary/
http://www.slideshare.net/hamukazu/introduction-to-behavior-based-recommendation-system 
http://yifanhu.net/PUB/cf.pdf
https://hivecolor.com/id/47
https://www.slideshare.net/takemikami/ss-76817490
https://www.slideshare.net/hoxo_m/ss-53305070?next_slideshow=2 

# Authors
Suda Takeru
