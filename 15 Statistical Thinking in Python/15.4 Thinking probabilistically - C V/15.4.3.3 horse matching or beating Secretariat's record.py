"""
What are the chances of a horse matching or beating Secretariat's record?
Assume that the Belmont winners' times are Normally distributed (with the 1970 and 1973 years removed), what is the probability that the winner of a given Belmont Stakes will run it as fast or faster than Secretariat?

Instructions
100 XP
Take 1,000,000 samples from the normal distribution using the np.random.normal() function. The mean mu and standard deviation sigma are already loaded into the namespace of your IPython instance.
Compute the fraction of samples that have a time less than or equal to Secretariat's time of 144 seconds.

¿Cuáles son las posibilidades de que un caballo coincida o supere el historial de la Secretaría?
Supongamos que los tiempos de los ganadores de Belmont se distribuyen normalmente (con los años 1970 y 1973 eliminados), ¿cuál es la probabilidad de que el ganador de una determinada Belmont Stakes lo ejecute tan rápido o más rápido que Secretariat?

Instrucciones
100 XP
Tome 1.000.000 de muestras de la distribución normal utilizando la función np.random.normal(). La media mu y la desviación estándar sigma ya están cargadas en el espacio de nombres de la instancia de IPython.
Calcular la fracción de muestras que tienen un tiempo menor o igual al tiempo de la Secretaría de 144 segundos.


"""
import numpy as np

# Take a million samples out of the Normal distribution: samples
samples = np.random.normal(mu,sigma, size=1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = np.sum(samples <= 144) / len(samples)


# Print the result
print('Probability of besting Secretariat:', prob)