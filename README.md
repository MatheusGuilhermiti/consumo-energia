# ⚡ Calculadora de Consumo de Energia

Este projeto é uma calculadora simples feita em Python para estimar o consumo de energia elétrica de um aparelho durante um mês.

## 🎯 Objetivo

O programa recebe o nome do aparelho, sua potência em watts e o tempo médio de uso por dia. Depois, calcula o consumo aproximado em kWh por mês.

Também existe uma estimativa do custo, considerando o valor de **R$ 0,75 por kWh**.

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Consumo-green)

## 📐 Fórmula

O consumo mensal é calculado usando:

```text
consumo mensal = (potência × horas por dia × 30) / 1000
```

Para calcular o custo:

```text
custo = consumo mensal × 0,75
```

## ▶️ Como executar

1. Tenha o Python instalado no computador.
2. Abra a pasta do projeto no VS Code.
3. Abra o terminal.
4. Execute:

```bash
python app.py
```

5. Digite as informações solicitadas pelo programa.

## 📁 Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

## 💡 Exemplo

```text
=== Calculadora de Consumo de Energia ===

Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 500
Digite o tempo de uso diário em horas: 3

--- Resultado ---
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75 por mês
```

## 👨‍💻 Projeto

Projeto desenvolvido como atividade de iniciação em tecnologia.
