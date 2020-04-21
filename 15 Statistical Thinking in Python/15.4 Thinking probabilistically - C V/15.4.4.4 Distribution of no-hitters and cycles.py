"""
Distribution of no-hitters and cycles
Now, you'll use your sampling function to compute the waiting time to observe a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean waiting time for hitting the cycle is 715 games.

Instructions
100 XP
Use your successive_poisson() function to draw 100,000 out of the distribution of waiting times for observing a no-hitter and a hitting of the cycle.
Plot the PDF of the waiting times using the step histogram technique of a previous exercise. Don't forget the necessary keyword arguments. You should use bins=100, normed=True, and histtype='step'.
Label the axes.

Distribución de no-hitters y ciclos
Ahora, usará la función de muestreo para calcular el tiempo de espera para observar un no-hitter y golpear el ciclo. El tiempo medio de espera para un no-hitter es 764 juegos, y el tiempo de espera medio para golpear el ciclo es 715 juegos.

Instrucciones
100 XP
Utilice su función successive_poisson() para sacar 100.000 de la distribución de los tiempos de espera para observar un no-hitter y un golpe del ciclo.
Trazar el PDF de los tiempos de espera utilizando la técnica de histograma de pasos de un ejercicio anterior. No olvide los argumentos de palabras clave necesarios. Usted debe utilizar bins-100, normed-True, y histtype 'paso'.
Etiquete los ejes.
"""

# Draw samples of waiting times: waiting_times
waiting_times= successive_poisson(764 ,715, size=100000)

# Make the histogram
plt.hist(waiting_times, bins= 100, normed=True, histtype='step')


# Label axes
plt.xlabel(' the waiting time')
plt.ylabel('PDF')


# Show the plot

plt.show()
