import numpy as np
from sklearn.decomposition import PCA

class OnlinePCA:
    def __init__(self, n_components=2, window_size=100, threshold=0.1):
        self.pca = PCA(n_components=n_components)
        self.window_size = window_size
        self.threshold = threshold
        self.reset()

    def reset(self):
        self.X = np.empty((0, self.pca.n_components))
        self.changepoints = []

    def update(self, x):
        self.X = np.vstack([self.X, x])

        if len(self.X) > self.window_size:
            self.X = self.X[1:]

        if len(self.X) > 1:
            self.pca.fit(self.X)
            explained_variance = self.pca.explained_variance_ratio_
            
            if len(self.X) % 10 == 0:
                print("expl var", explained_variance)
            explained_variance_change = np.abs(explained_variance[0] - explained_variance[1])

            # print('explained variance change',explained_variance_change)
            
            if explained_variance_change > self.threshold and len(self.X) > self.window_size:
                self.changepoints.append(len(self.X))
                
            #     self.reset()

# example usage
online_pca = OnlinePCA()


for i in range(1000):
    x = np.random.normal(size=(1, 2))
    if i > 500:
        online_pca.update(x+5*np.sin(np.random.normal()))
    else:
        online_pca.update(x)
        

print(online_pca.changepoints)
