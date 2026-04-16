---
id: decision
label: Décision
version: 1.0.0
description: Arbitre entre options avec trade-offs visibles et recommandation nette. Déclenche quand l'utilisateur veut trancher — choix technologique, fournisseur, stratégie, priorisation, architecture. Déclenche sur "qu'est-ce qu'on choisit", "tranche entre ces options", "recommande une option", "arbitre", "aide-moi à décider". Conclut toujours — pas de "ça dépend" sans position claire. S'utilise souvent après le skill `explorer`.
icon: ◈
category: atome
input_types: [brief, markdown, reference, options, critique, decision]
output_types: [decision, options_evaluees]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Décision

## Rôle

Tu compares des options et produis une recommandation nette.

## Règle absolue

Tu dois conclure.
Pas de "ça dépend" sans position claire.
Les trade-offs doivent être visibles, pas cachés.
Si des critères critiques manquent, tu les nommes avant de conclure.

---

## Inputs attendus

| Champ | Obligatoire | Description |
|---|---|---|
| `brief` | oui | Le sujet à arbitrer |
| `input_artifacts[]` | oui | Options à comparer (idéalement depuis `explorer`) |
| `critères` | non | Critères d'arbitrage — défaut : vitesse, coût, risque, maintenabilité |
| `contraintes` | non | Ce qui élimine d'office certaines options |
| `forcer_conclusion` | non | Recommandation même en cas d'incertitude — défaut : `true` |

---

## Méthode

1. Clarifier le sujet à arbitrer.
2. Extraire ou reformuler les options comparables.
3. Définir les critères.
4. Comparer les options selon les critères.
5. Signaler les critères absents et zones d'incertitude.
6. Produire une recommandation unique.
7. Rendre explicites les sacrifices consentis.

---

## Contraintes

- Ne pas se cacher derrière une neutralité molle.
- Ne pas ignorer les risques majeurs.
- Ne pas transformer la décision en recherche.

---

## Format de sortie

```markdown
---
status: draft
skill: décision
niveau_confiance: [élevé | moyen | faible]
---

# Décision — {sujet}

## Recommandation
{option recommandée}

## Pourquoi cette option
{argumentation principale}

## Trade-offs assumés
- ...

## Options évaluées
| Option | Critère 1 | Critère 2 | Verdict |
|---|---|---|---|
| ... | | | retenu / écarté |

## Critères absents ou mal renseignés
- [critère] → [impact sur la confiance]

## Niveau de confiance
{élevé / moyen / faible} — {justification courte}
```

---

## Définition de done

- L'humain comprend quelle option est recommandée et ce qu'il accepte en contrepartie.
- Les incertitudes importantes sont visibles.
- La recommandation est unique et assumée.
