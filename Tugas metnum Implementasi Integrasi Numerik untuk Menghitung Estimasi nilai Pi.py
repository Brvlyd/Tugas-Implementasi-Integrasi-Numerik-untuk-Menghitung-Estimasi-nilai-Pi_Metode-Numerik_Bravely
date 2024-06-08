import time
import numpy as np

def reimann_integration(N):
    dx = 1.0 / N
    total_area = 0.0
    for i in range(N):
        x = (i + 0.5) * dx
        total_area += 4.0 / (1.0 + x * x)
    pi_approx = total_area * dx
    return pi_approx

def calculate_rms_error(approx_pi, reference_pi):
    return np.sqrt((approx_pi - reference_pi) ** 2)

def main():
    reference_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]

    for N in N_values:
        start_time = time.time()
        approx_pi = reimann_integration(N)
        execution_time = time.time() - start_time
        rms_error = calculate_rms_error(approx_pi, reference_pi)

        print(f"N = {N}")
        print(f"Approximated Pi: {approx_pi}")
        print(f"RMS Error: {rms_error}")
        print(f"Execution Time: {execution_time} seconds\n")

if __name__ == "__main__":
    main()
