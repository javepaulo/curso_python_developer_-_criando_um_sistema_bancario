# Desafio: Criando um Sistema Bancário

Desafio proposto no módulo ***Sintaxe Básica com Python*** na plataforma **[DIO](https://www.dio.me/)** referente ao curso **[Suzano - Python Developer](https://web.dio.me/track/823e5de7-79a5-44fe-a472-cfe6bb0fec00).**


## 📑 Proposta do desafio:
Criar uma primeira versão do sistema onde serão implementadas apenas 3 operações, sendo elas: depósito, saque e extrato.

## 📌 Regras:
#### 📥 Depósito: 
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

#### 📤 Saque:
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#### 🧾 Extrato:
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
