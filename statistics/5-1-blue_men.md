[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>
Exercise: In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

The first step is to create a normal distribution of heights with the given parameters for men with cm as the units.
```
import scipy.stats
```
```
# Create normal distribution using scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```
The acceptable standard for male who can join the Blue Man Group is calculated by finding the difference between the CDF of 6'1'' and 5'10''.
```
low = dist.cdf(177.8)
high = dist.cdf(185.42)
criteria = high - low
low, high, criteria
# (0.48963902786483265, 0.83238586549630633, 0.34274683763147368)
```
34.3% of the U.S. male population is in the range to join Blue Man Group.
