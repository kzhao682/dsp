# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python list and tuples are both sequence of values that can be any type and indexed by integers. The primary difference is tuples are immutable, so in order to modify a tuple, it must replaced with another tuple.
```
Example:
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> t[0] = 'A' #returns an error because tuples are immutable
>>> t = ('A',) + t[1:] #replace tuple with another tuple
>>> t
('A', 'b', 'c', 'd', 'e')
```
>> Since dictionaries are implemented using a hashtable, the keys must be hashable. For this reason, tuples but not lists work as keys in 
dictionaries.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both Python lists and sets are used to store values, but are used in different cases. Lists keep the order in which the values are entered, but sets automatically arrange the values. Sets require the items to be hashable, but lists can have non-hashable items. Sets are much more efficient in finding an element since it orders all the values and eliminates duplicates.
```
#example of sets to show class test scores
>>> my_scores = {88, 64, 84, 88, 86, 92, 84, 84}
>>> print(my_scores)
{64, 84, 86, 88, 92}

#example of lists to show average temperature during the week
>>> my_temperature = [76, 70, 72, 72, 74, 76, 74]
>>> print(my_temperature)
[76, 70, 72, 72, 74, 76, 74]
```

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





