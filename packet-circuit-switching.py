from math import floor, comb

# Essa função retorna a probabilidade de termos "x" usuários ativos na rede, dado alguns parâmetros.
def probability_of_active_users(x, active_probability, connected_users):
    return ( comb(connected_users, x) * pow(active_probability, x) * pow(1 - active_probability , connected_users - x) );

# Essa função retorna a probabilidade da demanda da rede ser maior do que a capacidade do enlace.
def probability_of_demand_bigger_than_capacity(active_probability, connected_users, max_simultaneous_users):
    probability = 0
    for active_users in range(0,max_simultaneous_users+1):
        probability += probability_of_active_users(active_users, active_probability, connected_users)
    # A explicação para o cálculo ser 1 - probability está explicado nas linhas 67-73 do código.
    return (1 - probability)

def main():
    connected_users = int(input("Informe o número de usuários conectados: "))

    # Equivalente a um do-while.
    while True:
        active_probability = float(input("Informe a probabilidade de o usuário estar ativo (Ex: 0.450): "))
        if not (active_probability >= 0 and active_probability <= 1):
            print("Por favor, digite uma probabilidade válida, isto é, um valor entre 0 e 1.")
        else:
            break

    user_data_rate_requirement = float(input("Informe o requisito de taxa de dados de cada usuário enquanto ativo (em kbps): "))

    link_total_capacity = float(input("Informe a capacidade total do enlace (em kbps): "))

    # Considerando a comutação por circuito:
    # O número máximo de usuários ativos simultaneamente vai ser equivalente a  ⌊ link_total_capacity / user_data_rate_requirement ⌋

    max_simultaneous_users = floor( link_total_capacity/user_data_rate_requirement )

    print("------------------------------------------------")
    print(
        '''Considerando a comutação por circuito:
    O número máximo de usuários ativos que podem ser atendidos simultaneamente pelo enlace, levando em consideração os valores fornecidos, é de {val:.0f} usuários.
        '''.format(val=max_simultaneous_users)
    )
    print("------------------------------------------------")


    # Considerando a comutação por pacotes:
    # Seja max_simultaneous_users o número máximo de usuários ativos simultaneamente.
    # Considere max_simultaneous_users igual a m.
    # Sendo assim, a probabilidade da demanda da rede ser MAIOR do que a capacidade do enlace, é igual a P(x > m)
    # Perceba que P(x > m) = 1 - P(x <= m).
    # Perceba também que P(x <= m) = 1 - (P(x=0) + P(x=1) + P(x=2) + ... + P(x=m)).
    # Sendo assim, para calcularmos a probabilidade da demanda da rede ser MAIOR do que a capacidade do enlace, precisamos
    # apenas saber calcular a probabilidade de termos "x" usuários ativos. E assim calculamos estes valores com "x" variando de 0 até m, e obtemos nossa resposta.

    prob = probability_of_demand_bigger_than_capacity(active_probability, connected_users, max_simultaneous_users)

    print("A probabilidade da demanda da rede ser maior do que a capacidade do enlace, é de {val:.10f}.".format(val=prob))

if __name__ == "__main__":
    main()