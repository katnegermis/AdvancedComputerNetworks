% Advanced Computer Networks
% Exam question
% Michael Bang, mbang, 08/05-14

Multipath propagation
=======================

### 1. What is multipath propagation, and what are the causes of multipath propagation? Why is multipath propagation a problem?

Multipath propagation happens when radio waves are reflected (or diffracted or scattered) on objects in proximity to the sender and/or receiver of the radio signal. The reflected signals arrive at the receiver at a later point in time than the signal traveling in a straight line, meaning that the signals (symbols being sent) will overlap in time. This makes it difficult for the receiver to distinguish the signals correctly. This is called InterSymbol Interference (ISI).\
\
The problem of intersymbol interference (ISI) becomes greater as the time between symbols is decreased, i.e. at higher data rates. ISI therefore limits the transmission rate that can be achieved on a wireless link that has multipath propagation.

### 2. What can be done to reduce the problem of intersymbol interference (ISI)?
Instead of sending single symbols on a single frequency at a high rate, (almost) the same data rate can be achieved by sending multiple symbols _simultaneously_ on many narrower frequencies (sub-channels), at a lower rate. This is how Orthogonal Frequency Division Multiplexing (OFDM) works.

### 3. Explain how Orthogonal Frequency Division Multiplexing (OFDM) utilizes sub-channels to decrease the impact of multipath propagation, and construct a mathematical example that shows a theoretical gain from using OFDM.

As stated in question 2, OFDM sends multiple signals simultaneously, over narrower frequencies. This increases the time it takes to send a single symbol, and therefore decreases intersymbol interference, while the overall data rate is (almost) kept the same.
\
\
**Mathematical model**:\
Assuming a symbol duration of 8 $\mu$ and a delay of 2 $\mu$ between each symbol, the interference will be $\frac{2}{8} = 0.25 = 25\%$.

If we, instead, divide the symbols over 10 channels and send them simultaneously, the time to send each symbol will increase 10 times. The interference will then be $\frac{2}{8 * 10} = 0.025 = 2.5\%$.
