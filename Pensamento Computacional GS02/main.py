import json
import os
from models import Profile
from sample_data import CAREERS
from recommendations import recommend


TECH_COMPETENCES = (
    "Python",
    "SQL",
    "Aprendizado de Máquina",
    "Estatística",
    "Computação em Nuvem",
    "Scripting",
    "Ferramentas de Design",
)

BEH_COMPETENCES = (
    "Pensamento Analítico",
    "Criatividade",
    "Colaboração",
    "Adaptabilidade",
    "Comunicação",
    "Curiosidade",
    "Atenção aos Detalhes",
)

PROFILES_FILE = "profiles.json"


def load_profiles():
    try:
        with open(PROFILES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Profile.from_dict(d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Aviso: arquivo 'profiles.json' vazio ou corrompido. Nenhum perfil carregado.")
        return []


def save_profiles(profiles):
    tmp = PROFILES_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in profiles], f, ensure_ascii=False, indent=2)
    os.replace(tmp, PROFILES_FILE)


def create_profile_interactive():
    name = input("Nome do perfil: ").strip()
    p = Profile(name)
    print("\n--- Preencha competências técnicas (0-5) ---")
    for c in TECH_COMPETENCES:
        while True:
            try:
                v = input(f"{c} (0-5): ").strip()
                if v == "":
                    v = "0"
                lvl = int(v)
                p.set_technical(c, lvl)
                break
            except ValueError:
                print("Digite um número inteiro entre 0 e 5.")
    print("\n--- Preencha competências comportamentais (0-5) ---")
    for c in BEH_COMPETENCES:
        while True:
            try:
                v = input(f"{c} (0-5): ").strip()
                if v == "":
                    v = "0"
                lvl = int(v)
                p.set_behavioral(c, lvl)
                break
            except ValueError:
                print("Digite um número inteiro entre 0 e 5.")
    return p


def list_careers():
    print("\n--- Carreiras disponíveis ---")
    for i, c in enumerate(CAREERS, start=1):
        print(f"{i}. {c.name} - {c.description}")


def analyze_profile(profiles):
    if not profiles:
        print("Nenhum perfil cadastrado. Crie um perfil primeiro.")
        return
    print("\nSelecione um perfil para analisar:")
    for i, p in enumerate(profiles, start=1):
        print(f"{i}. {p.name}")
    try:
        sel = int(input("Escolha número: ")) - 1
        profile = profiles[sel]
    except Exception:
        print("Seleção inválida.")
        return
    print(f"\nAnalisando perfil: {profile.name}")
    recs = recommend(profile, CAREERS, top_n=3)
    print("\n--- Recomendações ---")
    for career, score in recs:
        print(f"{career.name}: {score}% de compatibilidade - {career.description}")
    print("\nSugestões de aprimoramento:")

    top_career = recs[0][0]
    missing = []
    for k, req in top_career.required_technical.items():
        prof_lvl = profile.technical.get(k, 0)
        if prof_lvl < req:
            missing.append(f"Aprimorar técnico: {k} (tem {prof_lvl}, recomendado {req})")
    for k, req in top_career.required_behavioral.items():
        prof_lvl = profile.behavioral.get(k, 0)
        if prof_lvl < req:
            missing.append(f"Aprimorar comport.: {k} (tem {prof_lvl}, recomendado {req})")
    if missing:
        for m in missing[:5]:
            print("- ", m)
    else:
        print("Perfil já bem alinhado com a carreira principal sugerida!")


def main_loop():
    profiles = load_profiles()
    while True:
        print("\n=== Future at Work - Orientador de Carreiras ===")
        print("1. Criar novo perfil")
        print("2. Listar perfis salvos")
        print("3. Listar carreiras disponíveis")
        print("4. Analisar perfil e gerar recomendações")
        print("5. Salvar perfis")
        print("0. Sair")
        choice = input("Escolha: ").strip()
        if choice == "1":
            p = create_profile_interactive()
            profiles.append(p)
            print(f"Perfil '{p.name}' criado.")
        elif choice == "2":
                
                profiles = load_profiles()
                if not profiles:
                    print("Nenhum perfil salvo.")
                else:
                    for i, p in enumerate(profiles, start=1):
                        print(f"{i}. {p.name}")
        elif choice == "3":
            list_careers()
        elif choice == "4":
            analyze_profile(profiles)
        elif choice == "5":
            save_profiles(profiles)
            print("Perfis salvos em 'profiles.json'.")
        elif choice == "0":
            print("Encerrando. Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main_loop()
