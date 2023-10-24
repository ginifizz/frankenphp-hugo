# -*- coding: utf-8 -*-

import os
import shutil
import re

# Variables
token = os.environ["GITHUB_KEY"]
repo_url = "https://" + token + "@github.com/dunglas/frankenphp.git"
dossier_a_cloner = "docs"
dossier_destination = os.path.abspath("content")
docs_destination = os.path.join(dossier_destination, "docs")
nav_destination = os.path.abspath("content/nav.md")
temp_dir = os.path.abspath("temp-documentation")

# Regex pour effectuer les transformations
regexLinks = r'\[([^\]]+)\]\(([^)]+)\)'

# Fonction de remplacement
def fixLinks(match):
    texte_lien = match.group(1)
    url = match.group(2)

    url = url.replace("/docs/docs", "/docs").replace("CONTRIBUTING", "contributing")

    # Vérifier si l'URL commence par "http" ou "/"
    if url.startswith("http") or url.startswith("/"):
        # Pas de changement pour les liens HTTP ou ceux commençant par "/"
        return f'[{texte_lien}]({url}/)'
    elif (url.startswith("docs/") and url.endswith(".md")) or url.endswith(".md"):
        # Ajouter "/" devant et retirer .md pour les liens "docs"
        return f'[{texte_lien}](/{url[:-3]}/)'

# supprumer le repo temporaire s'il existe
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)

# Cloner le dépôt
os.system(f"git clone {repo_url} {temp_dir}")

# Copier les fichiers nécessaires
if os.path.exists(docs_destination):
    shutil.rmtree(docs_destination)
shutil.copytree(os.path.join(temp_dir, dossier_a_cloner), os.path.join(dossier_destination, "docs"))
shutil.copy(os.path.join(temp_dir, "CONTRIBUTING.md"), dossier_destination)

# Modifier CONTRIBUTING.md
os.rename(os.path.join(dossier_destination, "CONTRIBUTING.md"), os.path.join(dossier_destination, "contributing.md"))
with open(os.path.join(dossier_destination, "contributing.md"), 'r') as file:
    content = file.read()


content = re.sub(regexLinks, fixLinks, content)    
regex_h1 = re.search(r'#\s+([^\n]+)', content)
# Vérifier si la regex a trouvé un résultat
if regex_h1 is not None:
     title = "FrankenPHP | " +regex_h1.group(1)
else:
    # Utiliser un titre par défaut ou faire quelque chose d'autre
    title = "FrankenPHP"
content = f'---\nlayout: docs\ntitle: "{title}"\n---\n{content}'
with open(os.path.join(dossier_destination, "contributing.md"), 'w') as file:
    file.write(content)


# Modifier README.md
shutil.copy(os.path.join(temp_dir, "README.md"), dossier_destination)
with open(os.path.join(dossier_destination, "README.md"), 'r') as file:
    content = file.read()
content = content.replace('src="frankenphp.png"', 'src="https://raw.githubusercontent.com/dunglas/frankenphp/main/frankenphp.png"')
with open(os.path.join(dossier_destination, "README.md"), 'w') as file:
    file.write(content)
os.rename(os.path.join(dossier_destination, "README.md"), os.path.join(dossier_destination, "docs/_index.md"))

# Modifier les fichiers .md dans le dossier docs
for filename in os.listdir(os.path.join(dossier_destination, "docs")):
    if filename.endswith(".md"):
        filepath = os.path.join(dossier_destination, "docs", filename)
        with open(filepath, 'r') as file:
            content = file.read()

        regex_h1 = re.search(r'#\s+([^\n]+)', content)
        # Vérifier si la regex a trouvé un résultat
        if regex_h1 is not None:
            title = "FrankenPHP | " +regex_h1.group(1)
        else:
            # Utiliser un titre par défaut ou faire quelque chose d'autre
            title = "FrankenPHP"
        content = f'---\nlayout: docs\ntitle: "{title}"\n---\n{content}'
        content = re.sub(regexLinks, fixLinks, content)  
        with open(filepath, 'w') as file:
            file.write(content)

# Extraire le contenu entre les sections "## Docs" et "##" de README.md
with open(os.path.join(temp_dir, "README.md"), 'r') as file:
    content = file.read()
start_index = content.find("## Docs")
end_index = content.find("##", start_index + 1)
nav_content = content[start_index:end_index].replace("##", "")
nav_content = re.sub(regexLinks, fixLinks, nav_content)  
nav_content = f'---\ndraft: true\n---\n{content}'
with open(nav_destination, 'w') as file:
    file.write(nav_content)

# Supprimer le répertoire temporaire
shutil.rmtree(temp_dir)