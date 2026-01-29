import requests
import pybadges
import os

USERNAME = "Adr43n"  # Ton username GitHub
OUTPUT_FILE = "LANGUAGES_BADGE.svg"

# Récupère tous les repos publics
repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
repos = requests.get(repos_url).json()

languages_count = {}

for repo in repos:
    lang_url = repo["languages_url"]
    langs = requests.get(lang_url).json()
    for lang in langs:
        languages_count[lang] = languages_count.get(lang, 0) + langs[lang]

# Trie les langages par taille (optionnel)
sorted_langs = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)

# Crée une chaîne avec tous les langages
langs_string = ", ".join([lang for lang, _ in sorted_langs])

# Génère le badge SVG
badge_svg = pybadges.badge(left_text="Languages", right_text=langs_string, right_color="blue")

# Sauvegarde
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(badge_svg)

print(f"Badge généré : {OUTPUT_FILE}")
