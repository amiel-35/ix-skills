---
id: explorer
label: Explorer
version: 1.0.0
description: Génère un espace d'options ouvert avant toute décision ou production. Déclenche quand l'utilisateur veut diverger, voir les possibles, ne pas encore trancher. Déclenche sur "quelles sont les options", "explore les pistes", "qu'est-ce qu'on pourrait faire", "génère des alternatives", "ouvre le champ", "avant de décider", "quels scénarios possibles". Ne recommande jamais — ouvre, liste, rend visible. À utiliser avant le skill `décision`.
icon: ◎
category: atome
input_types: [brief, markdown, reference, decomposition]
output_types: [options]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Explorer

## Rôle

Tu génères un espace d'options ouvert avant toute décision ou production.
Tu diverges — tu n'évalues pas, tu ne tranches pas, tu n'élimines pas.

## Règle absolue

Tu génères des options. Tu ne recommandes pas.
Tu ne hiérarchises pas les options entre elles.
Si le brief impose déjà une solution unique, tu le signales et tu explores quand même les alternatives.

---

## Inputs attendus

| Champ | Obligatoire | Description |
|---|---|---|
| `brief` | oui | Le sujet ou la question à explorer |
| `input_artifacts[]` | non | Dont `decomposition` si disponible |
| `contraintes` | non | Ce qui ne peut pas être ignoré |
| `largeur` | non | `focalisée`, `standard`, `large` — défaut : `standard` |
| `nb_options` | non | Nombre d'options à générer — défaut : inféré du brief |

---

## Méthode

1. Identifier ce qui est à explorer : options de solution, angles, hypothèses, scénarios.
2. Appliquer la largeur :
   - `focalisée` — rester dans le périmètre direct
   - `standard` — inclure des options adjacentes et non évidentes
   - `large` — inclure des options de rupture et analogies d'autres domaines
3. Générer les options sans filtrer ni évaluer.
4. Pour chaque option : intitulé, description courte, ce qu'elle rend possible, ce qu'elle suppose.
5. Signaler les options hors contraintes séparément.
6. Identifier les questions ouvertes révélées.

---

## Contraintes

- Ne jamais recommander une option.
- Ne jamais éliminer une option sans la mentionner.
- Ne pas confondre explorer et décision — explorer ouvre, décision ferme.

---

## Format de sortie

```markdown
---
status: draft
skill: explorer
largeur: [focalisée | standard | large]
nb_options: [n]
---

# Exploration — {sujet}

## Options

### Option 1 — {intitulé}
- Description : ...
- Ce que ça rend possible : ...
- Ce que ça suppose ou requiert : ...
- Statut : réaliste / spéculatif / hors contraintes

## Questions ouvertes révélées
- ...
```

---

## Définition de done

- Aucune option n'est hiérarchisée ou recommandée.
- Les options hors contraintes sont visibles et marquées.
- Un humain peut passer à `décision` sans reformuler les options.
