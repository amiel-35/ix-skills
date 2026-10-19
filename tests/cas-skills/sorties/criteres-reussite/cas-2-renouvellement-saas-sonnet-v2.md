<!-- Sortie brute de cahier-de-recette 1.0.0 (version ajustée du 2026-10-17), Sonnet, 0.29 $, 3 min. Cas : ../../cahier-de-recette.md -->

---
status: draft
skill: cahier-de-recette
deliverable_kind: négociation (dossier de préparation, puis accord)
author: directeur commercial + vous (demandeur)
judge: CEO, qui n'a pas participé au compte
---

# Cahier de recette: préparation de la renégociation du contrat de planification des tournées (client ETI logistique)

J'ai lu l'annexe négociation. Le demandeur fait partie des auteurs, donc je n'ai pas écrit de part cachée (voir la fin du document). Votre CEO doit lancer lui-même l'étape de la part cachée.

## Synthèse / Summary
Ce qui est livré: un dossier de préparation (mandat, intérêts des deux côtés, replis, concessions, scénarios) avant la négociation de novembre. Il est suivi d'un accord, dont on vérifie à 6 et 12 mois s'il était bon.

« Prêt » veut dire cinq choses:
- le dossier est complet et ses chiffres se recalculent;
- le CEO a signé un mandat avec plancher et cible avant la première offre;
- chaque camp a un repli valorisé;
- aucun scénario ne repose sur l'hypothèse que le client veut rester;
- quelqu'un qui n'a pas écrit le dossier sait le restituer.

« Bon accord » veut dire que les termes signés sont dans la zone fixée d'avance, au-dessus des deux replis. Il faut ensuite que l'accord soit appliqué, qu'il n'y ait pas de litige, que l'usage reparte et que la marge tienne.

Le plan compte **51 lignes visibles**: 21 mécaniques, 21 relectures, 9 terrain. Une boucle automatique ne couvre que le contrôle de l'arithmétique et de la complétude, soit environ 40 % des lignes. L'accord, la satisfaction et la durabilité ne se jouent pas là. Ce n'est pas un plan de boucle: l'auteur est humain.

**Alerte à lire avant tout.**
- Le préavis de 6 mois expirait le 30/09/2026 et nous sommes le 17/10.
- Le client dit avoir « ouvert une consultation » le 12/09 sans dénoncer formellement.
- Le contrat est peut-être reconduit, ou peut-être arrive-t-il à échéance le 31/03/2027. Cela change notre levier et notre repli.
- Aucune ligne du dossier ne vaut tant que ce point n'est pas tranché par un juriste (ligne 9).

Lignes bloquantes / Blocking lines: 9, 12, 13, 14, 37

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Un dossier complet: mandat, intérêts des deux côtés, replis, plan de concessions, scénarios | « un dossier de préparation (mandat signé par notre CEO, analyse des intérêts… scénarios) » | livrable |
| E2 | Mandat signé du CEO, avec plancher et cible par enjeu, fixés avant la première offre | « mandat signé par notre CEO »; « au minimum garder 170 k€/an » | livrable (les valeurs plancher/cible relèvent de l'issue) |
| E3 | Analyse des intérêts des deux côtés (DAF, nouveau directeur des opérations, entrepôts, concurrent) | « analyse des intérêts des deux côtés » | livrable |
| E4 | Replis valorisés: le nôtre et celui du client (concurrent + migration) | « solutions de repli »; concurrent à 150–170 k€/an + 60–90 k€ de migration | livrable |
| E5 | Plan de concessions face à −12 %, SLA 99,9 % avec pénalités, et vente du module à 38 k€/an | « −12 % et un SLA à 99,9 % avec pénalités »; module testé à Lyon (−9 % de km) | livrable |
| E6 | Scénarios, dont la situation contractuelle après le 30/09 (reconduit, échu, incertain) | « en fait ils nous ont écrit le 12/09… sans dénoncer formellement » | livrable |
| E7 | Accord: au moins 170 k€/an; idéal 3 ans de plus, indexation Syntec, module 38 k€/an | « au minimum garder 170 k€/an, idéalement… » | issue |
| E8 | Savoir à 6 et 12 mois si l'accord était bon, pas seulement signé | « dans six mois et dans un an, si l'accord était bon » | issue |
| E9 | Dossier prêt avant la négociation de novembre, avec un délai pour que le juge le lise | « on négocie en novembre » | livrable |
| E10 | Le mandat et les planchers ne fuient pas vers le client `[inferred]` | pratique de négociation | livrable |
| E11 | Parties touchées et non représentées identifiées `[inferred]` | annexe négociation §8 | livrable |
| E12 | Chiffres sourcés, recalculables et cohérents entre les pièces `[inferred]` | attente d'un lecteur compétent | livrable |

## Issue visée / Outcome zone
Les valeurs ci-dessous sont celles de votre direction, ou marquées `[proposed]`. Elles sont à confirmer et à signer par le CEO **avant la première offre**. Un plancher fixé après les premières discussions n'est pas un plancher.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E7 | Revenu annuel récurrent du compte | 170 k€/an (« au minimum »); à préciser: module inclus ou non, net de pénalités | 186 k€ + 38 k€ module = 224 k€/an `[proposed]` | CEO | à la signature |
| E7 | Durée | à fixer par le CEO | 36 mois de plus | CEO | à la signature |
| E7 | Indexation | à fixer par le CEO | Syntec | CEO | à la signature |
| E5 | SLA et pénalités | plafond annuel des pénalités à fixer par le CEO | rester à 99,5–99,7 % contractuel, avec crédits plafonnés `[proposed]` | CEO | à la signature |
| E8 | Satisfaction ressentie (Subjective Value Inventory, échelle 1–7) | ≥ 4,0 sur chacune des 4 dimensions `[proposed]` | ≥ 5,0 sur chacune `[proposed]` | CEO | juste après la signature |
| E8 | Usage Valence/Orléans (base: connexions de janvier 2026) | pas de baisse supplémentaire | retour à ≥ 80 % de la base `[proposed]` | CEO | T+6 et T+12 |
| E8 | Module vendu: baisse des km mesurée sur les données du client | ≥ −4,5 % (moitié du pilote) `[proposed]` | ≥ −9 % (pilote Lyon) | CEO | T+6 et T+12 |
| E8 | Contribution du compte (revenu − coût de service) | ≥ 98 k€/an (170 − 72) | ≥ 152 k€/an (224 − 72) `[proposed]` | CEO | T+12 |
| E8 | Durabilité | aucune dénonciation ni renégociation forcée | le client renégocierait de nouveau avec nous | CEO | T+6 et T+12 |

« T+6 » et « T+12 » se comptent à partir de la **date d'effet** des nouvelles conditions `[proposed]`. Si l'effet est le 01/04/2027, six mois après une signature de novembre ne donneraient que 2 à 3 mois de données (voir les questions ouvertes).

## Cahier de recette / Acceptance plan

**A. Le dossier: complétude et contenu**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1: les cinq composants | Ouvrir le dossier final tel que transmis et lister ses sections | Mandat, intérêts, replis, concessions, scénarios: les 5 présents, chacun avec un contenu propre (aucun renvoi « à venir ») | mécanique | quiconque ≠ auteur |
| 2 | E1: aucune lacune dans le rendu final | Rechercher dans le PDF/tableur final et toutes ses annexes: « [à compléter] », TODO, TBD, XXX, lorem, cellule vide d'un tableau, nom-placeholder (« Client X ») | 0 occurrence | mécanique | quiconque ≠ auteur |
| 3 | E12: sources des chiffres | Pour chaque chiffre des tableaux de synthèse, relever sa source (contrat, facturation, logs, estimation) | 100 % ont une source; toute estimation est étiquetée « estimation » avec son fondement | relecture | finance; données du compte visibles |
| 4 | E12: chiffres dérivés | Recalculer: 141 + 45 = 186; 141 k€/420 ≈ 336 €/utilisateur; 186 × 0,88 = 163,7 k€; 186 − 72 = 114 k€; 170 − 72 = 98 k€; 186/0,14 ≈ 1,33 M€ de CA récurrent total | Écart ≤ 1 % avec les valeurs du dossier; le CA récurrent total correspond au chiffre de la finance | mécanique (`calc-check`) | finance |
| 5 | E5, E12: SLA en durée d'indisponibilité | Convertir 99,5 / 99,7 / 99,9 % en heures par an selon la période et la définition du contrat | ≈ 43,8 h / 26,3 h / 8,8 h sur 365 j; la définition contractuelle (exclusions, maintenances) est citée | mécanique | quiconque ≠ auteur |
| 6 | E12: éléments nommés | Pour chaque référence (article du contrat, annexe, rapport du pilote Lyon, courrier du 12/09, export de logs), chercher le document dans le dossier | Chaque référence renvoie à un document présent | mécanique | quiconque ≠ auteur |
| 7 | E12: cohérence entre les pièces | Extraire chaque occurrence de 186 k€, 72 k€, 170 k€, 38 k€ dans toutes les pièces | Une seule valeur par grandeur | mécanique | quiconque ≠ auteur |
| 8 | E9: date de remise | Relever la date d'accusé de remise au CEO et la date de la première séance | Remise ≥ 7 jours avant la première séance `[proposed]` | mécanique | CEO |

**B. Position contractuelle (E6)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 9 | E6: effet du 30/09 | Un avis écrit analyse la clause de reconduction et de préavis, la forme exigée pour dénoncer, la durée de reconduction, l'effet du courrier du 12/09 | Le dossier cite la clause et conclut: (a) reconduit, (b) échu au 31/03/2027, ou (c) incertain; avis signé; courrier du 12/09 annexé | relecture | juriste; contrat visible |
| 10 | E6: scénarios par branche | Relire les scénarios | ≥ 1 scénario par branche de la ligne 9 et par issue (accord, expiration, migration chez le concurrent); chacun dit ce qu'il change au plancher et aux concessions | relecture | CEO |
| 11 | E6: perte du compte | Relire le scénario de perte | Chiffre la perte (186 k€ de revenu, 114 k€ de contribution, 14 % du récurrent) et décrit la réponse de l'entreprise le lendemain | relecture | CEO + finance |

**C. Mandat et zone (E2)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 12 | E2: signature et date | Relever signature et date du mandat; les comparer à la date de la première offre ou du premier échange chiffré | Signé par le CEO, daté avant toute offre | relecture | CEO |
| 13 | E2: complétude plancher/cible | Pour prix, durée, indexation, module, SLA, plafond de pénalités, paiement: chercher un plancher et une cible | 7 enjeux × 2 valeurs, avec unité, aucune case vide | mécanique | quiconque ≠ auteur |
| 14 | E2, E4: plancher face au repli | Relire la section du mandat sur 170 k€ | Dit si 170 k€ est un point de retrait ou une préférence, comparé à notre repli (114 k€ de contribution perdue sans accord vs 98 k€ à 170 k€) | relecture | CEO |
| 15 | E2, E5: plancher net de pénalités | Recalculer le revenu net en retranchant l'exposition attendue aux pénalités de chaque option de SLA | Le net de chaque package ≥ plancher; l'exposition est calculée sur les 99,7 % réels | mécanique | finance |
| 16 | E2: règle de partage | Chercher la règle (Nash ou maximin, nommée; maximin signalé comme analogie) et un seuil pour la partie la moins servie | Règle et seuil écrits avant la première offre | relecture | CEO |
| 17 | E2 `[inferred]`: autorité de retrait | Chercher qui peut autoriser un écart sous le plancher et sous quel délai | Une seule personne désignée (le CEO), avec délai | relecture | CEO |

**D. Intérêts des deux côtés (E3)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 18 | E3: notre grille | Chercher la grille (enjeux, options, poids, scores) et le visa du mandant | Grille existante, poids visés par le CEO avant la première offre | relecture | CEO |
| 19 | E3: arithmétique des poids | Additionner les poids de chaque partie | Somme = 100 pour chaque partie; scores recalculés à l'identique | mécanique | quiconque ≠ auteur |
| 20 | E3: grille du client | Relire les poids par acteur (DAF, nouveau directeur des opérations, directeurs de Valence et Orléans, IT/WMS) | Chaque poids est étiqueté « estimation » avec son fondement (fait observé, courrier du 12/09, démo d'août…) | relecture | un tiers qui connaît le compte (support), plus le CEO |
| 21 | E3: tout est scoré | Chercher les cellules vides parmi les options et packages du plan de concessions | Chaque option a un score pour chaque partie, 0 case vide | mécanique | quiconque ≠ auteur |
| 22 | E3: positions et intérêts | Pour −12 % et 99,9 %, relire l'intérêt sous-jacent | Chaque demande a un intérêt documenté et ≥ 2 options qui le satisfont autrement | relecture | CEO |
| 23 | E3: baisse d'usage | Recalculer la baisse de connexions à Valence et Orléans depuis l'export de logs | −40 % ± 2 points depuis janvier | mécanique | quiconque ≠ auteur |
| 24 | E3: cause de la baisse | Relire l'hypothèse « ancien outil Excel » | Confirmée ou infirmée par une source autre que notre supposition (entretien utilisateur, logs), avec une action associée | relecture | tiers du support |

**E. Replis (E4)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 25 | E4: notre repli | Relire la valorisation sans accord | Contribution perdue, capacité libérée, coûts de sortie; le 72 k€ ventilé entre coûts directs et alloués, avec sa source | relecture | finance |
| 26 | E4: repli du client, calcul | Recalculer le coût du client sur 3 ans | Concurrent: 510–600 k€ (3 × 150–170 + 60–90); nous à −12 %: ≈ 491 k€; bornes basse et haute présentes | mécanique | quiconque ≠ auteur |
| 27 | E4: repli du client, hypothèses | Relire l'origine des 150–170 k€ et des 60–90 k€ | Chaque estimation a sa base; le dossier estime la durée de migration de 11 entrepôts par rapport au 31/03/2027 | relecture | tiers du support + CEO |
| 28 | E4: au-dessus des replis | Comparer plancher, cible et chaque package à chaque repli, dans la grille | Chaque package dépasse notre repli et celui du client; sinon une justification écrite | mécanique | quiconque ≠ auteur |
| 29 | E4: non-dominance | Énumérer les packages de la grille | Aucun package de la grille ne domine la cible du plan | mécanique | quiconque ≠ auteur |

**F. Concessions (E5)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 30 | E5: structure des concessions | Chercher, pour chaque concession, la contrepartie, la valeur pour nous et pour le client, l'ordre, la limite | Aucune concession sans contrepartie | mécanique | quiconque ≠ auteur |
| 31 | E5: enchaînement | Rejouer la séquence des concessions dans l'ordre | Aucune étape ne franchit le plancher; la séquence finale reste ≥ plancher | relecture | CEO |
| 32 | E5: options de SLA | Relire les options de 99,5 % à 99,9 % | Coût estimé pour y arriver (astreinte, redondance) et exposition aux pénalités en €/an, plafond inclus | relecture | responsable technique + finance |
| 33 | E5 `[inferred]`: SLA de l'hébergeur | Chercher le SLA contractuel de l'hébergeur en amont | Document présent; SLA ≥ niveau que nous engagerions, ou écart traité dans le dossier | relecture | responsable technique |
| 34 | E5: pilote Lyon | Retracer le −9 % de km jusqu'à la mesure d'origine | Chiffre rattaché à des données du client ou vérifiables par lui, avec méthode et période | relecture | quelqu'un qui n'a pas monté le pilote |
| 35 | E5: gain pour le client sur le module | Recalculer le retour sur 38 k€ à partir de ses propres km | Hypothèses écrites; le gain chiffré recalculé à l'identique | mécanique | finance |

**G. Hors table, confidentialité, restitution (E10, E11, E1)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 36 | E11: parties non représentées | Relire la liste | Contient au moins nos autres clients (précédent d'un SLA à 99,9 % avec pénalités), notre équipe d'astreinte, les planificateurs de Valence et Orléans; coût/gain de chacune; relu par quelqu'un sans enjeu | relecture | un membre de l'équipe qui n'a pas travaillé sur le dossier |
| 37 | E10: fuite du mandat | Inspecter la version emportée en séance: feuilles masquées, commentaires, suivi des modifications, métadonnées, plages cachées | 0 plancher, 0 point de retrait, 0 coût de service dans cette version | mécanique | quiconque ≠ auteur |
| 38 | E1: restitution | Un lecteur qui n'a pas écrit le dossier le résume | Il redonne de mémoire plancher, première concession et condition de retrait, sans erreur | relecture | CEO ou un tiers désigné |

**H. L'accord et son suivi (E7, E8)**

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 39 | E7: revenu signé | Recalculer le revenu annuel du contrat signé | ≥ 170 k€/an, net de pénalités attendues | mécanique (après signature) | finance |
| 40 | E7: termes dans la zone | Comparer durée, indexation, SLA, plafond de pénalités, module au mandat | Chaque terme dans la zone plancher–cible | mécanique (après signature) | quiconque ≠ auteur |
| 41 | E7: texte complet | Rechercher les lacunes (ligne 2) et recalculer les totaux du contrat | 0 lacune; totaux exacts; les articles cités existent | mécanique (après signature) | quiconque ≠ auteur |
| 42 | E7: texte fidèle | Rapprocher chaque concession arrêtée en séance de sa clause | Chaque point négocié a sa clause; aucune clause n'est hors du mandat | relecture | juriste |
| 43 | E8: satisfaction ressentie | Questionnaire SVI (16 questions) à chaque négociateur, séparément; réponses gardées de l'autre camp; conditions d'usage à vérifier | Chaque dimension dans la zone fixée `[proposed]` | terrain | juste après la signature |
| 44 | E8: équilibre des dimensions | Comparer les 4 dimensions de chaque partie | Aucune dimension à plus de 1,5 point sous la moyenne des autres `[proposed]` | terrain | juste après la signature |
| 45 | E8: appliqué tel qu'écrit | Relever facturation, indexation à la date due, paiements, rapports de SLA | Appliqué comme écrit à T+6 et T+12 | terrain | finance, T+6/T+12 |
| 46 | E8: SLA réel et pénalités | Comparer le SLA mesuré au contractuel; relever les pénalités payées | Pénalités ≤ plafond du mandat | terrain | responsable technique, T+6/T+12 |
| 47 | E8: usage Valence/Orléans | Relever les connexions par rapport à janvier 2026 | Pas de baisse supplémentaire; cible ≥ 80 % de la base | terrain | support, T+6/T+12 |
| 48 | E8: module | Mesurer la baisse de km sur les données du client | ≥ −4,5 % plancher, −9 % cible | terrain | support/produit, T+6/T+12 |
| 49 | E8: pas de renégociation forcée | Relever dénonciation, avenant de baisse, litige, escalade | Aucune | terrain | CEO, T+6/T+12 |
| 50 | E8: relation | Entretien avec le sponsor du client mené par quelqu'un qui n'a pas négocié | « Négocierait de nouveau avec nous »: oui | terrain | un tiers, T+6/T+12 |
| 51 | E8: contribution | Calculer revenu − coût de service | ≥ 98 k€/an | terrain | finance, T+12 |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Le dossier est complet, mais il suppose que le contrat est encore ouvert à la négociation alors que le préavis est dépassé → 9, 10.
- Le plancher de 170 k€ est signé, mais il compte brut de pénalités: un SLA à 99,9 % avec pénalités non plafonnées ramène le net sous le plancher → 15, 40.
- Les grilles sont justes arithmétiquement, mais les poids du client sont arrangés pour que notre cible domine → 20, 22.
- Les 99,7 % réels sont cités, mais mesurés autrement que dans le contrat → 5, 32.
- Un plancher fixé au-dessus du repli passe pour un point de retrait, et le négociateur abandonne un accord qui valait mieux que rien → 14.
- Les scénarios supposent tous que le client veut rester; aucun ne traite la migration chez le concurrent → 10, 11, 27.
- Le plancher figure dans une feuille masquée de la version emportée en séance → 37.
- L'accord est signé au bon prix, mais Valence et Orléans continuent de s'éloigner; le renouvellement suivant échoue → 47, 49.
- Le module est vendu au prix, mais le −9 % du pilote ne se reproduit pas hors de Lyon → 34, 48.
- Les relecteurs partagent le point de vue des auteurs (même équipe commerciale) → 36, 38, et la part cachée à demander.

## Non testable en l'état / Not testable as stated
- « Un bon accord », en bloc: décomposé en zone d'issue (lignes 39–51); le jugement global reste celui du CEO sur ces lignes.
- Le prix du concurrent: testable seulement comme estimation (lignes 20, 27), non comme fait. Qu'est-ce qui l'étayerait (devis vu chez un autre client, marché, appel d'offres)?
- La satisfaction du client: elle ne se mesure que s'il accepte de répondre. Sinon la ligne 50 la remplace par un entretien mené par un tiers.
- « Idéalement 3 ans de plus » et « indexation Syntec »: pas de plancher donné. Quel plancher de durée et d'indexation accepterait le CEO?

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 21 | à demander | script ou relecteur sans enjeu, lancé par le juge |
| relecture | 21 | à demander | CEO, juriste, finance, responsable technique, tiers du support |
| terrain | 9 | à demander | séance, puis T+6 et T+12 après la date d'effet |

Une boucle automatique ne ferme que les lignes mécaniques, c'est-à-dire l'arithmétique des grilles, la complétude et la cohérence des pièces: environ 40 %. Les repli, intérêts du client et parties absentes relèvent de la relecture. L'accord, la satisfaction et la durabilité relèvent du terrain et ne peuvent pas être cochés avant.

## Questions ouvertes / Open questions
1. **Blocage:** le contrat est-il reconduit, échu, ou incertain après le 30/09 et le courrier du 12/09? Qui rend l'avis juridique, et quand?
2. 170 k€ est-il un point de retrait ou une préférence? Inclut-il le module de 38 k€? Est-ce par an, net de pénalités?
3. Quelle est la date de la première séance? Elle fixe le délai de la ligne 8.
4. Quelles sont les dates d'effet du nouvel accord? Elles fixent T+6 et T+12.
5. Quels planchers pour la durée, l'indexation et le plafond de pénalités? À fixer par le CEO.
6. Qui, dans l'équipe, est le relecteur sans enjeu des lignes 36 et 38?
7. Le client acceptera-t-il de répondre au questionnaire de satisfaction?
8. Limite de ce plan: le CEO est à la fois celui qui signe le mandat et le juge. Les lignes 38 et la part cachée à demander réduisent ce risque, sans le supprimer.

✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Exigences à garder: **E2, E3, E4, E5, E6, E12**. Environ 10 lignes, au moins une par exigence listée. Au moins un tiers des lignes viennent du comptage ci-dessus; ajoutez les trois lignes de contrepartie simulée de l'annexe négociation §9.

Au CEO: lancez `cahier-de-recette` avec `requester: judge`, ce brief et le plan visible ci-dessus. Gardez le résultat pour vous. Ne le transmettez ni au directeur commercial ni au demandeur, même en cas d'échec: dites seulement quelle exigence a échoué.