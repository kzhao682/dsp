[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Problem: Using the variable totalwgt_lb, investigate whether first babies
are lighter or heavier than others. Compute Cohen’s d to quantify the
difference between the groups. How does it compare to the difference in
pregnancy length?

First babies are lighter than others. Cohen's d size is 0.0887. This difference
is about 3 times larger than the difference in pregnancy length.

firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()
(7.201094430437772, 7.325855614973262)

CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
-0.088672927072602006
