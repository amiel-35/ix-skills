<!-- Sortie brute de cahier-de-recette 1.0.0 (brouillon du 2026-10-17, avant ajustements), Sonnet, 0.36 $, 4 min. Cas : ../../cahier-de-recette.md -->

# Cahier de recette: préparation de la renégociation du contrat (éditeur SaaS de planification de tournées × ETI logistique)

J'ai appliqué la méthode du skill et l'annexe négociation, qui était disponible. Aucun chiffre de la partie cachée n'apparaît dans le bloc visible, que vous pouvez donc transmettre tel quel à vos deux auteurs. Il y a trois points à lire avant le plan.

1. Date de préavis. Le préavis courait jusqu'au 30/09/2026 et nous sommes le 17/10/2026. Le client a « ouvert une consultation » sans dénoncer formellement. Ce que cela change dépend du texte de la clause de reconduction, que je n'ai pas lu. La ligne 33 le fait établir par un juriste.
2. Écart de prix. La demande de −12 % donne 163,7 k€/an. Votre plancher de 170 k€ est au-dessus, avec un écart de 6,3 k€/an. Le prix seul ne se recoupe donc pas, et l'accord se joue sur le reste du paquet (SLA, durée, module, périmètre). Les lignes 14 et 15 l'exigent.
3. Le plancher de 170 k€ n'est pas votre repli. Perdre le compte coûterait au moins 98 k€/an de contribution, car 170 − 72 = 98. Ce plancher est donc une préférence de la direction, pas un seuil sous lequel vous préféreriez partir. Le CEO doit le savoir en le signant (ligne 4).

---
status: draft
skill: cahier-de-recette
deliverable_kind: négociation (dossier de préparation, puis accord, puis suivi à 6 et 12 mois)
author: directeur commercial + demandeur
judge: CEO (n'a pas participé au compte), détenteur de la part cachée
---

## Synthèse / Summary
Le livrable est un dossier de préparation (mandat, intérêts des deux côtés, replis, plan de concessions, scénarios). « Prêt » veut dire que toutes les lignes mécaniques passent, que les lignes de relecture sont signées par des personnes nommées, et que le CEO a fait jouer le client simulé (part cachée) sans que le plan franchisse le plancher. « Bon accord » veut dire un accord dans la zone plancher/cible fixée avant la première offre, puis tenu, appliqué et ressenti comme correct à 6 et 12 mois.

Le plan compte 61 lignes visibles (26 mécanique, 24 relecture, 11 terrain) et 11 lignes cachées. Un script règle environ 43 % des lignes, soit l'arithmétique et la complétude, mais pas la qualité de l'accord. Question principale ouverte : les planchers de durée et de SLA/plafond de pénalités ne sont pas dans votre note.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Mandat signé par le CEO | « mandat signé par notre CEO » | livrable |
| E2 | Analyse des intérêts des deux côtés (dont acteurs côté client) | « analyse des intérêts des deux côtés » | livrable |
| E3 | Solutions de repli valorisées, les nôtres et celles du client | « solutions de repli » | livrable |
| E4 | Plan de concessions | « plan de concessions » | livrable |
| E5 | Scénarios | « scénarios » | livrable |
| E6 | Savoir quand le dossier est prêt | « savoir quand le dossier sera prêt » | livrable |
| E7 | Conserver au moins 170 k€/an | « au minimum garder 170 k€/an » | issue |
| E8 | Idéalement 3 ans de plus avec indexation Syntec | « idéalement passer à 3 ans de plus avec l'indexation Syntec » | issue |
| E9 | Vendre le module d'optimisation dynamique (38 k€/an) | « vendre le module… 38 k€/an » | issue |
| E10 | Savoir à 6 et 12 mois si l'accord était bon, pas seulement signé | « dans six mois et dans un an… » | issue |
| E11 | Traiter la demande −12 % et SLA 99,9 % avec pénalités | contexte (DAF) | livrable (réponse) / issue |
| E12 | Traiter la baisse d'usage à Valence et Orléans | contexte (−40 %) | livrable / issue |
| E13 | Établir le statut juridique de la reconduction et du courrier du 12/09 | [inféré] préavis passé le 30/09, pas de dénonciation formelle | livrable |
| E14 | Parties affectées et absentes de la table | [inféré] | livrable |
| E15 | Confidentialité du mandat et des coûts | [inféré] | livrable |
| E16 | Calendrier jusqu'à la 1re réunion de novembre | « on négocie en novembre » | livrable |
| E17 | Connaître le nouveau directeur des opérations | [inféré] sponsor parti en mai | livrable |

## Issue visée / Outcome zone
Les planchers sont fixés par le CEO avant la première offre, pas par les auteurs.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E7 | Prix annuel HT, toutes lignes | 170 k€/an (note). À préciser : module inclus ou non | 186 k€ de base + 38 k€ de module = 224 k€/an avant indexation [dérivé, suppose la base maintenue] | CEO | à la signature |
| E8 | Durée / indexation | durée plancher **non fournie, à fixer** | 3 ans de plus, soit jusqu'au 31/03/2030 [dérivé], avec indexation Syntec | CEO | à la signature |
| E11 | SLA et pénalités | niveau et plafond de pénalités **non fournis, à fixer** (contractuel 99,5 %, réel 99,7 %, demandé 99,9 %) | **à fixer** | CEO + CTO | à la signature, puis chaque mois |
| E9 | Module 38 k€/an | pas un plancher, à confirmer par le CEO | module vendu | CEO | signature, puis 12 mois |
| E12 | Usage Valence/Orléans (connexions) | pas de baisse supplémentaire à 6 mois | ≥ 80 % du niveau de janvier 2026 à 12 mois [proposé] | CEO | 6 et 12 mois |
| E10 | Contribution réalisée du compte | ≥ 98 k€/an (170 − 72) [dérivé] | ≥ 114 k€/an, soit la contribution actuelle (186 − 72) [dérivé] | CEO + finance | 12 mois |
| E10 | Valeur subjective (SVI), chaque partie, 4 dimensions | ≥ 4 par dimension [proposé] | ≥ 5 par dimension [proposé] | CEO | à 2 semaines après la signature |
| E10 | Durabilité | ni résiliation, ni litige, ni renégociation forcée | le client ne lance pas d'appel d'offres avant l'échéance | CEO | 6 et 12 mois |

Les mesures à 6 et 12 mois partent de l'entrée en vigueur des nouvelles conditions [proposé], soit environ le 01/10/2027 et le 01/04/2028 si elles démarrent le 01/04/2027. Elles ne partent pas de la signature : signé en novembre, le « 6 mois » tomberait un mois après le début du nouveau terme.

## Cahier de recette / Acceptance plan
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 — Mandat | Ouvrir le mandat signé | Signature du CEO, datée avant toute offre ou réunion de novembre | relecture | CEO |
| 2 | E7-E11 — Planchers | Lire la section planchers du mandat | Un nombre avec unité pour : prix annuel, durée, niveau de SLA, plafond de pénalités, périmètre (sièges) | relecture | CEO |
| 3 | E7 — Planchers inchangés | Comparer les planchers du mandat signé à toutes les versions du dossier | Valeurs identiques, ou révision datée et signée du CEO avec motif | mécanique | script/diff du juge |
| 4 | E7 — Plancher 170 k€ vs repli | Lire la justification du plancher | Le mandat chiffre la contribution perdue si le compte part (prix − 72 k€ de coût de service, soit 114 k€ au prix actuel). Il dit si 170 k€ est un seuil de départ ou une préférence | relecture | CEO + finance |
| 5 | E7 — Règle de partage | Lire le mandat | Règle nommée (Nash ou maximin, Rawls signalé comme analogie) et seuil écrit pour la partie la moins servie | relecture | CEO |
| 6 | E8 — Cible prix et durée | Lire la section cibles | Cible chiffrée (prix, durée) pour chaque enjeu | relecture | CEO |
| 7 | E8 — Indexation Syntec | Lire la définition | Indice, mois de base, date de révision et éventuel plafond écrits. Exemple chiffré sur 3 ans | relecture | finance + juriste |
| 8 | E9 — Module | Lire la fiche module | Prix, périmètre (entrepôts), conditions. Le mandat dit si l'accord tient sans le module | relecture | CEO |
| 9 | E2 — Grille de scoring (nous) | Vérifier la signature | Enjeux, options, poids signés par le CEO avant la 1re offre | relecture | CEO |
| 10 | E2 — Arithmétique de la grille | Recalculer | Poids = 100 par partie, scores dans l'échelle, totaux exacts | mécanique | `calc-check` / script |
| 11 | E2 — Grille du client | Lire l'analyse | ≥ 3 acteurs clients distincts [proposé] (DAF, nouveau directeur des opérations, responsables Valence/Orléans). Chaque poids marqué estimation avec sa base | relecture | responsable du compte non auteur + CEO |
| 12 | E2 — Complétude | Parcourir la grille | Aucune cellule vide : chaque option a un score pour chaque partie | mécanique | script |
| 13 | E2 — Enjeux liés | Lire la méthode de scoring | Prix, durée, SLA, module et sièges sont scorés en paquets, pas additivement | relecture | finance, non auteur |
| 14 | E11 — Demande −12 % | Recalculer | 163,7 k€/an. Écart au plancher 6,3 k€/an, soit 19 k€ sur 3 ans | mécanique | `calc-check` |
| 15 | E11 — Zone d'accord | Chercher dans la grille | ≥ 1 paquet où les deux parties sont au-dessus de leur repli, alors que le prix seul ne se recoupe pas | mécanique | script sur grille |
| 16 | E11 — Exposition SLA | Recalculer depuis l'export mensuel de supervision (12 mois) | Mois sous 99,9 % comptés, pénalité mois par mois par schéma, total vs plafond | mécanique | script, export tiré par le CTO |
| 17 | E11 — Définition SLA | Lire les schémas | Chacun précise ce qui compte comme indisponibilité (maintenance, force majeure, fournisseur cloud, cause client) | relecture | CTO / hébergement |
| 18 | E12 — Usage | Recalculer depuis l'export de connexions | Connexions mensuelles par entrepôt, −40 % Valence/Orléans retrouvé. Utilisateurs actifs vs 420 sièges | mécanique | script |
| 19 | E12 — Cause du maintien d'Excel | Lire l'analyse | Cause étayée (entretien, ticket, courriel), pas supposée | relecture | support / CS |
| 20 | E2 — Pilote Lyon | Lire la source | Document, période, référence de départ, qui a mesuré, validé ou non par le client, pour −9 % de km | relecture | CS / exploitation |
| 21 | E17 — Nouveau directeur des opérations | Lire la section | Ce qu'on sait et ne sait pas de ses priorités. Qui le rencontre, quand, avant la 1re réunion | relecture | CEO |
| 22 | E3 — Repli, perte du compte | Lire la valorisation | Revenu et contribution perdus sur 3 ans, effet sur les 14 % du récurrent, coûts qui ne baissent pas, méthode du 72 k€ (direct ou réparti) | relecture | finance + CEO |
| 23 | E3 — Repli du client, arithmétique | Recalculer | 3×(150 à 170) + (60 à 90) = 510 à 600 k€ vs notre offre sur le même horizon | mécanique | `calc-check` |
| 24 | E3 — Estimation concurrent | Lire les sources | Origine des 150-170 k€ et 60-90 k€, marqués estimation. Facteurs non prix traités (intégration WMS, risque de migration, délai vs 31/03/2027) | relecture | commercial non auteur + CEO |
| 25 | E3 — Autres replis | Lire | ≥ 2 replis [proposé] hors perte du compte, chacun valorisé avec son déclencheur | relecture | CEO |
| 26 | E3 — Paquets plancher et cible vs notre repli | Scorer | Les deux paquets au-dessus de notre repli | mécanique | script sur grille |
| 27 | E3 — Paquets vs repli du client | Lire | Au-dessus de son repli estimé, ou le plan dit pourquoi il accepterait en dessous | relecture | relecteur hors compte |
| 28 | E4 — Concessions | Parcourir le tableau | Chaque ligne : ce qu'on donne, coût €/an, valeur estimée pour le client, contrepartie demandée, rang. Aucun champ vide | mécanique | script |
| 29 | E4 — Séquence | Rejouer les concessions dans l'ordre prévu | Score cumulé jamais sous le paquet plancher | mécanique | script sur grille |
| 30 | E4 — Pareto | Énumérer les paquets | Aucun paquet ne domine le paquet cible | mécanique | script sur grille |
| 31 | E4 — Partie la moins servie | Scorer le paquet cible | Seuil de la ligne 5 respecté | mécanique | script sur grille |
| 32 | E5 — Scénarios | Lire | ≥ 3 [proposé], dont : le client part chez le concurrent, il réduit les sièges, il exige 99,9 % avec pénalités sans contrepartie. Pour chacun : signal, réponse, décideur | relecture | CEO |
| 33 | E13 — Reconduction | Lire l'avis juridique | Clause citée (article), effet au 31/03/2027 sans dénonciation formelle, qualification du courrier du 12/09, avis signé | relecture | juriste |
| 34 | E16 — Calendrier | Vérifier les dates | Calendrier daté jusqu'à la 1re réunion. Préavis = 30/09/2026 (6 mois avant le 31/03/2027) | mécanique | script de dates |
| 35 | E6 — Prêt | Lire la fiche go/no-go | Statut de chaque ligne, signature du CEO, datée ≥ 5 jours ouvrés avant la 1re réunion [proposé] | relecture | CEO |
| 36 | Contenu — Trous | Chercher dans les PDF tels qu'envoyés et toutes les annexes : [à compléter], TODO, TBD, XXX, lorem, « à définir », cellule vide | 0 occurrence | mécanique | script |
| 37 | Contenu — Sources | Le juge tire 10 chiffres [proposé] et les retrace | Chacun retrouvé (document, date, responsable) en moins de 5 min | relecture | CEO |
| 38 | Contenu — Chiffres dérivés | Recalculer | 186 = 141 + 45. 141 k€/420 = 335,7 €/siège. 186 k€ = 14 % du récurrent, donc ≈ 1,33 M€, à comparer au chiffre de la finance | mécanique | `calc-check` |
| 39 | Contenu — Éléments nommés | Vérifier | Chaque annexe, article, export et rapport cité existe et s'ouvre | mécanique | script |
| 40 | Contenu — Cohérence | Extraire les valeurs clés de chaque document | Planchers, cibles, niveaux de SLA, date de préavis identiques partout | mécanique | script |
| 41 | E15 — Confidentialité | Chercher les valeurs de planchers et le 72 k€ dans tous les documents | Présents seulement dans des documents marqués « restreint » | mécanique | script |
| 42 | E14 — Parties absentes | Lire la liste | Au moins : planificateurs de Valence/Orléans, équipe support/hébergement (astreinte sous 99,9 %), nos autres clients (précédent prix/SLA). Coût ou gain de chacun, relu par quelqu'un hors compte et sans variable dessus | relecture | relecteur sans enjeu |
| 43 | E7 — Accord signé vs planchers | Extraire du contrat : montant annuel toutes lignes, durée, plafond de pénalités, périmètre | Chaque valeur respecte le plancher du mandat | mécanique (après signature) | script |
| 44 | E7 — Texte signé | Chercher trous, annexes, totaux, exemple d'indexation | 0 trou, annexes présentes, totaux exacts | mécanique (après signature) | script |
| 45 | E7 — Texte = accord | Comparer le term sheet au texte signé | Aucun écart | relecture | juriste |
| 46 | E7 — Accord signé vs repli | Scorer l'accord signé | Au-dessus de notre repli | mécanique (après signature) | script sur grille |
| 47 | E7 — Accord signé, partie la moins servie | Scorer | Seuil de la ligne 5 respecté | mécanique (après signature) | script sur grille |
| 48 | E8-E9 — Cibles obtenues | Lire le contrat | Compte de 0 à 3 : durée ≥ 3 ans, clause Syntec, ligne module | mécanique (après signature) | script |
| 49 | E10 — SVI, notre côté | Questionnaire à chaque négociateur séparément, dans les 2 semaines [proposé] | ≥ 4 par dimension (plancher), ≥ 5 (cible) [proposés]. Échelle et conditions d'usage à vérifier | terrain | collecté par le CEO, hors auteurs |
| 50 | E10 — Écart entre dimensions | Comparer les 4 dimensions | Aucune dimension à plus de 1,5 point sous la moyenne des autres [proposé] | terrain | CEO |
| 51 | E10 — SVI ou debrief côté client | Demander au DAF et au directeur des opérations, séparément | Réponses obtenues et gardées à part. Si refus, le refus est noté et le CEO fait un appel de debrief | terrain | CEO |
| 52 | E10 — 6 mois, factures | Comparer facturation et contrat | Chaque montant facturé = montant contractuel, indexation comprise | mécanique (après 6 mois) | script de facturation |
| 53 | E10 — 6 mois, paiements | Contrôler | Toutes les factures payées dans les délais contractuels | terrain | finance |
| 54 | E11 — 6 mois, SLA mesuré | Recalculer chaque mois | Rapport mensuel envoyé 6 fois sur 6, pénalités calculées selon la formule | mécanique (après 6 mois) | script de supervision |
| 55 | E11 — 6 mois, pénalités versées | Sommer | ≤ exposition projetée à la ligne 16 | terrain | finance + CTO |
| 56 | E10 — 6 mois, durabilité | Chercher dans les courriers et tickets | Aucune escalade vers la résiliation, mise en demeure ou renégociation forcée | terrain | CEO |
| 57 | E12 — 6 mois, usage | Mesurer les connexions | Valence/Orléans pas sous le niveau de la signature | terrain | CS |
| 58 | E12 — 12 mois, usage | Mesurer | Valence/Orléans ≥ 80 % du niveau de janvier 2026 [proposé] | terrain | CS |
| 59 | E10 — 12 mois, contribution | Calculer revenu − pénalités versées − coût de service réel | ≥ 98 k€/an (plancher), ≥ 114 k€/an (cible) [dérivés] | terrain | finance |
| 60 | E10 — 12 mois, relation | Poser 2 questions (reconduirait-il, lancerait-il un appel d'offres) au DAF et au directeur des opérations | Ni l'un ni l'autre n'annonce d'appel d'offres avant l'échéance | terrain | CEO, pas les négociateurs |
| 61 | E9 — 12 mois, module (si vendu) | Mesurer les km selon la méthode du pilote Lyon, sur ≥ 1 nouvel entrepôt | ≥ −4,5 % de km [proposé : moitié du −9 % de Lyon] | terrain | exploitation + CS |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Les poids sont réglés après coup pour que le paquet préféré gagne. La grille est complète et juste, mais le résultat est arrangé → lignes 3, 9, 30.
- L'exposition SLA est calculée sur la moyenne annuelle (99,7 %) au lieu des mois pris un à un → ligne 16.
- Le plancher baisse discrètement quand le client insiste sur −12 %, et chaque document reste cohérent avec le nouveau chiffre → lignes 3, 40.
- Le dossier est complet, mais il suppose un client coopératif qui accepte 3 ans et le module → ligne 32.
- Le prix par siège tient sur le papier, mais le client peut ramener les sièges aux utilisateurs réellement actifs (Excel à Valence/Orléans) → lignes 18, 32.
- L'avis juridique est pris pour acquis : on suppose que le préavis passé ferme la porte au client, alors que la clause n'a pas été lue → ligne 33.
- Le satisfecit de fin est rempli par ceux qui ont négocié → lignes 49, 51, 60.
- La liste des parties absentes existe mais reste générique → ligne 42.

## Non testable en l'état / Not testable as stated
- E8 « idéalement » — aucun seuil de succès partiel. À quoi l'équipe reconnaît-elle un succès : 3 cibles sur 3, ou 2 sur 3, et lesquelles ?
- E6 « savoir quand le dossier sera prêt » — la note ne donne pas la date de la 1re réunion. Quelle est-elle ?
- « Bon accord » pris dans son ensemble n'est pas une ligne. Il se lit dans les lignes 43 à 61.
- Satisfaction du client — il peut refuser de répondre. La ligne 51 prévoit le repli (debrief du CEO).

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 26 | 5 | script, exécuté par le CEO (hors de portée des auteurs). 7 lignes visibles ne tournent qu'après signature ou après 6 mois |
| relecture | 24 | 5 | CEO, juriste, finance, CTO, CS, un relecteur hors compte |
| terrain | 11 | 1 | après signature, à 6 mois et à 12 mois, par des personnes autres que les négociateurs |

Un script ne règle que l'arithmétique de la grille et la complétude, environ 43 % des lignes. Il ne dit pas si l'accord est bon : cela dépend du client et ne se voit qu'à 6 et 12 mois. La couverture est faible sur l'issue et élevée sur le dossier.

## Questions ouvertes / Open questions
1. Les 170 k€ incluent-ils le module de 38 k€ ? La cible de 224 k€ suppose le prix de base maintenu.
2. Quels planchers pour la durée, le niveau de SLA, le plafond de pénalités et le nombre de sièges ? Le CEO doit les fixer avant la 1re offre (ligne 2).
3. Quelle est la date de la 1re réunion de novembre ? Sans elle, la ligne 35 n'a pas de date butoir.
4. Les directeurs commercial et demandeur ont-ils une part variable sur ce compte ? Si oui, ils sont partie prenante à la ligne 42.
5. Qui joue le client simulé dans la part cachée : une personne extérieure ou le skill `red-team` ?
6. Les conditions d'usage du questionnaire SVI autorisent-elles votre usage, et sur quelle échelle ?
7. Qui possède le suivi à 6 et 12 mois, avec nom et date au calendrier ?

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part
Chaque ligne vérifie une exigence que les auteurs connaissent déjà. En cas d'échec, on leur dit quelle exigence (E) a échoué, jamais le test ni les valeurs.

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E2 — Poids perturbés (garde les lignes 9, 10, 30) | Rejouer la grille avec chaque poids perturbé de ±30 % [proposé], ou avec les poids que le CEO donne lui-même | Le paquet cible reste au-dessus du plancher et non dominé. Le classement des 3 premiers paquets est stable | mécanique | CEO, script |
| H2 | E7 — Copie du mandat (garde la ligne 3) | Comparer l'empreinte (hash) de la copie du mandat signé que le CEO détient à la version finale du dossier | Planchers identiques, ou révision signée par le CEO | mécanique | CEO |
| H3 | E3/E4 — Tour simulé (garde les lignes 26 à 29) | Faire jouer le client, avec son repli estimé et ses contraintes, sans lui montrer notre plan. Deux variantes : concurrent à 150 k€ avec gain d'intégration WMS, et refus de 3 ans avec clause de sortie | Les réponses du plan tiennent sans franchir le plancher | relecture | joueur extérieur ou `red-team` |
| H4 | E5 — Coups du client (garde la ligne 32) | Lister les 3 coups les plus forts du client simulé | Chacun est prévu dans le plan, ou le plan est amendé | relecture | joueur extérieur ou `red-team` |
| H5 | E4 — Cible dominée (garde la ligne 30) | Le client simulé cherche un paquet que les deux côtés préfèrent à la cible | S'il en trouve un, la cible était dominée et le plan est amendé | relecture | joueur extérieur ou `red-team` |
| H6 | E11 — Exposition SLA (garde la ligne 16) | Recalculer sur un export de supervision tiré par le juge, pas par les auteurs, et sur le pire mois | Exposition ≤ plafond de pénalités du mandat, ou le plan dit comment il l'assume | mécanique | CEO + CTO |
| H7 | E12 — Réduction de sièges (garde les lignes 18 et 32) | Prix par siège ≈ 335,7 € (141 k€/420). Avec le prix de base maintenu à 186 k€, le plancher de 170 k€ ne supporte que ≈ 47 sièges en moins (≈ 11 %), si seules les licences bougent. Comparer aux sièges actifs réels | Le plan montre la réponse si les sièges tombent au nombre d'actifs, sans franchir le plancher | mécanique | CEO + finance |
| H8 | E13 — Seconde lecture (garde la ligne 33) | Un second juriste lit la clause de reconduction et le courrier du 12/09 sans voir l'avis du premier | Même conclusion, ou écart expliqué | relecture | juriste indépendant |
| H9 | Contenu — Trous (garde la ligne 36) | Chercher dans le rendu final d'autres formes : « à voir », « tbc », « xx k€ », « … », cellules vides, feuilles et lignes masquées, commentaires dans les fichiers | 0 occurrence | mécanique | CEO, script du juge |
| H10 | E10 — Appel indépendant (garde les lignes 49, 51, 60) | Le CEO appelle lui-même le DAF ou le directeur des opérations, 3 questions ouvertes, et compare à ce que les négociateurs ont rapporté | Concordance. Tout écart est tracé et expliqué | terrain | CEO |
| H11 | E14 — Parties absentes (garde la ligne 42) | Demander au responsable support, sans lui montrer la liste, qui paie et quoi sous 99,9 % avec pénalités, puis comparer | Les mêmes éléments sont retrouvés, ou la liste est complétée | relecture | responsable support |

Les lignes H1, H6 et H9 sont les plus exposées au contournement. Le plan est complet par construction, donc la grille et les recherches de trous doivent être rejouées avec d'autres entrées. H3 à H5 reprennent le client simulé de l'annexe négociation, joué par quelqu'un qui n'a pas lu le plan.