# %%
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


# %%
AND(1, 0)
# %%
import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
w*x
# %%
np.sum(w*x)
# %%
np.sum(x*w) 
# %%
b
# %%
0.5 -0.7
# %%
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b =-0.7
    tmp = np.sum(w*x) +b
    if tmp <=0:
        return 0
    else:
        return 1
# %%
AND(3,3)
# %%
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) +b
    if(tmp <=0):
        return 0
    else:
        return 1

# %%
NAND(1,0)
# %%
def OR(x1,x2):
    x = np.array([x1,x2])
    w =np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w) +b
    if tmp<= 0:
        return 0
    else:
        return 1
    

# %%
