![](2017-10-31-19-20-59.png)

- We update everytime we pull an arm
- Posterior we have now becomes the prior of the next

![](2017-10-31-19-22-42.png)
- Compare this against traditional machine learning methods
    - train again from scratch

![](2017-10-31-19-22-27.png)

# Pvalue thresholds


![](2017-10-31-19-24-02.png)

- must store a and b somewhere

![](2017-10-31-19-24-49.png)

- mu1 and mu2 are beta distributed

## Recall definition of pvalues

![](2017-10-31-19-25-38.png)
- You can't accept the null hypothesis
    - you can only not 'reject the null hypothesis'

![](2017-10-31-19-27-03.png)

- joint pdf
    - multiplication of the two
    - since they are independent

![](2017-10-31-19-27-57.png)
- find the area under the curve where mu1 > mu2

![](2017-10-31-19-28-45.png)

- we want the area on the upper triangle

# Another option
![](2017-10-31-19-29-55.png)

- Use a loss function
    - quit when a threshold is found

# Convergence.py

- See how it converges to the best bandit

At 1000 samples

![](2017-10-31-19-36-56.png)

At 10 000 samples

![](2017-10-31-19-37-49.png)