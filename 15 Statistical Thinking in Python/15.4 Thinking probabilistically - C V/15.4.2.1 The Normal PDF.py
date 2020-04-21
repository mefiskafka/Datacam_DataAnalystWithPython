"""
The Normal PDF
In this exercise, you will explore the Normal PDF and also learn a way to plot a PDF of a known distribution using hacker statistics. Specifically, you will plot a Normal PDF for various values of the variance.

Instructions
100 XP
Instructions
100 XP
Draw 100,000 samples from a Normal distribution that has a mean of 20 and a standard deviation of 1. Do the same for Normal distributions with standard deviations of 3 and 10, each still with a mean of 20. Assign the results to samples_std1, samples_std3 and samples_std10, respectively.
Plot a histograms of each of the samples; for each, use 100 bins, also using the keyword arguments normed=True and histtype='step'. The latter keyword argument makes the plot look much like the smooth theoretical PDF. You will need to make 3 plt.hist() calls.
Hit 'Submit Answer' to make a legend, showing which standard deviations you used, and show your plot! There is no need to label the axes because we have not defined what is being described by the Normal distribution; we are just looking at shapes of PDFs.

El PDF normal
En este ejercicio, explorará el PDF normal y también aprenderá una manera de trazar un PDF de una distribución conocida utilizando estadísticas de hackers. Específicamente, trazará un PDF normal para varios valores de la varianza.

Instrucciones
100 XP
Instrucciones
100 XP
Dibuje 100.000 muestras de una distribución normal que tenga una media de 20 y una desviación estándar de 1. Haga lo mismo para las distribuciones normales con desviaciones estándar de 3 y 10, cada una con una media de 20. Asigne los resultados a samples_std1, samples_std3 y samples_std10, respectivamente.
Trazar un histograma de cada una de las muestras; para cada uno, utilice 100 bins, también utilizando los argumentos de palabra clave normed-True y histtype''step'. Este último argumento de palabra clave hace que la gráfica se parezca mucho al PDF teórico suave. Usted tendrá que hacer 3 plt.hist() llamadas.
¡Pulsa 'Enviar respuesta' para crear una leyenda, mostrando qué desviaciones estándar usaste, y muestra tu trama! No hay necesidad de etiquetar los ejes porque no hemos definido lo que se describe en la distribución Normal; sólo estamos mirando formas de archivos PDF.
"""
import numpy as np
import matplotlib.pyplot as plt

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10

samples_std1=  np.random.normal(20,1,size= 100000)
samples_std3=  np.random.normal(20,3,size= 100000)
samples_std10= np.random.normal(20,10,size= 100000)


# Make histograms
_ = plt.hist(samples_std1, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std3, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std10, bins=100, normed=True, histtype='step')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
