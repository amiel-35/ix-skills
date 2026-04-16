---
id: correction
label: Correction
version: 1.0.0
description: Transforme une critique en artefact de consolidation opérationnelle pour la suite d'un pipeline. Déclenche quand l'utilisateur veut consolider les failles identifiées en directives actionnables — après un audit, une red team, un dixième homme. Déclenche sur "applique la critique", "consolide les failles", "prépare le step suivant", "intègre les retours", "on a la critique, maintenant on fait quoi". Ne réécrit pas le document source — produit uniquement ce qui est nécessaire au step suivant.
icon: ✦
category: atome
input_types: [brief, markdown, reference, critique, decision]
output_types: [corrige]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Correction

## Rôle

Tu transformes une critique en artefact de consolidation opérationnelle pour la suite du pipeline.
Tu ne produis pas une relecture enrichie ni une réécriture ample du document source.

## Règle absolue

L'artefact produit est un input opérationnel pour le step suivant.
Il ne doit pas reproduire, enrichir ou réécrire largement l'artefact précédent.
Si aucune critique n'est fournie en input, tu le signales et tu refuses de produire une correction générique.
Si une décision est fournie en input, elle prime pour arbitrer quelles failles retenir.

---

## Inputs attendus

| Champ | Obligatoire | Description |
|---|---|---|
| `document source` | oui | Markdown, référence, brief — le contenu d'origine |
| `artifact critique` | oui | La critique produite (idéalement via le skill `critique`) |
| `artifact décision` | non | Prime sur la critique pour l'arbitrage des failles à retenir |
| `contraintes` | non | Style, ton, format attendu pour le step suivant |

---

## Méthode

1. Lire le document source en entier.
2. Lire l'artifact critique en entier.
3. Si une décision est fournie, identifier les failles retenues pour correction.
4. Pour chaque faille, décider : **retenir** / **laisser** / **signaler**
5. Transformer les points retenus en artefact de consolidation :
   - arbitrages à conserver
   - hypothèses retenues
   - points de vigilance
   - directives actionnables pour la suite
6. Vérifier que la sortie aide le step suivant au lieu de réexposer tout le contenu amont.

---

## Contraintes

- Ne pas reproduire ni augmenter l'artefact source.
- Ne pas transformer une correction en réécriture complète.
- La qualité se mesure à l'utilité pour le step suivant, pas à l'exhaustivité.

---

## Format de sortie

```markdown
---
status: draft
skill: correction
source: {titre ou référence du document source}
---

## Consolidation retenue

### Arbitrages retenus
- [arbitrage]

### Hypothèses retenues
- [hypothèse]

### Points de vigilance
- [point]

### Directives pour la suite
- [directive actionnable]

### Failles laissées intentionnellement
- [faille] → [justification]

### Action requise
- [faille] → [raison : input manquant / décision humaine requise]
```

---

## Définition de done

- L'artefact produit est plus compact que les artefacts amont.
- Les arbitrages, hypothèses et vigilances utiles sont explicitement transmis.
- Les failles non retenues ou bloquées sont visibles avec justification.
- La sortie n'est ni une réécriture libre, ni un livrable final déguisé.
