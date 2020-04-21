"""
Relationship between Binomial and Poisson distributions
You just heard that the Poisson distribution is a limit of the Binomial distribution for rare events. This makes sense if you think about the stories. Say we do a Bernoulli trial every minute for an hour, each with a success probability of 0.1. We would do 60 trials, and the number of successes is Binomially distributed, and we would expect to get about 6 successes. This is just like the Poisson story we discussed in the video, where we get on average 6 hits on a website per hour. So, the Poisson distribution with arrival rate equal to np approximates a Binomial distribution for n Bernoulli trials with probability p of success (with n large and p small). Importantly, the Poisson distribution is often simpler to work with because it has only one parameter instead of two for the Binomial distribution.

Let's explore these two distributions computationally. You will compute the mean and standard deviation of samples from a Poisson distribution with an arrival rate of 10. Then, you will compute the mean and standard deviation of samples from a Binomial distribution with parameters n and p such that np=10.

Instructions
100 XP
Instructions
100 XP
Using the np.random.poisson() function, draw 10000 samples from a Poisson distribution with a mean of 10.
Make a list of the n and p values to consider for the Binomial distribution. Choose n = [20, 100, 1000] and p = [0.5, 0.1, 0.01] so that np is always 10.
Using np.random.binomial() inside the provided for loop, draw 10000 samples from a Binomial distribution with each n, p pair and print the mean and standard deviation of the samples. There are 3 n, p pairs: 20, 0.5, 100, 0.1, and 1000, 0.01. These can be accessed inside the loop as n[i], p[i].


Relación entre las distribuciones de Binomial y Poisson
Acabas de escuchar que la distribución de Poisson es un límite de la distribución de Binomial para eventos raros. Esto tiene sentido si piensas en las historias. Digamos que hacemos un ensayo de Bernoulli cada minuto durante una hora, cada uno con una probabilidad de éxito de 0.1. Haríamos 60 pruebas, y el número de éxitos se distribuye binomialmente, y esperaríamos obtener alrededor de 6 éxitos. Esto es como la historia de Poisson que discutimos en el video, donde obtenemos en promedio 6 visitas en un sitio web por hora. Por lo tanto, la distribución de Poisson con una tasa de llegada igual a np se aproxima a una distribución Binomial para n ensayos de Bernoulli con probabilidad p de éxito (con n grande y p pequeño). Es importante destacar que la distribución de Poisson suele ser más sencilla de trabajar porque solo tiene un parámetro en lugar de dos para la distribución Binomial.

Vamos a explorar estas dos distribuciones computacionalmente. Calculará la media y la desviación estándar de las muestras de una distribución de Poisson con una tasa de llegada de 10. A continuación, calculará la media y la desviación estándar de las muestras de una distribución Binomial con los parámetros n y p de tal forma que np-10.

Instrucciones
100 XP
Instrucciones
100 XP
Usando la función np.random.poisson(), extraiga 10000 muestras de una distribución de Poisson con una media de 10.
Haga una lista de los valores n y p que se deben tener en cuenta para la distribución binomial. Elija n á [20, 100, 1000] y p a [0.5, 0.1, 0.01] de modo que np siempre sea 10.
Usando np.random.binomial() dentro del bucle proporcionado, extraiga 10000 muestras de una distribución Binomial con cada par n, p e imprima la media y la desviación estándar de las muestras. Hay pares de 3 n, p: 20, 0.5, 100, 0.1 y 1000, 0.01. Se puede acceder a ellos dentro del bucle como n[i], p[i].

"""

import numpy as np

# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, size=10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
                       np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], size=10000)

    # Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
                                 np.std(samples_binomial))