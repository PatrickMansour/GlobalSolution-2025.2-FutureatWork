from typing import List, Tuple
from models import Profile, Career


def score_profile_vs_career(profile: Profile, career: Career) -> float:
    """Calcule uma pontuação de compatibilidade (0-100) entre um perfil e uma carreira.

Comparamos competências técnicas e comportamentais. Cada competência contribui
proporcionalmente à proximidade do nível do perfil ao nível exigido.
    """
    tech_score = 0.0
    tech_total = 0
    for name, req in career.required_technical.items():
        tech_total += 1
        prof_level = profile.technical.get(name, 0)
        if req <= 0:
            tech_score += 1.0
        else:
            tech_score += min(prof_level / req, 1.0)

    beh_score = 0.0
    beh_total = 0
    for name, req in career.required_behavioral.items():
        beh_total += 1
        prof_level = profile.behavioral.get(name, 0)
        if req <= 0:
            beh_score += 1.0
        else:
            beh_score += min(prof_level / req, 1.0)

    tech_part = (tech_score / tech_total) if tech_total > 0 else 1.0
    beh_part = (beh_score / beh_total) if beh_total > 0 else 1.0

    combined = 0.6 * tech_part + 0.4 * beh_part
    return round(combined * 100, 2)


def recommend(profile: Profile, careers: List[Career], top_n: int = 3) -> List[Tuple[Career, float]]:
    scored = []
    for c in careers:
        s = score_profile_vs_career(profile, c)
        scored.append((c, s))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]
