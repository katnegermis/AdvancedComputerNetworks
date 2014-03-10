% Advanced Computer Networks
% Assignment 2: Wireless Networks: Fundamentals
% March 13th 2014

Question 1
============
a)
----
The path loss (path attenuation) model is a mathematical model for predicting electro magnetic wave propagation.
The formula is as follows:
\begin{align*}
        loss = \frac{P_t}{P_r} = (\frac{4\cdot \pi d}{\lambda})^a
\end{align*}
where $P_t$ is transmitted power, $P_r$ is received power, $d$ is distance, $\lambda$ is wavelength, and $a$ is the path loss exponent. The path loss exponent has been emperically measured for different environments, and, for instance, is 2 in a vacuum[^1].

The path loss is often given in dB, which has the formula: 
\begin{align*}
    loss (dB) = 10log(\frac{P_t}{P_r}) = 10a\cdot log(\frac{4\cdot \pi d}{\lambda})
\end{align*}

b)
----
The log-normal shadowing model takes, by very simple means, account for ''random'' effects such as shadowing, refraction, reflection, scattering, and diffraction. The model takes these effects in to account by adding a gaussian random variable with zero mean and standard deviation $\sigma$ typically in the range $[2; 8]$. The formula then becomes:

\begin{align*}
    loss (dB) = 10log(\frac{P_t}{P_r}) = 10a\cdot log(\frac{4\cdot \pi d}{\lambda}) + X[dB]
\end{align*}

c)
----
Theoretically, the Signal to Interference + Noise Ratio (SINR) should be a good estimator for whether a signal can be decoded or not, but empirical data (such as from the MIT roofnet) shows that this is in fact not the case.

d)
----
The log-normal shadowing model does not very accurately predict what we will measure in real life because it is just a random variable and therefore doesn't take the actual environment in to account.

Question 2
============
The spread spectrum technique is a way to deliberately spread signals with a particular bandwidth over a wider band, resulting in a signal with a wider bandwidth[^2]. This allows the receiver to despread the signal and recover the original signal while removing both broad- and narrowband interference.

One of the main benefits of using a spread spectrum system is that it is resistant to narrow band interference. DSSS is resistant to multiple-path propagation, and is somewhat more secure (if the chipping sequence is kept secret.)

Question 3
============

Question 4
============
a)
----

b)
----

c)
----

Question 5
============
a)
----

b)
----

c)
----


[^1]: http://en.wikipedia.org/wiki/Log-distance_path_loss_model#Empirical_coefficient_values_for_indoor_propagation
[^2]: http://en.wikipedia.org/wiki/Spread_spectrum