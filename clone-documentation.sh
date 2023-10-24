repo_url="git@github.com:dunglas/frankenphp.git"
dossier_a_cloner="docs"
dossier_destination="$PWD/content"
nav_destination="$PWD/content/nav.md"
temp_dir="$PWD/temp-documentation"

git clone https://$GITHUB_KEY@github.com/dunglas/frankenphp.git $temp_dir
cp -r $temp_dir/$dossier_a_cloner $dossier_destination

cp "$temp_dir/CONTRIBUTING.md" $dossier_destination
  echo -e "---\nlayout: docs\n---\n$(cat $dossier_destination/CONTRIBUTING.md)" > "$dossier_destination/CONTRIBUTING.md"
mv $dossier_destination/CONTRIBUTING.md $dossier_destination/contributing.md
sed -i  '' 's|\](\([^)]*\).md)|\](/\1/)|g' $dossier_destination/contributing.md

cp "$temp_dir/README.md" $dossier_destination
sed -i '' 's|src="frankenphp.png"|src="https://raw.githubusercontent.com/dunglas/frankenphp/main/frankenphp.png"|g' $dossier_destination/README.md
mv $dossier_destination/README.md $dossier_destination/docs/_index.md

for file in $dossier_destination/docs/*.md; do
  echo -e "---\nlayout: docs\n---\n$(cat $file)" > $file
sed -i  '' 's|\](\([^)]*\).md)|\](/docs/\1)|g' $file
sed -i '' 's|/docs/CONTRIBUTING|/contributing|g' $file
sed -i '' 's|/docs/docs/|/docs/|g' $file
done

sed -n '/^## Docs$/,/^##/p' "$temp_dir/README.md" | sed '/^##/d' > $nav_destination
sed -i  '' 's|\](\([^)]*\).md)|\](/\1/)|g' $nav_destination
sed -i '' 's|CONTRIBUTING|contributing|g' $nav_destination
sed -i '' 's|/docs/docs/|/docs/|g' $nav_destination
rm -rf $temp_dir

