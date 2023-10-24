repo_url="https://$GITHUB_KEY@github.com/dunglas/frankenphp.git"
dossier_a_cloner="docs"
dossier_destination="$PWD/content"
nav_destination="$PWD/content/nav.md"
temp_dir="$PWD/temp-documentation"

# Cloner le dépôt
git clone "$repo_url" "$temp_dir"

# Copier les fichiers nécessaires
cp -r "$temp_dir/$dossier_a_cloner" "$dossier_destination"
cp "$temp_dir/CONTRIBUTING.md" "$dossier_destination"

# Modifier CONTRIBUTING.md
mv "$dossier_destination/CONTRIBUTING.md" "$dossier_destination/contributing.md"
sed -i '' 's|\](\([^)]*\).md)|\](/\1/)|g' "$dossier_destination/contributing.md"

# Modifier README.md
cp "$temp_dir/README.md" "$dossier_destination"
sed -i '' 's|src="frankenphp.png"|src="https://raw.githubusercontent.com/dunglas/frankenphp/main/frankenphp.png"|g' "$dossier_destination/README.md"
mv "$dossier_destination/README.md" "$dossier_destination/docs/_index.md"

# Modifier les fichiers .md dans le dossier docs
for file in "$dossier_destination/docs"/*.md; do
  sed -i '' -e '1s|^|---\nlayout: docs\n---\n|' "$file"
  sed -i '' 's|\](\([^)]*\).md)|\](/docs/\1)|g' "$file"
  sed -i '' 's|/docs/CONTRIBUTING|/contributing|g' "$file"
  sed -i '' 's|/docs/docs/|/docs/|g' "$file"
done

# Extraire le contenu entre les sections "## Docs" et "##" de README.md
sed -n '/^## Docs$/,/^##/p' "$temp_dir/README.md" | sed '/^##/d' > "$nav_destination"
sed -i '' 's|\](\([^)]*\).md)|\](/\1/)|g' "$nav_destination"
sed -i '' 's|CONTRIBUTING|contributing|g' "$nav_destination"
sed -i '' 's|/docs/docs/|/docs/|g' "$nav_destination"

# Supprimer le répertoire temporaire
rm -rf "$temp_dir"