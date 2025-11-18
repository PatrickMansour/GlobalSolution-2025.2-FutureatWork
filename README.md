# GlobalSolution-2025.2-FutureatWork
Criamos um sistema em Python orientado a objetos que organiza e analisa perfis profissionais do futuro, simulando uma ferramenta inteligente de orientação de carreiras.
=======
# Future at Work — Orientador de Carreiras (Global Solution 2025.2)


## Integrantes

- Patrick Mohamed Mansour de Souza – RM: 562970


- Pietro Mauer Godoy – RM: 564345


- Samir Assad Gonçalves de Souza – RM: 561562



## Descrição

Este projeto implementa um sistema em Python orientado a objetos que organiza e
analisa perfis profissionais do futuro e gera recomendações de carreiras e
trilhas de aprendizagem com base em competências técnicas e comportamentais.

O código demonstra o uso de listas, tuplas e dicionários para modelagem e análise
de dados, além de classes, atributos e métodos para estruturar o sistema.

## Funcionalidades

- Cadastro de perfis com níveis de competências (0-5).
- Estruturas de dados: listas/tuplas/dicionários.
- Modelo OOP: `Profile`, `Competence`, `Career` em `models.py`.
- Recomendação: pontuação de compatibilidade em `recommendations.py`.
- CLI simples (`main.py`) para interação: criar perfis, salvar, analisar.

## Estrutura de arquivos

- `main.py` — CLI principal para cadastrar perfis e gerar recomendações.
- `models.py` — classes `Profile`, `Competence`, `Career`.
- `profiles.json` — arquivo gerado para salvar perfis criados.
- `recommendations.py` — lógica de pontuação e recomendação.
- `sample_data.py` — exemplos de carreiras com competências requeridas.
- `README.md` — README do projeto.

## Como executar

1. Tenha Python 3.8+ instalado.
2. No PowerShell, dentro da pasta do projeto, rode:

```
python -m py_compile main.py
python main.py
```

3. Use o menu para criar perfis, listar carreiras e gerar recomendações.

## Observações técnicas

- A pontuação compara o nível do perfil com o nível exigido pela carreira e
	calcula uma porcentagem de compatibilidade (técnico 60% / comportamental 40%).
- O projeto é intencionalmente simples e focado em demonstrar conceitos de OOP,
	estruturas de dados e lógica condicional.







