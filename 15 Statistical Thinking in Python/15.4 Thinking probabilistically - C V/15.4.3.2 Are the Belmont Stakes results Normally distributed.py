"""
Are the Belmont Stakes results Normally distributed?
Since 1926, the Belmont Stakes is a 1.5 mile-long race of 3-year old thoroughbred horses. Secretariat ran the fastest Belmont Stakes in history in 1973. While that was the fastest year, 1970 was the slowest because of unusually wet and sloppy conditions. With these two outliers removed from the data set, compute the mean and standard deviation of the Belmont winners' times. Sample out of a Normal distribution with this mean and standard deviation using the np.random.normal() function and plot a CDF. Overlay the ECDF from the winning Belmont times. Are these close to Normally distributed?

Note: Justin scraped the data concerning the Belmont Stakes from the Belmont Wikipedia page.

Instructions
100 XP
Instructions
100 XP
Compute mean and standard deviation of Belmont winners' times with the two outliers removed. The NumPy array belmont_no_outliers has these data.
Take 10,000 samples out of a normal distribution with this mean and standard deviation using np.random.normal().
Compute the CDF of the theoretical samples and the ECDF of the Belmont winners' data, assigning the results to x_theor, y_theor and x, y, respectively.
Hit submit to plot the CDF of your samples with the ECDF, label your axes and show the plot.

¿Los resultados de Belmont Stakes se distribuyen normalmente?
Desde 1926, el Belmont Stakes es una carrera de 1,5 millas de largo de caballos pura sangre de 3 años de edad. Secretariat corrió las apuestas Belmont más rápidas de la historia en 1973. Si bien ese fue el año más rápido, 1970 fue el más lento debido a condiciones inusualmente húmedas y descuidadas. Con estos dos valores atípicos eliminados del conjunto de datos, calcule la media y la desviación estándar de los tiempos de los ganadores de Belmont. Muestre una distribución normal con esta media y desviación estándar utilizando la función np.random.normal() y trace un CDF. Superponga el ECDF de los tiempos ganadores de Belmont. ¿Están cerca de Distribuirse normalmente?

Nota: Justin raspalos los datos relativos a Belmont Stakes de la página de Wikipedia de Belmont.

Instrucciones
100 XP
Instrucciones
100 XP
Calcular la media y la desviación estándar de los tiempos de los ganadores de Belmont con los dos valores atípicos eliminados. La matriz NumPy belmont_no_aliers tiene estos datos.
Saque 10.000 muestras de una distribución normal con esta media y desviación estándar utilizando np.random.normal().
Calcular el CDF de las muestras teóricas y el ECDF de los datos de los ganadores de Belmont, asignando los resultados a x_theor, y_theor y x, y, respectivamente.
Pulse Enviar para trazar el CDF de sus muestras con el ECDF, etiquetar los ejes y mostrar la gráfica.


"""

import numpy as np

# Compute mean and standard deviation: mu, sigma
mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)


# Sample out of a normal distribution with this mu and sigma: samples

samples = np.random.normal(mu,sigma, size=10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = ecdf(samples)
x, y = ecdf(belmont_no_outliers)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()