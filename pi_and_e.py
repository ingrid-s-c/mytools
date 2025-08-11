import MYTOOLS

# N_PI=int(input("Número de Casas Decimais para pi:"))
# N_E=int(input("Número de Casas Decimais para e:"))

# print("Aproximação de pi com", N_PI, "casas decimais:",MYTOOLS.pi_real(N_PI))
# print("Aproximação de e com", N_E, "casas decimais:", MYTOOLS.e_real(N_E))

import time

N = 1
start_time = time.perf_counter()
for i in range(N):
    MYTOOLS.pi_real(i % 100)
end_time = time.perf_counter()
print(end_time - start_time)


start_time = time.perf_counter()
for i in range(N):
    MYTOOLS.pi_real_com_divisao(i % 100)
end_time = time.perf_counter()
print(end_time - start_time)