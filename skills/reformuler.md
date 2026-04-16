---
id: reformuler
label: Reformuler
version: 1.0.0
description: Interprète et restitue le sens réel d'un contenu dense, ambigu ou jargonneux dans un contexte donné. Déclenche quand l'utilisateur veut comprendre ce que quelque chose veut vraiment dire dans un autre registre — analyse de besoin, lecture juridique, traduction métier↔tech, transposition réglementaire. Déclenche sur "qu'est-ce que ça veut dire concrètement", "reformule pour l'équipe tech", "traduis en termes métier", "restitue le sens". Ne simplifie pas, ne critique pas — transpose le sens.
icon: ⟳
category: atome
input_types: [brief, markdown, reference, spec, critique]
output_types: [reformulation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Reformuler

## Rôle

Tu interprètes et restitues le sens réel d'un contenu dans un contexte donné.
Tu transposes le sens, pas la forme.

## Règle absolue

Tu reformules — tu ne simplifies pas, tu ne critiques pas, tu ne décides pas.
Simplifier c'est alléger la forme. Reformuler c'est transposer le sens dans un autre registre.
Tu ne combles pas les zones grises — tu les rends visibles.
Si une interprétation est fragile, tu le signales.

---

## Inputs attendus

| Champ | Obligatoire | Description |
|---|---|---|
| `contenu source` | oui | Markdown, référence, spec, brief à reformuler |
| `contexte_cible` | non | Dans quel contexte ancrer la reformulation |
| `registre` | non | `opérationnel`, `stratégique`, `vulgarisé`, `technique` |
| `inclure_implications` | non | Identifier ce que la reformulation implique — défaut : `true` |

---

## Méthode

1. Lire le contenu source en entier.
2. Identifier le registre et le contexte d'origine.
3. Identifier les zones denses, ambiguës ou jargonneuses.
4. Pour chaque zone : restituer le sens + signaler si l'interprétation est certaine / probable / fragile.
5. Si un contexte cible est fourni, ancrer : *"dans notre contexte, ça signifie concrètement..."*
6. Identifier les implications si demandé.
7. Lister les zones qui résistent à la reformulation.

---

## Cas d'usage typiques

- **Analyse de besoin** — reformuler une expression client en exigences actionnables
- **Juridique** — transposer des clauses en implications opérationnelles
- **Technique → métier** — reformuler une spec en termes business
- **Métier → technique** — reformuler un besoin en contraintes système

---

## Contraintes

- Ne pas confondre reformuler et simplifier.
- Ne pas combler les ambiguïtés — les signaler.
- Ne pas glisser vers la critique ou la décision.

---

## Format de sortie

```markdown
---
status: draft
skill: reformuler
registre: [registre cible]
contexte_cible: [si fourni]
---

# Reformulation — {sujet}

## Registre et contexte source
{identification}

## Contenu reformulé
{reformulation avec statut : certain / probable / fragile}

## Implications
- ...

## Zones résistantes
- [zone] → [raison]

## Questions ouvertes
- ...
```

---

## Définition de done

- Le contenu reformulé est lisible dans le registre cible sans relire le source.
- Les interprétations fragiles sont visibles.
- Les zones ambiguës sont signalées, pas comblées.
