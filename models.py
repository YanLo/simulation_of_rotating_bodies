#there models are described as diff equation like x' = f(x)

def oscillation(x):
    w = 1 #rad/sec
    #x[0] = x, x[1] = v      x' = v
    #x'' = -w^2 * x   <=>    v' = -w^2 * x

    return [x[1], - w**2 * x[0]]

