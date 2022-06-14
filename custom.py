import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class KmerTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, size=3):
        self.size = size

    def get_kmers(self, X):
        '''
        Create a list of rolling kmer's of size `size` from a sequence
        '''
        return X.apply(
            lambda x: ' '.join(
                tuple(''.join(x[i: i+self.size])
                      for i in range(len(x) - self.size + 1))
            )
        )

    def fit(self,X,y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        return self.get_kmers(X)
    
