import pandas as pd
import matplotlib.pyplot as plt


tabela = pd.DataFrame({
   'idade' : [21 ,23, 45, 31, 80],

   'nome' : ['João', 'Paulo', 'Gilberto', 'Pedro', 'Miguel']
})

tabela
plt.hist(tabela['idade'])