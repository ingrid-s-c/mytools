import MYTOOLS

N_PI=int(input("Número de Casas Decimais para pi:"))
N_E=int(input("Número de Casas Decimais para e:"))

print("Aproximação de pi com", N_PI, "casas decimais:",MYTOOLS.pi_real(N_PI))
print("Aproximação de e com", N_E, "casas decimais:", MYTOOLS.e_real(N_E))
