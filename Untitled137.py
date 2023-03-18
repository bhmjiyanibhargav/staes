#!/usr/bin/env python
# coding: utf-8

# # question 01
Q1. Write a Python function that takes in two arrays of data and calculates the F-value for a variance ratio
test. The function should return the F-value and the corresponding p-value for the test.
# In[1]:


import numpy as np
from scipy.stats import f_oneway

def variance_ratio_test(data1, data2):
    f_value, p_value = f_oneway(data1, data2)
    return f_value, p_value
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([6, 7, 8, 9, 10])

f_value, p_value = variance_ratio_test(data1, data2)
print("F-value:", f_value)
print("p-value:", p_value)


# # question 02 
Given a significance level of 0.05 and the degrees of freedom for the numerator and denominator of an
F-distribution, write a Python function that returns the critical F-value for a two-tailed test.
# In[2]:


from scipy.stats import f

def get_critical_f(alpha, dfn, dfd):
    return f.ppf(1 - alpha / 2, dfn, dfd)
critical_f = get_critical_f(0.05, 10, 20)
print(critical_f)


# # question 03
Q3. Write a Python program that generates random samples from two normal distributions with known

variances and uses an F-test to determine if the variances are equal. The program should output the F-
value, degrees of freedom, and p-value for the test.
# In[3]:


import numpy as np
from scipy.stats import f

# Set the seed for reproducibility
np.random.seed(42)

# Generate random samples from two normal distributions with known variances
sample1 = np.random.normal(loc=0, scale=1, size=50)
sample2 = np.random.normal(loc=0, scale=1.5, size=50)

# Calculate the F-statistic and p-value using an F-test
f_statistic, p_value = f.test(sample1, sample2)

# Calculate the degrees of freedom for the numerator and denominator
dfn = len(sample1) - 1
dfd = len(sample2) - 1

# Print the results
print("F-value:", f_statistic)
print("Degrees of freedom (numerator, denominator):", dfn, ",", dfd)
print("p-value:", p_value)


# # question 04
Q4.The variances of two populations are known to be 10 and 15. A sample of 12 observations is taken from
each population. Conduct an F-test at the 5% significance level to determine if the variances are
significantly different.
# In[4]:


from scipy.stats import f

# Define the sample sizes and known variances
n1 = n2 = 12
var1 = 10
var2 = 15

# Calculate the F-statistic and p-value using an F-test
f_statistic = var1/var2
p_value = f.cdf(f_statistic, n1-1, n2-1)

# Compare the p-value to the significance level to determine significance
alpha = 0.05
if p_value < alpha:
    print("The variances are significantly different.")
else:
    print("The variances are not significantly different.")

# Print the F-value, degrees of freedom, and p-value
print("F-value:", f_statistic)
print("Degrees of freedom (numerator, denominator):", n1-1, ",", n2-1)
print("p-value:", p_value)


# # question 05
A manufacturer claims that the variance of the diameter of a certain product is 0.005. A sample of 25
products is taken, and the sample variance is found to be 0.006. Conduct an F-test at the 1% significance
level to determine if the claim is justified.
# In[5]:


from scipy.stats import f

# Define the sample size, sample variance, and claimed population variance
n = 25
s2 = 0.006
sigma2 = 0.005

# Calculate the F-statistic and p-value using an F-test
f_statistic = s2/sigma2
p_value = f.cdf(f_statistic, n-1, n-1)

# Compare the p-value to the significance level to determine significance
alpha = 0.01
if p_value < alpha:
    print("The claim is not justified.")
else:
    print("The claim is justified.")

# Print the F-value, degrees of freedom, and p-value
print("F-value:", f_statistic)
print("Degrees of freedom (numerator, denominator):", n-1, ",", n-1)
print("p-value:", p_value)


# # question 06
Q6. Write a Python function that takes in the degrees of freedom for the numerator and denominator of an
F-distribution and calculates the mean and variance of the distribution. The function should return the
mean and variance as a tuple.
# In[6]:


def f_dist_mean_var(df1, df2):
    """
    Calculates the mean and variance of an F-distribution with degrees of freedom
    df1 for the numerator and df2 for the denominator.
    """
    mean = df2 / (df2 - 2)
    variance = (2 * df2**2 * (df1 + df2 - 2)) / (df1 * (df2 - 2)**2 * (df2 - 4))
    return (mean, variance)


# # question 07
Q7. A random sample of 10 measurements is taken from a normal population with unknown variance. The
sample variance is found to be 25. Another random sample of 15 measurements is taken from another
normal population with unknown variance, and the sample variance is found to be 20. Conduct an F-test
at the 10% significance level to determine if the variances are significantly different.
# In[7]:


from scipy.stats import f

# Define the sample sizes, sample variances, and degrees of freedom
n1 = 10
n2 = 15
s1 = 25
s2 = 20
df1 = n1 - 1
df2 = n2 - 1

# Calculate the F-statistic and p-value using an F-test
f_statistic = s1/s2
p_value = f.cdf(f_statistic, df1, df2)

# Compare the p-value to the significance level to determine significance
alpha = 0.10
if p_value < alpha/2 or p_value > 1 - alpha/2:
    print("The variances are significantly different.")
else:
    print("The variances are not significantly different.")

# Print the F-value, degrees of freedom, and p-value
print("F-value:", f_statistic)
print("Degrees of freedom (numerator, denominator):", df1, ",", df2)
print("p-value:", p_value)


# # question 08
The following data represent the waiting times in minutes at two different restaurants on a Saturday
night: Restaurant A: 24, 25, 28, 23, 22, 20, 27; Restaurant B: 31, 33, 35, 30, 32, 36. Conduct an F-test at the 5%
significance level to determine if the variances are significantly different.
# In[8]:


from scipy.stats import f

# Define the two samples
sample_A = [24, 25, 28, 23, 22, 20, 27]
sample_B = [31, 33, 35, 30, 32, 36]

# Calculate the sample variances and degrees of freedom
var_A = sum([(x - sum(sample_A) / len(sample_A))**2 for x in sample_A]) / (len(sample_A) - 1)
var_B = sum([(x - sum(sample_B) / len(sample_B))**2 for x in sample_B]) / (len(sample_B) - 1)
df1 = len(sample_A) - 1
df2 = len(sample_B) - 1

# Calculate the F-statistic and p-value using an F-test
f_statistic = var_A / var_B
p_value = f.cdf(f_statistic, df1, df2)

# Compare the p-value to the significance level to determine significance
alpha = 0.05
if p_value < alpha/2 or p_value > 1 - alpha/2:
    print("The variances are significantly different.")
else:
    print("The variances are not significantly different.")

# Print the F-value, degrees of freedom, and p-value
print("F-value:", f_statistic)
print("Degrees of freedom (numerator, denominator):", df1, ",", df2)
print("p-value:", p_value)


# # question 09
Q9. The following data represent the test scores of two groups of students: Group A: 80, 85, 90, 92, 87, 83;
Group B: 75, 78, 82, 79, 81, 84. Conduct an F-test at the 1% significance level to determine if the variances
are significantly different.
# In[9]:


from scipy.stats import f

# Define the two samples
sample_A = [80, 85, 90, 92, 87, 83]
sample_B = [75, 78, 82, 79, 81, 84]

# Calculate the sample variances and degrees of freedom
var_A = sum([(x - sum(sample_A) / len(sample_A))**2 for x in sample_A]) / (len(sample_A) - 1)
var_B = sum([(x - sum(sample_B) / len(sample_B))**2 for x in sample_B]) / (len(sample_B) - 1)
df1 = len(sample_A) - 1
df2 = len(sample_B) - 1

# Calculate the F-statistic and p-value using an F-test
f_statistic = var_A / var_B
p_value = f.cdf(f_statistic, df1, df2)

# Compare the p-value to the significance level to determine significance
alpha = 0.01
if p_value < alpha/2 or p_value > 1 - alpha/2:
    print("The variances are significantly different.")
else:
    print("The variances are not significantly different.")

# Print the F-value, degrees of freedom, and p-value
print("F-value:", f_statistic)
print("Degrees of freedom (numerator, denominator):", df1, ",", df2)
print("p-value:", p_value)


# In[ ]:




