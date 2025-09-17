# Controle de Consumo de Insumos

Este projeto simula o consumo diário de insumos em um laboratório e permite ao usuário consultar produtos, registrar pedidos de reposição e visualizar os consumos organizados por quantidade.

## Funcionalidades

- Simulação de consumo diário de 8 produtos aleatórios.
- Consulta interativa de produtos e registro de pedidos.
- Armazenamento dos pedidos do usuário.

## Estruturas e Algoritmos Utilizados

1. **Listas**  
   - Armazenam produtos e consumos diários.  
   - Permitem manipulação e consulta de forma simples.

2. **Fila**  
   - Registra os consumos na ordem em que ocorreram (cronológica).  
   - Mantém o histórico do dia de forma sequencial.

3. **Pilha**  
   - Armazena os consumos para consulta do mais recente para o mais antigo.  
   - Permite uma visão inversa do histórico de consumos.

4. **Busca Sequencial**  
   - Permite localizar rapidamente um produto específico na lista de consumos.  
   - Utilizada para exibir a quantidade utilizada e perguntar sobre reposição.

5. **Merge Sort**  
   - Ordena os produtos por quantidade utilizada de forma estável.  
   - Ajuda a identificar produtos com menor ou maior consumo.

6. **Quick Sort**  
   - Outra forma de ordenar os consumos por quantidade.  
   - Útil para análise rápida de estoque e reposição.

## Interatividade

- O usuário escolhe qual produto consultar.  
- Pode registrar pedidos de reposição, informando a quantidade desejada.  
- É possível consultar vários produtos em sequência.  
- No final, o sistema mostra os consumos do dia e os produtos pedidos.
