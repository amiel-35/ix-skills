<!-- Sortie brute de cahier-de-recette 1.0.0 (brouillon du 2026-10-17, avant ajustements), Sonnet, 0.33 $, 4 min. Cas : ../../cahier-de-recette.md -->

---
status: draft
skill: cahier-de-recette
deliverable_kind: grille de salaires (document chiffré, règles) + note CODIR/CSE, destinés à une négociation (NAO)
author: RRH + analyste, calculs tableur assistés par un agent
judge: DRH (porte la part cachée)
---

# Cahier de recette — Revue de la grille de salaires 2027

Pour ce cahier, j'ai lu l'annexe « négociation ». L'annexe « logiciel » n'a pas été lue, car le livrable n'est pas un logiciel. Les règles de boucle sont reprises plus bas, pour l'agent qui calcule.

## Synthèse / Summary
Le livrable est une grille de 9 niveaux × 4 familles, des règles de positionnement et de passage, un coût de mise en grille réparti, et une note CODIR puis CSE. « Terminé » veut dire trois choses. La grille est cohérente, sourcée et rejouable. Le coût tient dans 284 800 € (3,2 % × 8,9 M€). Aucune donnée individuelle ne sort du cercle des trois personnes autorisées.
Le cahier compte 85 lignes : 47 mécaniques, 31 de relecture, 7 de terrain. Parmi elles, 15 sont cachées. Une boucle automatique peut en couvrir environ 55 % en nombre de lignes. Elle ne couvre rien de l'issue (accord en NAO, ressenti, effets à 12 mois).
Question principale : le périmètre exact de la « préparation à la directive » et la base de calcul du 3,2 %. Voir la fin du document.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Grille de fourchettes (min, médiane, max) par niveau (9) et famille (4) | « la nouvelle grille (fourchettes par niveau et famille) » | livrable |
| E2 | Résorber la compression niveaux 3–5 | « confirmés embauchés en 2025 gagnent autant que des seniors présents depuis six ans » | livrable (simulé), issue (réel) |
| E3 | Traiter les 19 salariés au-dessus du max et les 6 sous le min | « 19 salariés au-dessus du maximum… 6 sous le minimum » | livrable |
| E4 | Traiter l'écart F/H de 7,2 % en conseil, à niveau égal | « écart… 7,2 % à niveau égal sur la famille conseil » | livrable (simulé), issue (réel) |
| E5 | Critères écrits de passage d'un niveau à l'autre | « demande des élus du CSE » | livrable ; leur acceptation est une issue |
| E6 | Préparer la transparence de la directive 2023 (fourchettes dans les offres, droit à l'information, rapport sur les écarts) | « se préparer aux obligations de transparence » | livrable (préparation), périmètre à préciser |
| E7 | Tenir l'enveloppe : 3,2 % de 8,9 M€ chargé, qui couvre mises en grille et augmentations individuelles | « enveloppe de 3,2 %… doit couvrir à la fois » | livrable (plan), issue (exécution) |
| E8 | Règles de positionnement (entrée, promotion, placement dans la fourchette) | « règles de positionnement et de passage » | livrable |
| E9 | Coût de mise en grille et répartition | « le coût de mise en grille et sa répartition » | livrable |
| E10 | Note de présentation CODIR, puis CSE | « une note… au CODIR puis au CSE » | livrable ; la décision est une issue |
| E11 | S'appuyer sur l'export de paie au 30/09 et l'étude du cabinet | « Les données viennent de… » | livrable |
| E12 | Salaires individuels vus par la RRH, l'analyste et le DRH seulement | « ne doivent être vus que par… » | livrable |
| E13 | Minima conventionnels Syntec respectés [inferred] | « convention Syntec… rattachés aux positions » | livrable |
| E14 | Grille cohérente en interne : min < médiane < max, progression entre niveaux [inferred] | compétence attendue d'une grille | livrable |

## Issue visée / Outcome zone
Les seuils marqués [proposed] sont à confirmer ou corriger par le DRH et la direction avant le début du travail, pas après avoir vu les résultats.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E10 | Validation CODIR | Grille renvoyée pour reprise avant la NAO | Validée avec l'enveloppe et son mandat de concession | Direction | Date de CODIR à fixer, avant janvier |
| E5, E7 | NAO sur la grille et l'enveloppe | La discussion s'ouvre sur la grille et les critères comme base, sans rejet de principe | Accord signé sur grille + critères, enveloppe ≤ mandat | Direction (mandat), avant la 1re séance | Clôture de la NAO |
| E7 | Exécution | Coût réel > 284 800 € ou ≥ 1 salarié sous le min à la date d'effet | Coût réel ≤ 284 800 € et 0 sous le min | DRH | 1re paie après la date d'effet, puis 12 mois |
| E4 | Écart F/H réel, conseil, même méthode | Écart > 7,2 % | ≤ 5 % [proposed], seuil de la directive pour l'évaluation conjointe, à confirmer par un juriste | DRH | Recalcul à 12 mois |
| E2 | Départs volontaires niveaux 3–5 | Taux > celui des 12 mois précédents | Taux inférieur [proposed] | DRH | 12 mois |
| E10 | Ressenti (Subjective Value Inventory, 4 dimensions) | Une dimension sous le seuil [proposed] pour une partie | Toutes les dimensions ≥ cible [proposed], sans dimension très en retrait | DRH | Après la NAO, chaque partie séparément |

## Cahier de recette / Acceptance plan
Seuils [proposed] à confirmer par le DRH. Les lignes marquées « DRH » exigent de voir des salaires individuels.

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 – Complétude | Compter les cellules niveau × famille | 36 cellules : chacune a min, médiane, max, ou porte « non applicable » avec motif | mécanique | Script ; DRH |
| 2 | E14 – Ordre interne | Tester chaque cellule | min < médiane < max dans 36/36 cellules | mécanique | Script ; DRH |
| 3 | E14 – Progression | Tester chaque famille, niveau n → n+1 | min, médiane et max strictement croissants | mécanique | Script ; DRH |
| 4 | E2, E14 – Écart de médianes | Calculer médiane(n+1)/médiane(n) pour chaque famille | ≥ 1,05 [proposed] pour tous les niveaux adjacents | mécanique | Script ; DRH |
| 5 | E13 – Minima conventionnels | Comparer le min de chaque cellule au minimum de la position rattachée, en base ETP | 36/36 cellules ≥ minimum Syntec en vigueur à la date d'effet | mécanique | Script ; juriste (données agrégées) |
| 6 | E13 – Rattachement | Contrôler la table des 9 niveaux vers les positions Syntec contre le texte de la convention cité | Chaque rattachement a une référence au texte, sans écart | relecture | Juriste droit social ; aucune donnée individuelle |
| 7 | E11 – Sourçage des médianes | Pour chaque médiane : source, percentile, taille d'échantillon, date | Champs renseignés pour 36/36 ; écart à la médiane marché ≤ ±5 % [proposed] ou justifié par écrit | mécanique | Script ; DRH |
| 8 | E11 – Pertinence du benchmark | Lire l'étude du cabinet : échantillon (secteur ESN, taille, zone), table de correspondance de ses métiers vers nos familles | Correspondance écrite pour les 4 familles ; limites de l'échantillon énoncées | relecture | DRH ; données de marché seulement |
| 9 | E11 – Données sources | Rapprocher l'export du 30/09 des effectifs ; contrôler les doublons de matricule | Lignes = effectif (140), ou écart expliqué ligne à ligne ; 0 matricule en double ; ETP renseigné partout | mécanique | Script ; DRH |
| 10 | E3 – Reproduction du constat | Recompter sur l'export, avec l'ancienne grille, les salariés hors fourchette | 19 au-dessus du max et 6 sous le min retrouvés, ou écart expliqué | mécanique | Script ; DRH |
| 11 | E3 – Traitement individuel | Lister les cas hors fourchette sous la nouvelle grille, un traitement par matricule | Chaque cas a un code de traitement et une justification ; nombre de traitements = nombre de cas | mécanique | Script ; DRH |
| 12 | E3 – Sous le minimum | Compter les salariés sous le min de leur cellule après mise en grille | 0 à la date d'effet | mécanique | Script ; DRH |
| 13 | E3 – Aucune baisse | Comparer fixe après et fixe avant, ligne par ligne | fixe après ≥ fixe avant pour 100 % des lignes | mécanique | Script ; DRH |
| 14 | E3 – Niveaux inchangés | Comparer le niveau de l'export au niveau de la simulation | Tout changement de niveau est listé avec sa décision de promotion ; 0 changement non listé | mécanique | Script ; DRH |
| 15 | E3 – Règle au-dessus du max | Lire la règle : durée du gel ou du traitement, base légale | Horizon daté ; aucune baisse de salaire sans accord ; coût indiqué | relecture | Juriste droit social ; DRH |
| 16 | E2 – Inversions niveaux 3–5 | Compter les paires où un salarié de niveau inférieur ou moins ancien gagne ≥ un salarié de niveau supérieur ou plus ancien, par famille, avant puis après | Nombre après < nombre avant ; ≤ cible fixée par le DRH | mécanique | Script ; DRH |
| 17 | E2 – Cas cités | Suivre les matricules des confirmés de 2025 et des seniors de six ans cités dans le constat | Fixe du senior ≥ fixe du confirmé + 5 % [proposed] après mise en grille | mécanique | Script ; DRH |
| 18 | E7 – Montant de l'enveloppe | Recalculer 3,2 % × 8 900 000 | 284 800 €, identique dans la feuille et dans les deux notes | mécanique | Script (calc-check) |
| 19 | E7 – Coût en année pleine | Sommer mises en grille + augmentations individuelles, chargées | ≤ 284 800 € | mécanique | Script ; DRH |
| 20 | E7 – Coût de l'exercice | Chercher le coût de l'exercice et la date d'effet | Les deux sont présents ; la note dit lequel est comparé au 3,2 % | mécanique | Script ; DRH |
| 21 | E7 – Coefficient de charges | Comparer le coefficient aux bulletins ou à la paie | Coefficient sourcé et daté, écart au réel ≤ 2 % [proposed] ou expliqué | relecture | Gestionnaire de paie ; DRH |
| 22 | E7 – Rapprochement | Comparer la somme des augmentations individuelles au total des tableaux de synthèse | Écart ≤ 1 € | mécanique | Script ; DRH |
| 23 | E9 – Répartition | Sommer les parts (grille, individuel, écart F/H, compression) par famille et niveau | Somme des parts = total, à 1 € près | mécanique | Script ; DRH |
| 24 | E8 – Temps partiel | Prendre toutes les lignes avec temps < 1 ; comparer à la grille sur base ETP, augmentation au prorata | 100 % des lignes à temps partiel traitées en ETP, aucune comparée en brut | mécanique | Script ; DRH |
| 25 | E4 – Reproduction du 7,2 % | Recalculer l'écart conseil à niveau égal depuis l'export | 7,2 % ± 0,1 pt, ou écart de méthode expliqué | mécanique | Script ; DRH |
| 26 | E4 – Méthode écrite | Lire la méthode : moyenne ou médiane, ETP, fixe ou fixe+variable, pondération | Chaque choix est écrit et justifié | relecture | Juriste ou statisticien ; données agrégées |
| 27 | E4 – Petits effectifs | Chercher les cellules avec moins de 5 personnes d'un sexe (seuil [proposed]) | 0 chiffre affiché pour ces cellules (« non significatif ») | mécanique | Script ; DRH |
| 28 | E4 – Écart simulé après plan | Recalculer l'écart conseil après mise en grille, même méthode | ≤ cible fixée par le DRH (5 % [proposed]), jamais > 7,2 % | mécanique | Script ; DRH |
| 29 | E4 – Écart expliqué ou non | Lire la décomposition par facteurs | Chaque facteur est objectif et neutre du point de vue du genre ; l'écart résiduel est chiffré | relecture | Juriste droit social ; données agrégées |
| 30 | E4 – Attribution des corrections | Lire la règle d'attribution des correctifs F/H | Règle écrite, applicable à tous, sur critère de position ; pas de critère direct de sexe | relecture | Juriste droit social |
| 31 | E5 – Une fiche par passage | Compter les passages n → n+1 | 8 passages, chacun avec ≥ 1 critère | mécanique | Script ; RRH exclue (auteur) |
| 32 | E5 – Critères observables | Lire chaque critère | Chaque critère renvoie à un fait, un livrable ou une durée vérifiable | relecture | Manager hors RH |
| 33 | E5 – Pas de critère « attendre » | Lire chaque passage | Aucun passage ne s'obtient par la seule ancienneté | relecture | DRH |
| 34 | E5 – Application à l'aveugle | 10 profils pseudonymisés, 2 lecteurs indépendants appliquent les critères | Accord sur le niveau ≥ 80 % [proposed] | relecture | Un manager hors RH + le DRH |
| 35 | E5 – Neutralité | Lire les critères : temps partiel, congés parentaux, absences | Aucun critère ne pénalise le temps partiel ni un congé parental | relecture | Juriste droit social |
| 36 | E8 – Règles déterminées | 10 cas types dont 2 limites (au min, au max) | Chaque cas aboutit à un seul résultat, identique pour deux lecteurs | relecture | Manager hors RH |
| 37 | E8 – Règles rejouées | Rejouer les règles avec un script indépendant de la feuille | Salaire proposé = résultat des règles pour 100 % des lignes hors exceptions listées | mécanique | Script, hors espace de l'agent ; DRH |
| 38 | E8 – Exceptions | Compter les lignes où le proposé ≠ la règle | ≤ 7 [proposed], chacune justifiée par écrit | mécanique | Script ; DRH |
| 39 | E6 – Fourchettes dans les offres | Lire un exemple d'annonce par famille | La fourchette du niveau visé est lisible, brute annuelle, avec son périmètre (fixe seul ou non) | relecture | Juriste droit social |
| 40 | E6 – Droit à l'information | Faire tourner la procédure sur une demande test par famille | Elle produit la rémunération moyenne par sexe pour la catégorie, avec le seuil de petits effectifs appliqué | mécanique | Script ; DRH |
| 41 | E6 – Travail de valeur égale | Lire la correspondance cellules → catégories de valeur égale | Critères de la directive cités (compétences, effort, responsabilités, conditions) pour chaque regroupement entre familles | relecture | Juriste droit social |
| 42 | E6 – Écarts par catégorie | Calculer l'écart F/H par catégorie | Catégories avec écart > 5 % non justifié listées, 0 omise | mécanique | Script ; DRH |
| 43 | E10 – Chiffres des notes | Extraire tous les chiffres des deux notes ; les rapprocher de la feuille | 0 écart | mécanique | Script ; RRH exclue (auteur) |
| 44 | E10 – Aucun trou | Chercher « [à compléter] », TODO, TBD, XXX, lorem, #REF!, #N/A, #DIV/0!, champs vides, dans les PDF ou documents rendus (CODIR et CSE) et dans tous les onglets | 0 occurrence | mécanique | Script ; RRH exclue (auteur) |
| 45 | E10 – Éléments cités | Vérifier chaque annexe, onglet, source, article cité | 100 % existent ; 0 lien externe ; 0 onglet caché non décrit | mécanique | Script ; DRH |
| 46 | E10 – Note CODIR | Lire la note : décision demandée, ≥ 2 options de répartition de l'enveloppe, coût et gagnants/perdants de chacune | Les trois éléments sont présents pour chaque option | relecture | DRH |
| 47 | E10 – Note CSE | Faire lire la note à une personne non RH, qui reformule | Elle restitue en ses mots le fonctionnement de la grille, comment monter de niveau, et ce que ça coûte | relecture | Manager hors RH ; version CSE sans salaire |
| 48 | E10 – Limites déclarées | Lire la note : date des données, hypothèses, limites du benchmark | Limites énoncées, aucune hypothèse tacite | relecture | DRH |
| 49 | E12 – Version CSE | Chercher matricules, salaires individuels, métadonnées (auteur, commentaires, lignes masquées, modifications suivies) | 0 occurrence | mécanique | Script ; DRH |
| 50 | E12 – Accès | Lister les comptes ayant accès aux fichiers de salaires | Exactement 3 comptes, ceux de la RRH, de l'analyste et du DRH | mécanique | DRH + administrateur système |
| 51 | E12 – Données et agent | Lire le traitement des données par l'agent : fichier pseudonymisé, hébergement, conservation, réutilisation | Données transmises sans nom ni date de naissance ; conditions de l'outil écrites ; pas de réutilisation | relecture | DPO ou DRH |
| 52 | Négo – Mandat | Lire le mandat : poids des enjeux, plancher, cible, concession maximale (dont enveloppe > 3,2 % ou non) | Signé et daté avant la 1re séance de NAO | relecture | Direction (porteur du mandat) |
| 53 | Négo – Grille d'évaluation | Recalculer les poids (somme 100 par partie) et les scores | Somme = 100 ; arithmétique exacte | mécanique | Script (calc-check) |
| 54 | Négo – Gabarit du CSE | Lire le gabarit estimé du CSE | Chaque poids est marqué « estimation » avec sa base (demandes, PV de NAO passées) | relecture | DRH |
| 55 | Négo – Repli | Lire la valorisation du repli (désaccord en NAO, retard de conformité, départs, contentieux) | Valorisé, sources et coûts cités ; repli du CSE estimé et marqué comme tel | relecture | DRH |
| 56 | Négo – Paquets scorés | Compter les options et paquets de répartition | Chacun a un score pour la direction et pour le CSE | mécanique | Script |
| 57 | Négo – Au-dessus de notre repli | Comparer le score de l'accord visé au repli | Score > repli | mécanique | Script |
| 58 | Négo – Au-dessus du repli du CSE | Lire l'argument | Score > repli estimé du CSE, ou le plan dit pourquoi il accepterait moins | relecture | DRH |
| 59 | Négo – Non-dominance | Énumérer les paquets de répartition | Aucun paquet n'est meilleur pour une partie et pire pour aucune | mécanique | Script |
| 60 | Négo – Règle de partage | Lire la règle choisie (Nash ou maximin) et le seuil pour la partie la moins servie | Règle et seuil écrits dans le mandat avant la 1re offre | relecture | Direction |
| 61 | Négo – Seuil respecté | Comparer l'accord visé au seuil | Seuil respecté | mécanique | Script |
| 62 | Négo – Plan de concession | Lire ce qui peut être cédé sans dépasser 284 800 € et ce qui exige une extension | Liste des deux catégories, avec coût et ordre | relecture | Direction |
| 63 | Négo – Parties non représentées | Lire la liste des parties concernées sans être à la table (futurs embauchés, salariés au-dessus du max, temps partiel, fonctions centrales…), ce que le plan leur coûte ou donne | Liste, effet par partie, relecture par un tiers sans enjeu | relecture | Juriste ou expert externe |
| 64 | E10 – Décision CODIR | Constater la décision | Dans la zone (voir issue) | terrain | DRH, au CODIR |
| 65 | E5, E7 – NAO | Constater le déroulé et le résultat | Dans la zone | terrain | DRH, à la clôture de la NAO |
| 66 | E10 – Ressenti | Passer le questionnaire sur 4 dimensions à chaque partie, séparément | Chaque dimension dans la zone ; aucune très en retrait | terrain | DRH ; réponses non partagées avec l'autre partie |
| 67 | E7 – Application | Contrôler la paie à 6 et 12 mois : textes publiés, augmentations versées | Appliqué tel qu'écrit ; 0 sous le min | terrain | Gestionnaire de paie + DRH |
| 68 | E7 – Coût réel | Comparer le coût payé à 12 mois à l'enveloppe | ≤ 284 800 € | terrain | Paie + DRH |
| 69 | E4 – Écart réel | Recalculer l'écart conseil à 12 mois, même méthode | Dans la zone | terrain | DRH |
| 70 | E2 – Départs | Compter les départs volontaires niveaux 3–5 sur 12 mois | Dans la zone | terrain | DRH |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Le coût tient dans 284 800 € parce que les charges, le variable ou l'effet année pleine sont omis, ou parce que la masse de 8,9 M€ ne correspond pas à la paie → lignes 19, 20, 21, 22, H3, H12.
- Les 6 sous le minimum disparaissent parce qu'on les a reclassés à un autre niveau, ou que le min a été abaissé → lignes 14, 12, H6.
- Les totaux tombent juste parce qu'ils sont collés en valeurs dans la feuille, sans formules → H1, 22, 43.
- L'écart F/H passe sous 5 % grâce à une méthode choisie pour cela (moyenne au lieu de médiane, variable exclu, ETP ignoré), pas parce que les salaires ont changé → lignes 25, 26, 28, H4.
- Chaque passage de niveau a des critères, mais le critère réel est « attendre N ans » ou un mot vague (« autonomie ») → lignes 32, 33, 34, H8.
- La note CSE affiche des fourchettes agrégées, mais un petit effectif permet de retrouver un salaire (ex. conseil, niveau 5, 2 personnes) → lignes 27, 49, H10.
- Les règles de positionnement sont écrites, mais la feuille contient des ajustements à la main que les règles ne reproduisent pas → lignes 37, 38, H2.
- L'accord visé est bon pour la direction et le CSE mais coûte à des absents : futurs embauchés, salariés gelés au-dessus du max → ligne 63.
- Les notes sont complètes dans le fichier source, mais le PDF rendu contient des trous ou des #REF! → lignes 44, H9.

## Non testable en l'état / Not testable as stated
- E6 (directive) – « se préparer » n'a pas de livrable défini. Question : quels livrables précis (modèle d'annonce, procédure de demande d'information, premier calcul d'écarts) sont attendus pour janvier ? Le statut de la transposition française est à confirmer par un juriste.
- E7 (variable) – on ne sait pas si les fourchettes et la masse de 8,9 M€ portent sur le fixe seul ou sur fixe + variable. Les lignes 19 et 21 ne sont testables qu'une fois ce choix fait.
- E7 (base du 3,2 %) – le 3,2 % s'applique-t-il au coût annuel ou au coût de l'exercice ?
- E2 – « compression résorbée » n'a pas de seuil donné. Le DRH doit confirmer ou remplacer les seuils [proposed] des lignes 4, 16 et 17.

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 38 | 9 | Script, lancé par le DRH hors espace de l'agent |
| relecture | 25 | 6 | Juriste droit social, manager hors RH, gestionnaire de paie, DPO, direction, DRH |
| terrain | 7 | 0 | DRH, paie, à la date d'effet, à 6 et 12 mois |

Une boucle peut clore les calculs, la complétude et la cohérence : 47 lignes sur 85, soit environ 55 %. Elle ne dit rien de l'issue : accord en NAO, ressenti, effets à 12 mois. Les lignes juridiques et de pertinence exigent un relecteur. Les lignes qui exigent de voir des salaires individuels ne peuvent être vérifiées que par le DRH (voir Questions ouvertes).

## Critère d'arrêt de la boucle / Loop stopping criterion
- **La boucle s'arrête** quand toutes les lignes mécaniques visibles passent, et que les lignes mécaniques cachées, lancées par le DRH hors de l'espace de l'agent, passent aussi. Le rapport de l'agent ne suffit jamais.
- **La boucle ne décide pas** des lignes de relecture ni de terrain. Elles vont au juge après la boucle. En cas d'échec, l'agent reçoit le numéro de l'exigence, jamais le test caché.
- **L'instrument de mesure est protégé** :
  - le DRH détient la somme de contrôle du fichier d'export du 30/09, des scripts de test et des paramètres ;
  - aucun test n'est ignoré ni marqué comme attendu en échec ;
  - la feuille est paramétrée par formules, sans valeurs collées ;
  - le périmètre de lignes de l'export ne change pas.
- **Retour en cas d'échec** : numéro d'exigence et symptôme visible, sans valeur attendue ni donnée de test.

## Questions ouvertes / Open questions
1. Base de la masse de 8,9 M€ (fixe seul ou avec variable) et coefficient de charges.
2. Date d'effet et date du CODIR.
3. Périmètre exact de E6 et statut de la transposition française (voir « Non testable en l'état »). L'effectif de 140 est proche du seuil de 150, qui change la fréquence du rapport sur les écarts : à faire confirmer par un juriste.
4. Qui est le second contrôleur des lignes à salaires ? Seules trois personnes les voient, et deux sont auteures : le DRH est le seul vérificateur indépendant. Le DRH peut-il habiliter une quatrième personne ?
5. Le mandat de négociation autorise-t-il un dépassement de 3,2 % ? Sans cette réponse, les lignes 52, 60 et 62 ne peuvent pas être renseignées.
6. Quel est l'outil d'agent utilisé, et où vont les données ? C'est un risque pour la ligne 51.

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E7 – Totaux sans valeurs collées (garde 22, 43) | Compter les cellules de calcul qui contiennent une constante là où une formule est attendue ; modifier un salaire dans une copie et relancer | 0 constante ; les totaux se recalculent | mécanique | DRH, script |
| H2 | E8 – Règles sur d'autres cas (garde 36, 37) | 12 cas fictifs du juge : au min, au max, à 80 %, promotion qui dépasse le max du nouveau niveau, entrée en cours d'année | Chaque cas donne un seul résultat conforme aux règles écrites | mécanique | DRH |
| H3 | E7 – Coût recalculé autrement (garde 19, 22) | Recalculer le coût ligne par ligne depuis l'export brut, par une autre méthode | Écart ≤ 0,5 % [proposed] sur le total | mécanique | DRH, script |
| H4 | E4 – Écart sous d'autres méthodes (garde 25, 28) | Recalculer l'écart en médiane, en fixe + variable, et par régression avec l'ancienneté | Écart entre méthodes ≤ 1,5 pt [proposed], ou écart expliqué | mécanique | DRH, script |
| H5 | E4 – Facteurs de la décomposition (garde 29) | Lire chaque facteur « explicatif » : est-il lui-même source de discrimination (négociation à l'embauche, disponibilité…) ? | Aucun facteur n'est susceptible de reproduire un biais ; sinon justifié | relecture | Juriste droit social |
| H6 | E3 – Traçage de cas (garde 11, 14) | Tirer au sort 5 des 25 cas hors fourchette ; suivre ligne d'export → décision → feuille → note | Cohérent aux quatre étapes | mécanique | DRH |
| H7 | E2 – Compression sur d'autres paires (garde 16, 17) | Recalculer sur des paires choisies par le juge, en conseil et en développement | Même conclusion que dans la note, sans paire inversée | mécanique | DRH |
| H8 | E5 – Profils construits par le juge (garde 33, 34) | 6 profils dont 3 « ancienneté seule » et 3 « preuves réelles » ; lecteur hors RH | ≥ 5/6 niveaux conformes à l'attendu | relecture | Manager hors RH |
| H9 | E10 – Documents rendus (garde 44, 45) | Ouvrir les PDF et documents rendus sur une machine propre ; chercher trous, erreurs, liens externes, onglets cachés, modifications suivies | 0 occurrence | mécanique | DRH |
| H10 | E12 – Réidentification (garde 49, 27) | Croiser niveau × famille × sexe × tranche d'ancienneté dans la version CSE | 0 individu identifiable | mécanique | DRH |
| H11 | E13 – Échantillon de minima (garde 5, 6) | Choisir 3 cellules et les rapprocher du texte Syntec à la date d'effet | Aucun écart | relecture | Juriste |
| H12 | E7 – Masse de 8,9 M€ (garde 18, 21) | Reconstituer la masse chargée depuis l'export et le coefficient | Écart avec 8,9 M€ ≤ 2 % [proposed], ou expliqué | mécanique | DRH, script |
| H13 | Négo – Contrepartie simulée (garde 52–62) | Donner à un juge ou à `red-team` le gabarit estimé du CSE, sans le plan ; il joue une séance de NAO | Les réponses du plan tiennent sans franchir le plancher | relecture | `red-team` ou juge indépendant |
| H14 | Négo – Trois coups forts anticipés (garde 62) | Comparer les trois meilleurs coups de la contrepartie au plan (ex. demande > 3,2 %, rattrapage général, publication individuelle) | Les trois sont anticipés, ou le plan est amendé | relecture | Même juge |
| H15 | Négo – Cible dominée ? (garde 59) | La contrepartie cherche un paquet qui plaît aux deux parties plus que la cible | Aucun trouvé ; sinon la cible est dominée et le plan est amendé | relecture | Même juge |

Si une ligne cachée échoue, l'auteur apprend quelle exigence a échoué, jamais le test. Un test dont le contenu a fuité est épuisé et doit être remplacé. Les lignes H13 à H15 testent des exigences que l'auteur connaît (la préparation de la NAO) ; elles n'ajoutent aucune exigence nouvelle.