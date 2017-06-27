[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 3.1 Something like the class size paradox appears if you survey
children and ask how many children are in their family. Families with many
children are more likely to appear in your sample, and families with no chil-
dren have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribu-
tion for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children
and asked them how many children under 18 (including themselves) are in
their household.
Plot the actual and biased distributions, and compute their means.

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
```
![Image of distributions](dsp/img/stats3_1.png)

```
# Means of pmfs
print('Actual', pmf.Mean())
print('Biased', biased_pmf.Mean())
```
