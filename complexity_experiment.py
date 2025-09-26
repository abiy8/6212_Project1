import time, math
import matplotlib.pyplot as plt

def run_code(n):
    a = [1] * (n+1)
    b = [1] * (n+1)
    c = [1] * (n+1)
    Sum = 0
    for i in range(1, n+1):
        j = i
        while j < n:
            k = j
            while k < n:
                Sum += a[i]*b[j]*c[k]
                step_k = int(math.log(math.log(n))) if n > 3 else 1
                k += max(1, step_k)
            step_j = int(math.log(j+10)) if j > 1 else 1
            j += max(1, step_j)
    return Sum

# Experiment
n_values = [100, 200, 400, 800, 1600]
times = []

for n in n_values:
    start = time.time()
    run_code(n)
    end = time.time()
    times.append(end - start)

# Theoretical values (scaled for comparison)
theoretical = [(n**3)/(math.log(n)*math.log(math.log(n))) for n in n_values]

# Plot
plt.plot(n_values, times, 'o-', label="Experimental")
plt.plot(n_values, theoretical, 's--', label="Theoretical (scaled)")
plt.xlabel("n")
plt.ylabel("Time / Complexity")
plt.title("Experimental vs Theoretical Growth")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()
