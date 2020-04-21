"""
If you have a story, you can simulate it!
Sometimes, the story describing our probability distribution does not have a named distribution to go along with it. In these cases, fear not! You can always simulate it. We'll do that in this and the next exercise.

In earlier exercises, we looked at the rare event of no-hitters in Major League Baseball. Hitting the cycle is another rare baseball event. When a batter hits the cycle, he gets all four kinds of hits, a single, double, triple, and home run, in a single game. Like no-hitters, this can be modeled as a Poisson process, so the time between hits of the cycle are also Exponentially distributed.

How long must we wait to see both a no-hitter and then a batter hit the cycle? The idea is that we have to wait some time for the no-hitter, and then after the no-hitter, we have to wait for hitting the cycle. Stated another way, what is the total waiting time for the arrival of two different Poisson processes? The total waiting time is the time waited for the no-hitter, plus the time waited for the hitting the cycle.

Now, you will write a function to sample out of the distribution described by this story.

Instructions
100 XP
Instructions
100 XP
Define a function with call signature successive_poisson(tau1, tau2, size=1) that samples the waiting time for a no-hitter and a hit of the cycle.
Draw waiting times tau1 (size number of samples) for the no-hitter out of an exponential distribution and assign to t1.
Draw waiting times tau2 (size number of samples) for hitting the cycle out of an exponential distribution and assign to t2.
The function returns the sum of the waiting times for the two events.

Si tienes una historia, ¡puedes simularla!
A veces, la historia que describe nuestra distribución de probabilidad no tiene una distribución con nombre para acompañarla. ¡En estos casos, no temas! Siempre puede simularlo. Lo haremos en este y en el próximo ejercicio.

En ejercicios anteriores, examinamos el raro evento de los no-hitters en las Grandes Ligas de Béisbol. Golpear el ciclo es otro evento de béisbol raro. Cuando un bateador batea batea el ciclo, obtiene los cuatro tipos de hits, un sencillo, doble, triple y jonrón, en un solo juego. Al igual que los no-hitters, Esto puede ser modelado como un proceso de Poisson, por lo que el tiempo entre los golpes del ciclo también se distribuyen exponencialmente.

¿Cuánto tiempo debemos esperar para ver a un no-hitter y luego un bateador golpeó el ciclo? La idea es que tenemos que esperar algún tiempo para el no-hitter, y luego después del no-hitter, tenemos que esperar para alcanzar el ciclo. Dicho de otra manera, ¿cuál es el tiempo total de espera para la llegada de dos procesos diferentes de Poisson? El tiempo total de espera es el tiempo esperado para el no-hitter, más el tiempo esperado para el golpeo del ciclo.

Ahora, escribirá una función para muestrear fuera de la distribución descrita en esta historia.

Instrucciones
100 XP
Instrucciones
100 XP
Defina una función con la firma de llamada successive_poisson(tau1, tau2, size-1) que muestree el tiempo de espera para un no-hitter y un hit del ciclo.
Dibuje los tiempos de espera tau1 (número de tamaño de muestras) para el no-hitter fuera de una distribución exponencial y asígnelos a t1.
Dibuje los tiempos de espera tau2 (número de tamaño de muestras) para golpear el ciclo de una distribución exponencial y asignar a t2.
La función devuelve la suma de los tiempos de espera para los dos eventos.
"""

def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(np.mean(tau1), size= size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(np.mean(tau2), size= size)

    return t1 + t2