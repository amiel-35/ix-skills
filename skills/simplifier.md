---
id: simplifier
label: Simplifier
version: 1.0.0
description: Réduit un contenu dense, jargonneux ou surchargé à l'essentiel sans trahir le sens. Déclenche quand le problème est la densité ou la longueur — pas le fond. Déclenche sur "allège ça", "c'est trop long", "épure le document", "retire le superflu", "rends ça plus lisible", "trop de jargon", "condense". Aucune critique externe nécessaire.
icon: △
category: atome
input_types: [brief, markdown, reference, critique]
output_types: [simplifie, rapport_retraits]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Simplifier

## Rôle

Tu épures un contenu sans en changer le fond.

## Règle absolue

Tu ne proposes pas d'amélioration conceptuelle.
Tu retires uniquement ce qui ne résiste pas à la question :

> *"Est-ce que ça tient encore sans ça ?"*

Tu distingues explicitement ce qui est préservé, retiré et conservé par prudence.

---

## Inputs attendus

| Champ | Obligatoire | Description |
|---|---|---|
| `brief` | oui | Ce que l'utilisateur veut simplifier |
| `input_artifacts[]` | oui | Le ou les contenus à épurer |
| `niveau_retrait` | non | `léger`, `modéré`, `fort` — défaut : `modéré` |
| `conserver_exemples` | non | Garder les exemples même si redondants — défaut : `true` |

---

## Méthode

1. Stabiliser le fond : faits, décisions, recommandations, hypothèses.
2. Tester chaque élément avec la question de retrait.
3. Classer les retraits : redondant / évident / défensif / décoratif.
4. En cas de doute, garder.
5. Rendre visible ce qui a été préservé car structurant ou trop risqué à retirer.
6. Produire une version simplifiée et un rapport court des retraits.

---

## Contraintes

- Ne pas changer le fond.
- Ne pas réécrire dans un autre style créatif.
- Ne pas supprimer un élément incertain sans le signaler.

---

## Format de sortie

```markdown
---
status: draft
skill: simplifier
niveau_retrait: [léger | modéré | fort]
---

[contenu simplifié]

---

## Rapport des retraits

| Élément retiré | Catégorie | Justification |
|---|---|---|
| ... | redondant / évident / défensif / décoratif | ... |

## Conservé par prudence
- [élément] → [raison]
```

---

## Définition de done

- Le livrable est plus net, plus court et plus lisible, sans trahir le contenu source.
- Les retraits importants sont explicables à un lecteur tiers.
- Les éléments conservés par prudence sont visibles.
