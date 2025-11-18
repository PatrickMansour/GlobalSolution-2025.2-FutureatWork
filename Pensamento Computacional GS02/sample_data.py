from models import Career


# Lista de carreiras focadas no futuro com competências requeridas
# Níveis de competência: escala de 0 a 5.
CAREERS = [
    Career(
        "Cientista de Dados",
        req_tech={"Python": 4, "Estatística": 4, "Aprendizado de Máquina": 4, "SQL": 3},
        req_beh={"Pensamento Analítico": 4, "Curiosidade": 4, "Comunicação": 3},
        description="Analisar dados para extrair insights e construir modelos preditivos.",
    ),
    Career(
        "Engenheiro(a) de IA",
        req_tech={"Python": 4, "Aprendizado de Máquina": 5, "Aprendizado Profundo": 4, "Computação em Nuvem": 3},
        req_beh={"Resolução de Problemas": 4, "Adaptabilidade": 4, "Trabalho em Equipe": 3},
        description="Desenvolver e implantar modelos de IA em escala.",
    ),
    Career(
        "Designer de Produto",
        req_tech={"Ferramentas de Design": 4, "Prototipagem": 3},
        req_beh={"Criatividade": 5, "Empatia": 4, "Colaboração": 4},
        description="Projetar experiências de usuário e interfaces de produto.",
    ),
    Career(
        "Analista de Cibersegurança",
        req_tech={"Redes": 4, "Princípios de Segurança": 4, "Python": 2},
        req_beh={"Atenção aos Detalhes": 5, "Resiliência": 4},
        description="Proteger sistemas e analisar incidentes de segurança.",
    ),
    Career(
        "Engenheiro(a) de Automação",
        req_tech={"Python": 3, "Scripting": 4, "Robótica": 3, "CI/CD": 3},
        req_beh={"Raciocínio Lógico": 4, "Colaboração": 3},
        description="Construir pipelines de automação e fluxos de trabalho inteligentes.",
    ),
]
