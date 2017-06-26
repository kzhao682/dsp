[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
# Compile data for children under 18
resp = nsfg.ReadFemResp()
under = resp.numkdhh

# Create biased and unbiased pmfs
pmf = thinkstats2.Pmf(under, label='Actual')
biased_pmf = BiasPmf(pmf, label='Biased')

# Plot pmf distribution
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='Number of Children')

# Means of pmfs
print('Actual', pmf.Mean())
print('Biased', biased_pmf.Mean())
```
