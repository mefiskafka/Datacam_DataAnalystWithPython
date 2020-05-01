"""

How is this parameter optimal?
Now sample out of an exponential distribution with τ being twice as large as the optimal τ. Do it again for τ half as large. Make CDFs of these samples and overlay them with your data. You can see that they do not reproduce the data as well. Thus, the τ you computed from the mean inter-no-hitter times is optimal in that it best reproduces the data.

Note: In this and all subsequent exercises, the random number generator is pre-seeded for you to save you some typing.

Instructions
0 XP
Instructions
0 XP
Take 10000 samples out of an Exponential distribution with parameter τ1/2 = tau/2.
Take 10000 samples out of an Exponential distribution with parameter τ2 = 2*tau.
Generate CDFs from these two sets of samples using your ecdf() function.
Add these two CDFs as lines to your plot. This has been done for you, so hit 'Submit Answer' to view the plot!

"""

# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2, 10000)
