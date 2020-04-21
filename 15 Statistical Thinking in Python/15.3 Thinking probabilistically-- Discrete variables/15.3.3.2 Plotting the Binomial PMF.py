"""
Trazado del PMF Binomial
Como se menciona en el video, trazar un PMF de aspecto agradable requiere un poco 
de trucos matplotlib que no vamos a entrar aquí. 
En su lugar, trazaremos el PMF de la distribución Binomial como un histograma 
con habilidades que ya ha aprendido.
 El truco es configurar los bordes de las bandejas para pasar a plt.hist()
  a través del argumento de palabra clave bins.
   Queremos las papeleras centradas en los enteros.
    Por lo tanto, los bordes de las bandejas deben ser -0.5, 0.5, 1.5, 2.5, ... 
    hasta max(n_defaults) + 1.5. 
    Puede generar una matriz como esta utilizando np.arange()
     y luego restando 0.5 de la matriz.

Ya ha muestreado fuera de la distribución de Binomial durante sus ejercicios sobre los valores
predeterminados de préstamo, y las muestras resultantes se encuentran en la matriz NumPy
 n_defaults.

Instructions
100 XP
Instructions
100 XP
Using np.arange(), compute the bin edges such that the bins are centered on the integers. Store the resulting array in the variable bins.
Use plt.hist() to plot the histogram of n_defaults with the normed=True and bins=bins keyword arguments.
Show the plot.

"""

# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, normed=True, bins=bins)

# Label axes
plt.xlabel('number of defaults out of 100 loans')
plt.ylabel('PMF')

# Show the plot
plt.show()