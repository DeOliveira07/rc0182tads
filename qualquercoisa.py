import pandas as pd
import matplotlib.pyplot as plt

table = pd.DataFrame({
    'nome':['joao','maria','jose'],
    'idade':[20,23,24,24,24]
})
plt.hist(table['idade'])