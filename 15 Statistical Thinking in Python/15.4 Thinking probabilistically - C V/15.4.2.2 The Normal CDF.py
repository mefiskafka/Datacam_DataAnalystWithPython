"""

The Normal CDF
Now that you have a feel for how the Normal PDF looks, let's consider its CDF. Using the samples you generated in the last exercise (in your namespace as samples_std1, samples_std3, and samples_std10), generate and plot the CDFs.

Instructions
100 XP
Use your ecdf() function to generate x and y values for CDFs: x_std1, y_std1, x_std3, y_std3 and x_std10, y_std10, respectively.
Plot all three CDFs as dots (do not forget the marker and linestyle keyword arguments!).
Hit submit to make a legend, showing which standard deviations you used, and to show your plot. There is no need to label the axes because we have not defined what is being described by the Normal distribution; we are just looking at shapes of CDFs.
--------------------------------------------------------------------------------------

El CDF normal
Ahora que tiene una idea de cómo se ve el PDF normal, consideremos su CDF. Con los ejemplos generados en el último ejercicio (en el espacio de nombres como samples_std1, samples_std3 y samples_std10), genere y trace los CDF.

Instrucciones
100 XP
Utilice la función ecdf() para generar valores x e y para CDF: x_std1, y_std1, x_std3, y_std3 y x_std10, y_std10, respectivamente.
Trazar los tres CDF como puntos (¡no olvide los argumentos de palabra clave de marcador y estilo de línea!).
Pulse Enviar para crear una leyenda, mostrando qué desviaciones estándar ha utilizado y para mostrar la gráfica. No hay necesidad de etiquetar los ejes porque no hemos definido lo que se describe en la distribución Normal; sólo estamos mirando formas de CDFs.

"""

import numpy as np
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return (x, y)


samples_std1=  np.random.normal(20,1,size= 100000)
samples_std3=  np.random.normal(20,3,size= 100000)
samples_std10= np.random.normal(20,10,size= 100000)

# Generate CDFs

x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker=".", linestyle="none")
_ = plt.plot(x_std3, y_std3, marker=".", linestyle="none")
_ = plt.plot(x_std10, y_std10, marker=".", linestyle="none")

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()