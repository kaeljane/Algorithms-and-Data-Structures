def soma_ate_N(n):  # soma de 1 até tal número
    if (n <= 1):
        return n    # condição de parada
    else:
        return (n + soma_ate_N(n-1))

print(soma_ate_N(100)) 

# soma_ate_N(5)  <-----------------------
    # 5 + soma_ate_N(4)                 15
        # 4 + soma_ate_N(3)             10
            # 3 + soma_ate_N(2)         6
                # 2 + soma_ate_N(1) --> 3
                    # 1