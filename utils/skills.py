def calculate_iq(correct):
    if correct <= 5:
        return correct, "Juda past"
    elif correct <= 8:
        return correct, "O‘rtacha"
    elif correct <= 11:
        return correct, "Yaxshi"
    elif correct <= 13:
        return correct, "A'lo"
    else:
        return correct, "Daho"


def detect_skills(category_scores):
    result = []

    if category_scores["mantiq"] >= 7:
        result.append("🧠 Mantiqiy fikrlash kuchli")
    elif category_scores["mantiq"] <= 3:
        result.append("🧠 Mantiq pastroq")

    if category_scores["davlat"] >= 7:
        result.append("🌍 Geografik bilim kuchli")
    elif category_scores["davlat"] <= 3:
        result.append("🌍 Geografiya sust")

    if category_scores["tarix"] >= 7:
        result.append("🏺 Tarix bo‘yicha bilim yaxshi")
    elif category_scores["tarix"] <= 3:
        result.append("🏺 Tarix bo‘yicha ojizroq")

    if category_scores["game"] >= 7:
        result.append("🎮 O‘yinlar bo‘yicha kuchli")
    elif category_scores["game"] <= 3:
        result.append("🎮 Gaming bo‘yicha sust")

    if not result:
        result = ["⚡ O'rtacha umumiy qobiliyat"]

    return "\n".join(result)
