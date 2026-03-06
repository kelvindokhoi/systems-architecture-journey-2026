Here is the solution for Problem 3, following your notation and derivation style.

## Problem 3

### a. Is  an unbiased estimator of ?

First, we find :
\begin{align*}
E[X] &= \int_{0}^{1} x f_X(x) , dx \
&= \int_{0}^{1} x \left( \theta(x - \frac{1}{2}) + 1 \right) , dx \
&= \int_{0}^{1} (\theta x^2 - \frac{\theta}{2}x + x) , dx \
&= \left[ \frac{\theta x^3}{3} - \frac{\theta x^2}{4} + \frac{x^2}{2} \right]_0^1 \
&= \frac{\theta}{3} - \frac{\theta}{4} + \frac{1}{2} \
&= \frac{\theta}{12} + \frac{1}{2}
\end{align*}

Now, we find :
\begin{align*}
E[\hat{\Theta}_n] &= E[12\bar{X} - 6] \
&= 12E[\bar{X}] - 6 \
&= 12E[X] - 6 \
&= 12(\frac{\theta}{12} + \frac{1}{2}) - 6 \
&= \theta + 6 - 6 \
&= \theta
\end{align*}

Thus:
\begin{align*}
B[\hat{\Theta}_n] &= E[\hat{\Theta}_n] - \theta \
&= \theta - \theta \
&= 0
\end{align*}
**Thus it is unbiased.**

---

### b. Is  a consistent estimator of ?

An estimator is consistent if  and  as .

We already have . Now we check the variance:
\begin{align*}
Var(\hat{\Theta}*n) &= Var(12\bar{X} - 6) \
&= 144 Var(\bar{X}) \
&= 144 \frac{Var(X)}{n}
\end{align*}
Since  is a constant (finite for this distribution over ):
\begin{align*}
\lim*{n \to \infty} Var(\hat{\Theta}*n) &= \lim*{n \to \infty} \frac{144 Var(X)}{n} \
&= 0
\end{align*}
**Thus it is consistent.**

---

### c. Find the mean squared error (MSE) of .

Since  is unbiased, . First, we need :
\begin{align*}
E[X^2] &= \int_{0}^{1} x^2 (\theta x - \frac{\theta}{2} + 1) , dx \
&= \left[ \frac{\theta x^4}{4} - \frac{\theta x^3}{6} + \frac{x^3}{3} \right]_0^1 \
&= \frac{\theta}{4} - \frac{\theta}{6} + \frac{1}{3} = \frac{\theta}{12} + \frac{1}{3}
\end{align*}

Now find :
\begin{align*}
Var(X) &= E[X^2] - (E[X])^2 \
&= (\frac{\theta}{12} + \frac{1}{3}) - (\frac{\theta}{12} + \frac{1}{2})^2 \
&= \frac{\theta}{12} + \frac{1}{3} - (\frac{\theta^2}{144} + \frac{\theta}{12} + \frac{1}{4}) \
&= \frac{1}{12} - \frac{\theta^2}{144}
\end{align*}

Finally, the MSE:
\begin{align*}
MSE(\hat{\Theta}_n) &= 144 \frac{Var(X)}{n} \
&= \frac{144}{n} (\frac{1}{12} - \frac{\theta^2}{144}) \
&= \frac{12 - \theta^2/12 \cdot 12}{n} \text{ (simplifying)} \
&= \frac{12 - \theta^2/12}{n} \text{ or } \frac{144 - \theta^2}{12n}
\end{align*}

Would you like me to double-check the integration steps or move on to the next problem in your set?