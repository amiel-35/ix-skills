# Cas de test des skills

Un fichier par skill : des demandes réalistes, ce que doit contenir une bonne sortie (critères écrits avant de lire les sorties), et les résultats des passages. Les sorties gardées comme exemples sont dans `sorties/<id>/`.

Même format et même méthode que `tests/cas-skills/` d'ix-recipes, dont le banc (`banc.py`) peut jouer ces fichiers. Un cas se joue avec le skill seul, depuis `dist/skills/<id>/` (avec ses `references/`), sans le cache du plugin :

```bash
claude -p --model sonnet --system-prompt-file dist/skills/<id>/SKILL.md --tools Read --strict-mcp-config --setting-sources "" --disable-slash-commands < demande.txt
```

lancé depuis un dossier qui contient `references/` et les pièces du cas. Ces fichiers ne sont lus ni par `build.py` ni par les tests Python.
