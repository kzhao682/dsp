[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
```
rand = np.random.random(1000)
```
```
pmf = thinkstats2.Pmf(rand, label='Random')
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number', ylabel='Pmf')
```
```
cdf = thinkstats2.Cdf(rand, label='Random')
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Number', ylabel='Cdf')
```
