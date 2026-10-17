<!-- Sortie brute de criteres-reussite 1.2.0, Sonnet, 0.46 $, 5 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: grille de salaires (fourchettes par niveau et famille), règles de positionnement et de passage, coût de mise en grille, notes CODIR et CSE; la suite est une négociation (NAO)
author: la RRH et l'analyste, avec un agent pour les calculs du tableur
judge: le DRH, qui garde la part cachée et exécute les contrôles (hypothèse [inféré], voir « Critère d'arrêt »)
requester: judge (« je jugerai ») — la part cachée est donc écrite
---

# Critères de réussite — Revue de la grille de salaires 2027

## Synthèse / Summary

Il s'agit de livrer 36 fourchettes (9 niveaux × 4 familles), les règles de positionnement et de passage, le coût de mise en grille et sa répartition, et deux notes (CODIR puis CSE). Le travail est terminé quand quelqu'un d'autre que la RRH et l'analyste peut refaire les calculs et retrouver les chiffres. Il faut aussi que le coût tienne dans 284 800 € chargés (3,2 % × 8,9 M€) et que les trois problèmes du constat soient réglés: compression 3–5, hors-fourchette (19 au-dessus, 6 en dessous) et écart de 7,2 % en conseil. Enfin, les critères de passage doivent être applicables par des lecteurs tiers, et la grille doit être publiable dans les offres.

**65 lignes visibles**: 36 mécanique, 21 relecture, 8 terrain. **16 lignes cachées**: 9 mécanique, 5 relecture, 2 terrain. Une boucle peut clore environ 55 % des lignes, surtout l'arithmétique, mais pas la conformité juridique, l'équité ni la NAO.

- J'ai lu les annexes « négociation » et « écrit ». Je n'ai pas lu l'annexe « logiciel »: c'est un tableur, pas un logiciel. J'applique la méthode et l'étape 12 directement.
- Hypothèses [inféré]:
  - Vous exécutez les contrôles ou les faites exécuter sous votre contrôle.
  - L'agent peut itérer dans le tableur jusqu'à ce que les tests passent.
- Cette réponse contient la part cachée. Ne la collez pas dans l'espace de travail de l'analyste ou de l'agent. Pour transmettre le plan visible, coupez à la ligne ✂ et retirez la colonne « Caché » du tableau de couverture.

**Lignes bloquantes**: 1, 2, 13, 19, 24, 37, 45, 46, 50, 51.

**Noyau** (30 lignes, mécanique et relecture rapide, sans terrain ni ligne cachée): 1, 2, 3, 4, 8, 9, 13, 14, 15, 19, 20, 22, 24, 25, 28, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 45, 46, 48, 49, 50.

**Légende « Qui vérifie »** (la RRH et l'analyste ne vérifient aucune ligne):
- **Script du juge**: script écrit par une personne sans accès aux salaires, testé sur un fichier fictif de même structure, puis lancé par le DRH sur le vrai export, hors de l'espace de l'agent.
- **DRH**: seul juge habilité à voir les salaires individuels.
- **Juriste**: juriste ou avocat en droit social. Il voit les textes et les agrégats, jamais une ligne individuelle.
- **Lecteurs tiers**: 2 à 3 managers ou personnes hors RH, sans accès aux salaires, qui travaillent sur des profils anonymisés et sans rémunération.
- **Admin IT**: voit les droits d'accès et les fichiers, pas leur contenu.

## Exigences / Requirements

| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Nouvelle grille: min, médiane, max par niveau (9) et par famille (4) | « fourchettes … par niveau et famille » | livrable |
| E2 | Compression 3–5 corrigée | « confirmés embauchés en 2025 gagnent autant que des seniors … six ans » | livrable (effet: issue) |
| E3 | 19 salariés au-dessus du max traités | « 19 salariés au-dessus du maximum » | livrable |
| E4 | 6 salariés sous le min traités | « 6 sous le minimum » | livrable |
| E5 | Écart F/H de 7,2 % en conseil traité | « 7,2 % à niveau égal sur la famille conseil » | livrable (écart à 12 mois: issue) |
| E6 | Critères écrits de passage de niveau | demande des élus du CSE | livrable (acceptation: issue) |
| E7 | Règles de positionnement | « règles de positionnement et de passage » | livrable |
| E8 | Coût de mise en grille et sa répartition | « le coût de mise en grille et sa répartition » | livrable |
| E9 | Enveloppe de 3,2 % de 8,9 M€ chargés = 284 800 €, mises en grille et augmentations individuelles comprises | « doit couvrir à la fois… » | livrable (tenue en NAO: issue) |
| E10 | Note de présentation, CODIR puis CSE | « note … au CODIR puis au CSE » | livrable |
| E11 | Préparation à la directive de 2023: fourchettes dans les offres, droit à l'information, rapport sur les écarts | « obligations de transparence salariale » | livrable |
| E12 | Calculs fondés sur l'export de paie au 30/09 et sur l'étude du cabinet | « Les données viennent de… » | livrable |
| E13 | Prêt pour la NAO de janvier, discussion de la grille et de l'enveloppe | « La NAO commence en janvier » | issue |
| E14 | Les 9 niveaux sont rattachés aux positions Syntec, et les minima conventionnels sont respectés | « rattachés aux positions de la convention »; minima [inféré] | livrable |
| E15 | Salaires individuels vus par la seule RRH, l'analyste et le DRH | dernière phrase du brief | livrable |
| E16 | Légalité [inféré]: aucune baisse de salaire, non-discrimination, consultations obligatoires | thème | livrable |
| E17 | Fiabilité et traçabilité du tableur et de l'agent [inféré] | thème | livrable |
| E18 | Données personnelles: ce qui part vers l'agent, pseudonymisation, effacement [inféré] | thème | livrable |
| E19 | Parties non représentées: futurs embauchés, temps partiels, salariés absents ou gelés au plafond, clients (taux de facturation) [inféré] | thème | issue |
| E20 | Mandat de négociation: priorités, plancher, repli si pas d'accord [inféré] | thème (négociation) | livrable (préparation) |

Limites (ce ne sont pas des exigences): une masse de 8,9 M€ brut chargé, 140 salariés, et une NAO en janvier 2027.

## Issue visée / Outcome zone

Les seuils marqués [proposé] sont à décider par vous avant le lancement. Un plancher fixé après avoir vu les résultats ne vaut rien.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E9, E10 | Validation CODIR | Grille et enveloppe ≤ 3,2 % validées assez tôt pour que le CSE ait ses documents dans le délai de la ligne 59 | Validées au premier passage, sans changer l'enveloppe | Direction générale et DRH | Date du CODIR [à fixer] |
| E13, E20 | Issue de la NAO | Accord ou avis recueilli, grille applicable à la date prévue sans conflit, coût ≤ le maximum du mandat | Accord à ≤ 3,2 % | Direction générale (mandat) | Fin de la NAO |
| E5 | Écart F/H en conseil | ≤ 5 % sur toutes les familles et aucun niveau de conseil au-dessus [proposé: seuil de la directive, à confirmer par le juriste] | ≤ 2 % [proposé] | DRH et direction | Recalcul à 12 mois, même méthode que la ligne 23, export au 30/09/2027 |
| E2 | Compression 3–5 | Écart entre médianes réelles de niveaux adjacents ≥ 6 % [proposé] et aucune nouvelle inversion créée par les embauches 2027 | ≥ 8 % [proposé] | DRH | 12 mois |
| E6, E13 | Durabilité | Grille appliquée comme écrit à 6 et 12 mois; départs des niveaux 3–5 non supérieurs à ceux de 2026 | Inférieurs, aucun contentieux de classification | DRH | 6 et 12 mois |
| E19 | Équité ressentie | Chez le DRH et chez les élus, aucune des 4 dimensions du questionnaire de valeur subjective nettement sous les autres | ≥ 70 % des répondants de l'enquête salariés disent comprendre les critères [proposé] | DRH | Après la NAO, puis à 6 mois |

## Critères vérifiables / Checks

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E12 — export au 30/09 | Compter les matricules, chercher les doublons et les champs vides | 140 matricules uniques (ou écarts expliqués ligne à ligne: alternants, mandataires…); 0 niveau, famille, sexe, taux ou fixe manquant; niveau 1–9; taux de temps ∈ ]0;1] | mécanique | Script du juge |
| 2 | E12 — masse | Recalculer (fixe + variable annualisés) × coefficient de charges (source paie) et comparer à 8,9 M€ | Écart ≤ 2 % [proposé] ou expliqué poste par poste | mécanique | Script du juge; DRH |
| 3 | E3, E4 — constats | Recompter sur l'ancienne grille et l'export | Exactement 19 au-dessus du max et 6 sous le min; sinon écart expliqué | mécanique | Script du juge |
| 4 | E5 — constat | Recalculer l'écart en conseil avec la méthode de la ligne 23 | 7,2 % ± 0,3 pt [proposé]; sinon écart de méthode expliqué | mécanique | Script du juge |
| 5 | E12 — datation | Lire les notes: chaque chiffre porte sa date; les entrées, sorties et augmentations depuis le 30/09 sont listées | Aucun chiffre sans date; variation d'effectif affichée | relecture | DRH |
| 6 | E12 — étude du cabinet | Pour chacune des 36 cellules, vérifier la présence de source, d'effectif de l'échantillon n, de date et de correspondance niveau/famille | 36/36 renseignées; cellules à n < 15 [proposé] signalées et non retenues seules | mécanique | Script du juge |
| 7 | E12 — étude | Lire les conditions de licence et la correspondance de niveaux | La citation en CODIR et en CSE est permise; les correspondances niveau/famille sont plausibles | relecture | Juriste (licence); pair RH hors entreprise (correspondances) |
| 8 | E1 — complétude | Parcourir les 36 fourchettes | 108 valeurs numériques; min < médiane < max partout | mécanique | Script du juge |
| 9 | E1 — progression | Comparer, par famille, les niveaux successifs | Min, médiane et max strictement croissants avec le niveau | mécanique | Script du juge |
| 10 | E1 — recouvrement | Calculer le chevauchement de niveaux adjacents | ≤ 50 % de la plus étroite des deux fourchettes [proposé] | mécanique | Script du juge |
| 11 | E1 — largeur | Calculer max/min par cellule | Dans un couloir fixé par le DRH avant le travail [proposé: 1,20 à 1,45] | mécanique | Script du juge |
| 12 | E14 — minima Syntec | Rapprocher le tableau de minima retenu du texte officiel en vigueur à la date d'application | Tableau conforme, avenant et date cités | relecture | Juriste ou paie |
| 13 | E14 — rattachement | Vérifier le rattachement des niveaux et comparer chaque min au minimum Syntec | Chaque niveau rattaché à une seule position; min de chaque cellule ≥ minimum conventionnel (temps partiel au prorata) | mécanique | Script du juge |
| 14 | E2 — écart entre niveaux | Calculer, par famille, le rapport des médianes de salaires réels après mise en grille, niveaux 3→4 et 4→5 | ≥ 6 % [proposé]; la valeur avant est affichée | mécanique | Script du juge |
| 15 | E2 — inversions | Compter les paires (niveau inférieur et ancienneté moindre) payées ≥ (niveau supérieur et ancienneté supérieure), dans la même famille | Compte avant et après; après = 0, ou chaque reste listé | mécanique | Script du juge |
| 16 | E2 — inversions restantes | Lire les motifs des paires restantes | Chaque reste a un motif écrit, objectif et sans référence au sexe | relecture | DRH |
| 17 | E3 — les 19 | Vérifier que chaque cas a un code de règle | 19/19 rattachés à une règle écrite une seule fois; 0 décision ad hoc | mécanique | Script du juge |
| 18 | E3 — règle | Lire la règle appliquée aux 19 | Appliquée de façon uniforme et défendable par le DRH devant les élus | relecture | DRH; juriste |
| 19 | E16 — aucune baisse | Comparer, par matricule, fixe 2027 et fixe 2026, à taux de temps inchangé | 0 baisse | mécanique | Script du juge |
| 20 | E4 — les 6 | Comparer leur fixe au nouveau min de leur cellule à la date d'effet | 6/6 ≥ min, ou exception datée et écrite | mécanique | Script du juge |
| 21 | E3, E4 — bornes | Pour chaque cellule dont le max ou le min s'écarte de plus de 10 % [proposé] de la référence marché, lire la justification | Aucune justification ne s'appuie sur un salarié nommé ou identifiable | relecture | DRH |
| 22 | E3, E4 — résiduel | Compter les salariés hors fourchette après mise en grille | ≤ 5 % de l'effectif [proposé], tous listés avec leur règle | mécanique | Script du juge |
| 23 | E5 — méthode | Lire la définition écrite avant tout calcul: équivalent temps plein, fixe ou total, définition de « niveau égal », ancienneté | Méthode datée et signée par le DRH avant le calcul de la ligne 4 | relecture | Juriste; DRH |
| 24 | E5 — après correction | Simuler l'écart en conseil après mise en grille, avec la méthode de la ligne 23 | ≤ plancher de la zone (5 % [proposé]) | mécanique | Script du juge |
| 25 | E5 — partout | Calculer l'écart pour les 4 familles et par niveau dans chaque famille | Aucune cellule de plus de 5 % [proposé] sans critère objectif écrit; écart des autres familles après ≤ avant | mécanique | Script du juge |
| 26 | E5 — correction | Lire les critères de rattrapage et le tableau de coût | Critères indépendants du sexe; poste de coût distinct dans le tableau | relecture | Juriste; DRH |
| 27 | E11 — neutralité | Lire les critères de niveau (disponibilité, astreintes, présence…) | Aucun critère indirectement lié au sexe sans justification écrite | relecture | Juriste ou référent égalité professionnelle |
| 28 | E6 — critères | Lire les critères des 9 niveaux | Chaque niveau a des critères avec un observable (périmètre, livrables, autonomie démontrée); aucun adjectif seul | relecture | Lecteurs tiers |
| 29 | E6 — test à deux lecteurs | Deux lecteurs classent 12 profils anonymisés avec les seuls critères écrits | ≥ 80 % [proposé] d'accord entre eux et avec le niveau de référence; les écarts renvoient à une réécriture | relecture | Lecteurs tiers |
| 30 | E6 — règle de passage | Lire la règle de passage | Conditions, délai maximal, décideur, voie de recours et calendrier annuel écrits | relecture | Juriste; lecteurs tiers |
| 31 | E6 — application | Appliquer les critères aux 140 | Reclassements ≤ 10 % [proposé], tous listés et motivés par les critères | mécanique | Script du juge |
| 32 | E7 — positionnement | Appliquer la règle deux fois aux 140 | Une position par salarié; résultats identiques | mécanique | Script du juge |
| 33 | E7 — historique | Chercher dans les règles « salaire précédent », « rémunération actuelle du candidat » et équivalents | 0 occurrence | mécanique | Script du juge |
| 34 | E7 — embauches | Passer 5 cas d'embauche écrits par le DRH dans la règle | Aucun nouvel embauché ne dépasse un titulaire plus ancien, même niveau et même famille, sans justification écrite | mécanique | Script du juge |
| 35 | E8 — coût | Refaire le calcul de coût par un script indépendant du tableur | Total identique à ± 0,5 % [proposé] | mécanique | Script du juge |
| 36 | E8 — répartition | Sommer les répartitions par famille, niveau, sexe et nature (grille, compression, rattrapage, individuel) | Chaque somme est égale au total, à l'euro | mécanique | Script du juge |
| 37 | E9 — enveloppe | Comparer le coût année pleine chargé, avec mises en grille et augmentations individuelles, à 284 800 € | ≤ 284 800 € | mécanique | Script du juge |
| 38 | E9 — date | Lire le coût en année pleine et le coût 2027 | Date d'effet écrite; les deux montants chargés sont affichés | mécanique | Script du juge |
| 39 | E9 — sensibilité | Faire varier le taux de charges de +2 pts, l'effectif de ±5 embauches et la date d'effet | Le coût suit; si l'enveloppe est dépassée, le montant est dit | mécanique | Script du juge |
| 40 | E9 — arbitrage | Lire la note: les postes obligatoires (6 sous le min, rattrapage, compression) plus les individuels contre l'enveloppe | Marge restante ou dépassement chiffré avec les options; rien n'est enfoui | relecture | DRH |
| 41 | E10 — mêmes chiffres | Extraire tous les chiffres des deux notes, de la grille et du tableau de coût | Identiques (même arrondi) | mécanique | Script du juge |
| 42 | E10 — restes | Chercher « [à compléter] », TODO, XXX, lorem, commentaires, modifications suivies et feuilles masquées dans les fichiers tels qu'envoyés | 0 occurrence | mécanique | Script du juge |
| 43 | E10 — questions posées | Lire la note CODIR (décisions demandées) et la note CSE (réponse à la demande de critères écrits) | Chaque décision et la demande des élus ont chacune une réponse localisable | relecture | DRH |
| 44 | E10 — lisibilité | 3 lecteurs hors RH restituent le message et les chiffres de la note CSE | ≥ 2 sur 3 restituent le bon message; ils trouvent les critères de passage en moins de 2 minutes | relecture | Lecteurs tiers |
| 45 | E15 — petits effectifs | Compter les personnes par cellule (famille × niveau × sexe) dans les notes | Aucune cellule < 5 personnes [proposé]; aucun matricule ni nom | mécanique | Script du juge |
| 46 | E15 — accès | Lister les droits sur l'export, le tableur, l'espace de l'agent et les journaux | Seuls la RRH, l'analyste et le DRH | mécanique | Admin IT; DRH |
| 47 | E18 — flux vers l'agent | Lire où vont les données quand l'agent travaille: prestataire, lieu d'hébergement, conservation, réutilisation | Flux documenté; registre des traitements à jour; avis du DPO ou du juriste | relecture | DPO ou juriste |
| 48 | E18 — pseudonymisation | Inspecter les fichiers donnés à l'agent | Aucune colonne nom ou prénom; matricule seul | mécanique | Script du juge |
| 49 | E18 — effacement | Chercher les matricules et salaires dans les dossiers, caches, journaux d'agent, exports et courriels | 0 copie hors archive désignée | mécanique | Script du juge; Admin IT |
| 50 | E17 — tableur | Parcourir le classeur final | 0 erreur (#REF!, #N/A…); 0 lien externe; 0 valeur saisie dans une cellule calculée; feuilles masquées documentées | mécanique | Script du juge |
| 51 | E11 — obligations | Lire la note juridique datée | Elle liste les obligations applicables à 140 salariés (offres, information, rapport), leurs dates et l'état de la transposition; la grille y répond | relecture | Juriste |
| 52 | E11 — offres | Rédiger 3 offres types avec la fourchette de la grille | Fourchette publiable et objective; aucune question sur l'historique de rémunération | relecture | Juriste |
| 53 | E11 — droit à l'information | Simuler 3 demandes (niveaux 2, 4 et 7, familles différentes) | Réponse en ≤ 10 jours ouvrés [proposé] avec le niveau de salaire et les moyennes par sexe de la catégorie; aucune donnée individuelle d'un tiers | terrain | DRH observe |
| 54 | E11 — rapport | Rapprocher les champs de l'export de la liste d'indicateurs fixée par le juriste | Tous présents, ou manquants listés | mécanique | Script du juge |
| 55 | E20 — mandat | Lire le mandat | Signé avant la première réunion de janvier: marge sur l'enveloppe, priorités, plancher et cible de chaque issue, repli chiffré si pas d'accord | relecture | Direction générale |
| 56 | E20 — gabarit | Contrôler l'arithmétique du gabarit de scores | Poids de chaque partie = 100; chaque paquet proposé noté pour chaque partie | mécanique | Script du juge |
| 57 | E20 — poids | Lire les poids et les replis des autres parties | Chaque poids est marqué comme estimation avec son fondement | relecture | Lecteur sans enjeu |
| 58 | E19 — absents | Lire la liste des parties non représentées | Chaque partie a son coût ou gain; revue par un tiers sans enjeu | relecture | Lecteur sans enjeu |
| 59 | E13 — calendrier | Relever les dates réelles de remise aux élus et au CODIR | Documents remis ≥ 8 jours ouvrés [proposé, ou le délai du juriste s'il est plus long] avant la première réunion | terrain | DRH |
| 60 | O1 — CODIR | Observer la décision | Dans la zone de la table des issues | terrain | DRH |
| 61 | O2 — NAO | Observer l'issue | Dans la zone | terrain | DRH |
| 62 | O3 — écart F/H | Recalculer à 12 mois, même méthode | Dans la zone | terrain | Script du juge; DRH |
| 63 | O4 — compression | Refaire les lignes 14 et 15 à 12 mois | Dans la zone | terrain | Script du juge; DRH |
| 64 | O5 — durabilité | Constater à 6 et 12 mois | Dans la zone | terrain | DRH |
| 65 | O6 — équité ressentie | Questionnaire séparé du DRH et des élus, puis enquête auprès des salariés | Dans la zone | terrain | DRH, via un tiers pour l'enquête |

## Ce qui passerait et serait faux / What could pass and still be wrong

- **Bornes déplacées.** Le max est relevé pour inclure les 19 et le min abaissé pour les 6: les comptes tombent à 0 sans régler le fond → lignes 21, 22 (et 10, 11).
- **Enveloppe respectée en apparence.** Le coût est calculé en brut, ou en coût 2027 partiel, alors que le coût année pleine chargé dépasse 284 800 € → lignes 37, 38, 2.
- **Écart déplacé.** Les 7,2 % « disparaissent » en changeant la définition (fixe contre total, regroupement de niveaux), ou la moyenne est corrigée alors qu'un niveau reste en écart, ou l'écart passe dans une autre famille → lignes 23, 25.
- **Compression masquée.** Elle est « réglée » par des fourchettes très larges et recouvrantes, alors que les paires de salaires réels restent inversées → lignes 14, 15, 10.
- **Critères écrits mais inapplicables.** Les adjectifs sont présents dans chaque niveau, mais deux lecteurs ne classent pas pareil → lignes 28, 29.
- **Chiffres divergents ou fuite.** La note CSE n'a pas les chiffres de la note CODIR, ou une petite cellule permet de deviner un salaire → lignes 41, 45.
- **Tableur figé.** Les valeurs sont collées et non calculées, le coût ne bouge pas quand on change une donnée → lignes 50, 35, 39.
- **Une note juridique mais pas de conformité.** Elle liste les obligations et la grille ne les remplit pas (offres, information) → lignes 51, 52.
- **Chemin heureux seulement.** La compression se reforme dès les premières embauches de 2027 → lignes 34, 63.

## Non testable en l'état / Not testable as stated

- **E1 — « grille compétitive ».** Aucune cible de position par rapport au marché n'est donnée. Question: quel percentile du marché vise-t-on, par famille (médiane, P60…)?
- **E9 — « couvrir à la fois mises en grille et individuelles ».** Aucune part minimale n'est donnée. Question: quelle part pour les augmentations individuelles, et dans quel ordre de priorité si l'enveloppe ne suffit pas?
- **E13 — « discuter de l'enveloppe ».** Question: le 3,2 % est-il négociable, de combien, et qui sont les interlocuteurs (délégués syndicaux ou élus du CSE)?
- **E5 — « à niveau égal ».** Question: la directive raisonne en travail de valeur égale, pas en niveau Syntec. Le niveau interne est-il la catégorie de comparaison retenue?

## Couverture / Coverage

| Kind | Visible | Caché | Who |
|---|---|---|---|
| mécanique | 36 | 9 | script du juge, lancé par le DRH hors de l'espace de l'agent |
| relecture | 21 | 5 | juriste, DPO, lecteurs tiers, DRH |
| terrain | 8 | 2 | DRH, janvier à fin 2027 |

Une boucle peut clore les 36 lignes mécaniques visibles et les 9 cachées, soit environ 55 % des lignes. Elles garantissent l'arithmétique, le coût, la cohérence et la confidentialité de fichiers. Elles ne disent rien de la conformité juridique, de la qualité des critères, de la NAO ni de l'équité ressentie, qui sont en relecture ou en terrain. Une grille dont tout le mécanique passe peut encore être refusée par les élus.

## Critère d'arrêt de la boucle / Loop stopping criterion

Réglage retenu: **un juge qui exécute** (étape 12). Si vous ne faites que lire ce que l'agent vous montre, c'est l'étape 13: seules les lignes mécaniques visibles du noyau peuvent être closes pendant la boucle, et le reste se joue après.

- **L'instrument est le vôtre.** Les scripts des lignes mécaniques sont écrits par une personne sans accès aux salaires, testés sur un fichier fictif de même structure, puis gelés avant le premier tour avec une somme de contrôle (checksum) que vous gardez.
- **La boucle s'arrête** quand toutes les lignes mécaniques visibles passent et que les lignes mécaniques cachées, lancées par vous hors de l'espace de l'agent, passent aussi. Le rapport de l'agent seul ne suffit jamais.
- **L'instrument reste intact.** Aucun test sauté, supprimé ou affaibli; le nombre de tests n'est pas inférieur à celui du jeu gelé.
- **La boucle ne décide pas** des lignes de relecture et de terrain. Quand une ligne échoue, l'agent reçoit l'exigence et le symptôme visible, jamais l'entrée cachée ni la valeur attendue.

## Questions ouvertes / Open questions

1. Date d'effet de la nouvelle grille (1er janvier, 1er avril…)? Elle change le coût 2027 (ligne 38).
2. Que contient la masse de 8,9 M€ (variable, charges patronales, année de référence)?
3. Le calcul interne de 7,2 % n'est pas daté: avec quelle méthode, sur quel export?
4. Politique de position sur le marché par famille (voir « Non testable »).
5. Tolérance de reclassement (ligne 31) et couloir de largeur (ligne 11), à fixer par vous avant le travail.
6. Minima Syntec: quel avenant est en vigueur à la date d'application? La source doit être confirmée avant tout calcul sur le contenu (ligne 12).
7. Directive de 2023: état de la transposition en France à ce jour, et quelles obligations s'appliquent à 140 salariés? Les dates du rapport dépendent de l'effectif (seuils dans la directive, à confirmer par le juriste).
8. L'agent est-il un service externe? Où partent les données individuelles?
9. Les 140 incluent-ils alternants et mandataires? Les temps partiels sont-ils ramenés à l'équivalent temps plein?
10. Licence de l'étude du cabinet: les chiffres peuvent-ils être cités en CODIR et en CSE (ligne 7)?

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part

À garder hors de l'espace de la RRH, de l'analyste et de l'agent. Une ligne qui a échoué puis été corrigée, ou dont le contenu a fuité, est remplacée. À l'échec, on indique à l'auteur l'exigence ou la famille d'exigences, jamais le test.

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E9 — coût, autre source | Recalculer le coût avec un coefficient de charges tiré des bordereaux du prestataire paie, par votre propre copie de l'export | Écart ≤ 0,5 % [proposé] avec le total livré | mécanique | DRH |
| H2 | E9 — tableur figé | Dans une copie, modifier 10 salaires de l'export et relancer le classeur livré | Le coût bouge de la variation attendue ± 1 % [proposé] | mécanique | DRH |
| H3 | E5 — autres méthodes | Recalculer l'écart en conseil après correction par 3 méthodes: taux horaire équivalent temps plein, fixe seul, régression sur niveau, ancienneté et temps | ≤ plancher de la zone avec les 3 | mécanique | DRH |
| H4 | E5 — rattrapage réel | Dans une copie, mélanger au hasard le sexe puis relancer la règle de rattrapage | Coût du rattrapage ≤ 10 % [proposé] du coût réel: la règle réagit à un écart réel, elle ne déguise pas une augmentation générale | mécanique | DRH |
| H5 | E3, E4 — bornes bougées | Comparer la première version datée de la grille (que vous avez conservée) à la version finale | Toute cellule où min ou max a bougé de ≥ 5 % [proposé] pour y faire entrer des salariés hors fourchette est justifiée par écrit | mécanique | DRH |
| H6 | E3, E4 — bornes indépendantes | Retirer les 25 salariés hors fourchette de votre copie et recalculer les cellules, si la grille est dérivée des données | Bornes inchangées à ± 3 % [proposé] | mécanique | DRH |
| H7 | E6 — profils pièges | Six profils fictifs: deux limites, deux avec adjectifs forts et faits faibles, deux francs, classés par deux lecteurs avec les critères écrits | ≥ 5 sur 6 conformes à votre référence; les profils limites sont tranchés par la règle écrite | relecture | Lecteurs tiers |
| H8 | E6 — concordance | Pour 20 salariés tirés au hasard, comparer leur niveau selon les critères à l'appréciation du manager sur dossier anonymisé | ≥ 80 % [proposé] de concordance | relecture | Managers sans enjeu |
| H9 | E15 — ré-identification | Avec votre export, tenter de retrouver une personne ou un des 19 / 6 à partir des notes (cellules, croisements famille, niveau, bande d'ancienneté) | 0 personne identifiée | relecture | DRH; tiers sans enjeu |
| H10 | E15 — fichiers bruts | Décompresser les .xlsx et .docx livrés; chercher feuilles masquées, caches de tableaux croisés, commentaires et propriétés du document | Aucune donnée individuelle; aucun nom d'auteur ou de dossier interne résiduel | mécanique | DRH; Admin IT |
| H11 | E2 — embauches rejouées | Cinq profils d'embauche à vous (un confirmé, un senior, etc.) passés dans la règle de positionnement | Aucun ne passe au-dessus de la médiane des titulaires plus anciens du même niveau et de la même famille | mécanique | DRH |
| H12 | E2 — le cas du brief | Dans votre copie, isoler les confirmés embauchés en 2025 et les seniors de six ans, niveaux 3 à 5 | Écart de salaire réel après mise en grille ≥ celui de la ligne 14 pour ces paires; si ce n'est pas le cas, le motif est écrit | mécanique | DRH |
| H13 | E20 — contrepartie simulée | Faire jouer les élus par `red-team` à partir de leurs seuls intérêts, sans le plan, sur un tour | Les réponses du plan tiennent sans franchir le plancher; les 3 coups les plus forts ont été anticipés | relecture | DRH; `red-team` |
| H14 | E20 — paquet dominant | Même simulation: la contrepartie cherche un paquet que les deux côtés préfèrent à la cible du plan | Aucun, ou le plan est amendé; le coût du paquet adverse est chiffré dans le classeur le jour même | relecture | DRH; `red-team` |
| H15 | E11 — demande inopinée | Déposer vous-même une demande d'information fictive (niveau 5, conseil) sans prévenir | Réponse dans le délai de la ligne 53, contenu correct, aucune donnée individuelle | terrain | DRH |
| H16 | E11 — petite catégorie | Demande fictive dans une catégorie avec 2 personnes du même sexe | La réponse ne révèle pas un salaire individuel | terrain | DRH |

**Exigences gardées** (au moins deux lignes chacune):
- E9: H1, H2
- E5: H3, H4
- E3 et E4: H5, H6
- E6: H7, H8
- E15: H9, H10
- E2: H11, H12
- E20: H13, H14
- E11: H15, H16

Elles sont les plus exposées au contournement: instruments qu'on peut modifier (H2, H5), valeurs collées (H2), définitions qu'on peut changer (H3, H4) et critères sans effet réel (H7, H8). Toutes testent des exigences que l'auteur connaît déjà dans le plan visible, par d'autres entrées ou sous un autre angle.

Les lignes 10 et 11 (recouvrement, largeur) sont les plus faibles du plan visible: leurs seuils sont [proposé] et peuvent être satisfaits en changeant la grille. H5 et H6 les complètent.