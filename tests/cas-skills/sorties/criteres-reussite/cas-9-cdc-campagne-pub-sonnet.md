<!-- Sortie brute de criteres-reussite 1.0.0 (avec les annexes documents et travaux), Sonnet, 0.17 $, 2 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: document (cahier des charges d'une consultation) + critères de choix d'agence + issue d'une campagne
author: vous et la directrice marketing
judge: comité des franchisés (voir la demande de part cachée en fin de document)
---

# Critères de réussite : CDC de la consultation « campagne de printemps, pains au levain »

## Synthèse / Summary
Il y a trois livrables et trois moments de contrôle. Le **CDC** doit être prêt avant l'envoi aux cinq agences. La **grille de choix** doit départager les réponses. La **campagne** doit avoir marché en juin, ce qui dépend des clients et des boutiques, donc se vise par une zone plancher/cible. Le plan compte **28 lignes visibles : 16 mécaniques, 8 de relecture, 4 de terrain**. Une boucle automatique, c'est-à-dire un script lancé sur le PDF et les tickets, ne peut clore que 16 lignes sur 28.

Pour la partie cachée, vous êtes l'auteur. Je ne l'écris donc pas et je rédige une demande scellée pour le comité (voir plus bas). L'annexe « livrable écrit » n'a pas été consultée, c'est la méthode seule qui s'applique.

Lignes bloquantes : 1, 3, 5, 7, 8, 9, 13, 18, 22.

**Hypothèses que j'ai faites, à corriger si elles sont fausses :**
- Le printemps visé est celui de 2027, puisque nous sommes en octobre 2026.
- Vous êtes `requester: author`.
- Les ventes par boutique sont sensibles pour les franchisés.
- Les données de la carte de fidélité sont des données personnelles et ne circulent que pseudonymisées.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Faire connaître la nouvelle gamme de pains au levain | « faire connaître la nouvelle gamme » | issue |
| E2 | Ramener en boutique les 25-40 ans, qui achètent de plus en plus en grande surface | « ramener en boutique les 25-40 ans » | issue |
| E3 | Budget de 90 k€ HT, création et achat d'espace compris | « Budget : 90 k€ HT » | livrable (CDC, puis réponses) |
| E4 | Campagne de mars à mai | « mars à mai » | livrable |
| E5 | Canaux : affichage local, réseaux sociaux, radio locale « peut-être » | brief | livrable |
| E6 | Moitié du coût payée par les franchisés : dépense justifiable devant eux | « méfiants », cotisation marketing | livrable (transparence) et issue (confiance) |
| E7 | Effet mesurable sur les ventes (2024 : visuels primés, aucun effet mesurable) | « aucun effet mesurable » | livrable (protocole) |
| E8 | Les 38 boutiques, en Bretagne et Pays de la Loire, présentes partout (carte du site, supports) | « boutiques pas sur la carte du site » | livrable |
| E9 | CDC prêt à envoyer à cinq agences | « prêt à envoyer » | livrable |
| E10 | Pouvoir choisir la bonne agence | « choisir la bonne » | livrable (grille) |
| E11 | Dire en juin si la campagne a marché | « en juin » | livrable (rapport) et issue |
| E12 | Le comité des franchisés juge | « c'est le comité qui jugera » | livrable |

## Issue visée / Outcome zone
Les seuils chiffrés ne sont pas dans votre brief et je n'en invente pas. Ils doivent être **fixés par la direction marketing et le comité avant l'envoi du CDC**, pas après les résultats.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E1 | Ventes de la gamme levain, par boutique et par semaine, par rapport à la référence 2022-2026 | Écart non distinguable de zéro, tel que calibré par le test à blanc (ligne 9) | à fixer | direction marketing + comité, avant l'envoi | fin mai, synthèse début juin |
| E2 | Porteurs de carte de 25-40 ans : nouveaux, réactivés, fréquence (30 % des clients seulement) | à fixer | à fixer | idem | idem, plus un point à l'automne |
| E8 | Part des boutiques au-dessus de leur propre référence | à fixer (seuil pour la boutique la moins bien servie) | à fixer | comité | idem |

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E9, CDC tel qu'envoyé | Recherche de « [à compléter] », TODO, TBD, XXX, lorem ipsum, champs vides, dans le **PDF rendu** et chaque annexe, pas dans la source | 0 occurrence | mécanique | quelqu'un d'autre que les rédacteurs, par script |
| 2 | E9, pièces citées | Chaque annexe, tableau ou fichier cité dans le texte est joint et s'ouvre | 100 % des pièces citées présentes | mécanique | idem |
| 3 | E3, budget | Recherche de tous les montants. Recalcul de la décomposition, avec indication de ce que 90 k€ HT inclut : honoraires, production, achat d'espace | Un seul chiffre global dans tout le CDC. Total des postes = 90 k€ HT. Inclusions et exclusions écrites | mécanique | direction financière ou `calc-check` |
| 4 | E4, calendrier | Extraction de toutes les dates : remise des offres, soutenances, choix, création, lancement, fin, rapport | Dates ordonnées, jours ouvrés, année indiquée. Délai entre le choix et le 1er mars [proposé : ≥ 8 semaines] compatible avec l'affichage et la radio | mécanique | quelqu'un d'autre que les rédacteurs |
| 5 | E8, annexe des boutiques | Comptage et rapprochement avec le fichier réseau : nom, adresse, département, région, coordonnées GPS | 38 lignes, aucune manquante, aucune en double, 100 % des lignes complètes | mécanique | responsable réseau |
| 6 | E5, canaux | Pour affichage, réseaux sociaux et radio, le texte dit « imposé », « option chiffrée à part » ou « libre » | Un statut par canal, sans « peut-être » restant | relecture | un franchisé non rédacteur |
| 7 | E1, E2, E11, objectifs | Le CDC contient un tableau référence, plancher, cible, unité, période, source de données | Tous les champs remplis, sans cellule vide | mécanique | script de recherche, valeurs relues par le comité |
| 8 | E7, protocole de mesure | Une personne qui n'a pas écrit le CDC refait le calcul sur un échantillon à partir du texte seul : référence, comparaison, traitement de Pâques, des ruptures de stock et des dates d'arrivée de la gamme par boutique | Elle obtient le même chiffre, sans poser de question aux rédacteurs | relecture | analyste de données ou contrôleur de gestion |
| 9 | E7, test à blanc | Application du protocole à un printemps **sans** campagne, puis au printemps 2024 | Sans campagne : effet non distinguable de zéro. 2024 : verdict chiffré, qui sert à calibrer le plancher | mécanique | analyste, sur les tickets 2022-2026 |
| 10 | E2, définition des 25-40 | Le CDC dit comment les 25-40 sont comptés et ce que vaut ce chiffre, étant donné les 30 % de porteurs de carte | Périmètre écrit : porteurs de carte seulement. Biais nommé. Pas de conclusion sur « tous les 25-40 » | relecture | analyste |
| 11 | E9, confidentialité | Lecture des données remises aux candidats avant le choix | Agrégats seulement. Aucune vente identifiable par franchisé, aucune donnée personnelle | relecture | DPO ou juriste, avec un représentant du comité |
| 12 | E12, lisibilité | Deux membres du comité lisent le CDC et la grille, puis redisent par écrit : ce qu'on demande, comment on choisit, comment on mesurera | Les 3 points sont correctement reformulés, sans aide | terrain | deux franchisés, avant l'envoi |
| 13 | E10, grille | Poids des critères, nombre de niveaux de notation | Somme des poids = 100. Chaque critère a le même nombre de niveaux | mécanique | script |
| 14 | E10, descripteurs | Pour chaque critère, relecture de chaque niveau de note. Contrôle du poids de la création par rapport à la mesure d'effet et à la couverture des 38 boutiques | Chaque niveau décrit un observable, pas « bon » ou « convaincant ». La création ne peut pas compenser seule l'absence de plan de mesure (leçon 2024) | relecture | comité, avec la direction marketing |
| 15 | E10, notation à blanc | Deux évaluateurs notent séparément deux réponses fictives | Écart ≤ 1 point sur l'échelle par critère [proposé] | relecture | deux évaluateurs |
| 16 | E10, égalité de traitement | Questions-réponses, données remises, dates et formats | Les cinq agences ont reçu les mêmes pièces et les mêmes réponses, aux mêmes dates | relecture | quelqu'un d'extérieur à la rédaction |
| 17 | E3, gabarit de prix des réponses | Recalcul du tableau de prix imposé : création, production, achat par canal, honoraires, suivi | Total ≤ 90 k€ HT, postes qui s'additionnent, parts du média et de la création lisibles | mécanique | `calc-check` |
| 18 | E8, couverture des réponses | Rapprochement du plan média de chaque réponse avec l'annexe des 38 boutiques | 38 boutiques sur 38 couvertes, ou l'écart signalé | mécanique | script |
| 19 | E1, ventes de la gamme | Ventes levain par boutique et par semaine, mars-mai, contre la référence | Au-dessus du plancher. Le niveau est comparé à la cible (tableau de la ligne 7) | mécanique | analyste |
| 20 | E2, trafic total | Nombre de tickets et chiffre d'affaires total par boutique | Hausse du total, pas seulement un transfert depuis les autres pains | mécanique | analyste |
| 21 | E2, 25-40 | Porteurs de carte de 25-40 ans : nouveaux, réactivés, fréquence | Au-dessus du plancher, avec la mention « porteurs de carte » (ligne 10) | mécanique | analyste, données pseudonymisées |
| 22 | E8, carte et supports | Avant le lancement, puis en semaine 1 : script sur la carte du site, avec adresses et liens, et sur les supports géolocalisés | 38 boutiques sur 38 affichées, au bon endroit | mécanique | script, puis un tiers sur 3 boutiques tirées au sort |
| 23 | E8, répartition | Résultats boutique par boutique | Nombre de boutiques sous leur référence et écart de la moins bien servie, comparés au seuil fixé | mécanique | analyste |
| 24 | E3, E6, dépense réelle | Factures des agences contre le plan | Total ≤ 90 k€ HT, détail par poste, écarts justifiés | mécanique | direction financière |
| 25 | E6, preuves de diffusion | Photos ou relevés d'affichage, certificats de passage radio, rapports des réseaux sociaux, rapprochés du plan | Chaque poste facturé a une preuve datée et localisée | relecture | un franchisé et un contrôleur |
| 26 | E1, notoriété | Enquête avant et après auprès des 25-40 ans de la zone (si le comité la finance) | Hausse de la connaissance spontanée de la gamme au-dessus du seuil fixé | terrain | institut ou équipe d'étude |
| 27 | E2, durée de l'effet | Mêmes indicateurs que les lignes 19 à 21, fin juin, puis à 3 mois | Pas de retour à la référence dès l'arrêt (ou l'effet est qualifié d'un pic) | terrain | analyste |
| 28 | E11, E12, restitution | Remise du rapport de juin au comité, avec une page par boutique | Date tenue. Chaque franchisé retrouve ses chiffres. Le comité peut dire si les seuils sont atteints, sans nouvelle analyse | terrain | comité |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Un CDC propre et complet, mais sans protocole refaisable par un tiers. Le résultat de juin est alors indiscutable… ou invérifiable → lignes 8, 9.
- Les ventes montent parce que Pâques tombe fin mars et que le printemps est un pic saisonnier, pas à cause de la campagne → lignes 9, 19.
- Les ventes de levain montent aux dépens des autres pains, sans plus de clients → ligne 20.
- Le chiffre 25-40 est mesuré sur les 30 % de porteurs de carte. Il ne dit rien sur les autres clients ni sur les clients qui n'ont pas la carte → lignes 10, 21.
- La carte du site affiche « 38 pastilles », mais certaines sont mal placées, sans horaires, ou renvoient vers la mauvaise boutique → lignes 5, 22.
- La moyenne est positive mais portée par quelques grosses boutiques, les autres n'ont rien vu → ligne 23.
- Une réponse à 89 k€ HT dont 70 % de création et 10 % de média coche toutes les cases de la grille → lignes 14, 17 (la répartition acceptable création/média est une question ouverte).
- La grille a des poids qui s'additionnent à 100 mais ne départage rien : tout le monde a 3 sur 5 → lignes 14, 15 (et part cachée).
- Un montant ou une dimension fausse dans une annexe, que la recherche faite sur le seul document principal ne voit pas → lignes 1, 2, 3.

## Non testable en l'état / Not testable as stated
- E1 « faire connaître » : sans mesure de notoriété avant, on ne peut pas dire de combien. Question : finance-t-on une enquête avant/après (ligne 26), ou la notoriété est-elle jugée uniquement par les ventes de la gamme ?
- E11 « a marché » : tant que plancher et cible ne sont pas fixés, la ligne 7 ne peut pas être décidée. Question : qui les fixe, et à quelle date avant l'envoi ?
- E10 « la bonne agence » : « bonne » n'est pas défini. Question : quels critères pèsent le plus pour le comité : effet attendu, couverture des 38 boutiques, prix, capacité de mesure, références ?
- E6 « méfiants » : ce n'est pas une exigence testable en soi. Je l'ai traduit en lignes 24, 25, 28.

## Couverture / Coverage
| Preuve | Visible | Caché | Qui |
|---|---|---|---|
| mécanique | 16 | à écrire par le juge | script, lancé par quelqu'un d'autre que les rédacteurs |
| relecture | 8 | idem | analyste, DPO, franchisé, comité |
| terrain | 4 | idem | franchisés avant l'envoi ; analyste et comité en juin et à l'automne |

Une vérification automatique peut clore les lignes 1 à 5, 7, 9, 13, 17 à 24 : le CDC, les prix et les résultats. Elle ne dit rien de la qualité de l'idée, de la clarté du texte pour le comité, ni de la confiance des franchisés. Et surtout, elle ne prouve pas que l'effet vient de la campagne si le protocole est mal conçu : tout dépend de la ligne 9.

## Questions ouvertes / Open questions
1. Les tickets identifient-ils les produits de la gamme levain ? Depuis quelle date chaque boutique la vend-elle ?
2. La carte de fidélité contient-elle l'âge ou la date de naissance ?
3. Peut-on garder quelques boutiques ou zones comme témoin, ou décaler le démarrage, pour avoir une comparaison ? Sans cela, l'effet se lit seulement contre le passé.
4. Le plancher et la cible : qui les fixe, et avant quelle date ?
5. Les 90 k€ HT incluent-ils les honoraires et la production ? Les 45 k€ des franchisés font-ils l'objet d'un suivi comptable séparé ?
6. Quelle part minimale de média, ou maximale de création, le comité accepte-t-il ?
7. La radio : dedans, en option chiffrée, ou dehors ?
8. Qui est le « quelqu'un d'autre » qui lance les scripts (lignes 1 à 5, 22) ?

✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Requirements to guard: E1, E2, E3, E7, E8, E10. About 6 lines, at least one per requirement listed. Comme le CDC et sa grille seront publiés aux agences, la partie cachée teste la **grille**, pas le travail des agences. Elle doit contenir en particulier des réponses fictives qui cochent toutes les cases sans servir le besoin et qui ne doivent pas gagner.

Judge (comité des franchisés, ou la personne qu'il désigne) : lancez `criteres-reussite` avec `requester: judge`, ce brief et le plan visible ci-dessus, et gardez pour vous ce qu'il écrit. Ne le transmettez ni à la direction marketing ni aux rédacteurs.