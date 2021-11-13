---
layout: posts
title: "Non-linear optimization with NLopt"
date: 2020-01-29
---

## Introduction
NLopt is a nonlinear optimization library


## Example
```python
import nlopt
import numpy as np
```
We wish to mimise the function
\begin{equation}
\underbrace{\text{min}}_{x\in\mathbb{R}} = \sqrt{x_2}
\end{equation}

in the interval $-0.5\le x_2\le1$, subject to the constaints

\begin{equation}
x_2 \ge 0 \quad \text{and} \quad x_2 \ge (a_ix_1 + b_i)^3,
\end{equation}

with parameters $a_1=2$, $b_1=0$ and $a_2=-1$, $b_2=1$. This is a very simple problem that could be solved as a linear optimization problem. The two constrains and the region of feasability are shown below. 

<center>
<img src="/assets/images/nlopt.png" alt="" pading="1px" style="width:600px">
</center>

First, we need to define the function that we want to minimse, here the function prototype is 'func(x, grad)'. The gradient function is only used in gradient methods (Newton-Krylov methods, for example), where the gradient is used to find the optimum. Here the 'grad' arrays stores the partial derivatives of your function with respect to $x_1$ and $x_2$

\begin{equation}
\frac{\partial}{\partial x_1}\sqrt{x_2}=0,  \quad \frac{\partial}{\partial x_2}\sqrt{x_2}=\frac{1}{2\sqrt{x_2}}.
\end{equation}

```python
def myfunc(x, grad):
    if(grad.size > 0):
        # modify in place, not used for gadient-free algorithms
        grad[0] = 0.0
        grad[1] = 0.5 / np.sqrt(x[1])
    return np.sqrt(x[1])
```

To impose the constraint, we must also define a function with prototype `constraint(x, grad)`. Here both our constraint are similar ,we will just define a single constraint function for both, and we will use 'lambda' function to change the two paramaters.

```python
def myconstraint(x, grad, a, b):
    if(grad.size > 0):
        # modify in place, not used for gadient-free algorithms
        grad[0] = 3*a*(a*x[0] + b)**2
        grad[1] = -1.0
    return (a*x[0]+b)**3 - x[1]
```

We can then start the optimization. First we need to select an algorithm and a number of parameters, in this case we use the Local (L) gradient-based (D) Method of Moving Asymptotes (MMA) for two parameters

```python
opt = nlopt.opt(nlopt.LD_MMA, 2)
```

We can then set the bounds of our two parameteres

```python
opt.set_lower_bounds([-float('inf'), 0])
```

```python
opt.set_min_objective(myfunc)
```



```python
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,2,0), 1e-8)
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,-1,1), 1e-8)
```

```python
x = opt.optimize([1.234, 5.678])
minf = opt.last_optimum_value()
```

```python
print("optimum at ", x[0], x[1])
print("minimum value = ", minf)
print("result code = ", opt.last_optimize_result())
```