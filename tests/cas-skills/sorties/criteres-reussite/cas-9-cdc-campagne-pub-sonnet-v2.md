<!-- Sortie brute de criteres-reussite 1.0.0 (version finale), Sonnet, 0.23 $, 2 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: document (cahier des charges d'appel d'offres), puis sélection d'agence, puis bilan de campagne
author: vous et la directrice marketing (CDC) ; l'agence retenue (campagne)
judge: comité des franchisés pour le verdict ; détenteur de la part cachée à désigner (voir fin)
---

# Critères de réussite : consultation d'agences, campagne « pains au levain » printemps 2027

## Synthèse / Summary
Il y a trois choses à juger : le CDC (prêt à envoyer quand il est lisible, chiffré et mesurable), la grille de choix (elle doit départager une agence qui sert le besoin d'une agence qui coche les cases) et le bilan de juin (une campagne qui a fait vendre, pas seulement plu).
Dates supposées : on est en octobre 2026, donc campagne de mars à mai 2027 et bilan en juin 2027 `[inferred]`.
Le plan compte **46 lignes visibles** : 24 mécaniques, 14 relecture, 8 terrain. Il y a en plus une part cachée d'environ 9 lignes, à faire écrire par le juge.
Un script règle environ la moitié des lignes, surtout avant l'envoi du CDC. La vraie question, « la campagne a-t-elle marché ? », relève du terrain et des chiffres de juin.
Question ouverte principale : l'exigence de mesure (boutiques témoins) s'oppose à l'équité entre franchisés (toutes les boutiques couvertes). Voir « Questions ouvertes ».
Lignes bloquantes / Blocking lines : 2, 7, 8, 10, 12, 24.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Faire connaître la nouvelle gamme de pains au levain | « faire connaître la nouvelle gamme » | issue |
| E2 | Ramener en boutique les 25-40 ans | « ramener en boutique les 25-40 ans » | issue |
| E3 | Campagne de mars à mai, bilan en juin | « mars à mai », « en juin » | livrable (diffusion) et issue (bilan) |
| E4 | 90 k€ HT, création et achat d'espace compris | « Budget : 90 k€ HT » | livrable |
| E5 | Canaux : affichage local, réseaux sociaux, radio locale à trancher | « radio locale peut-être » | livrable |
| E6 | Les 38 boutiques comptent : aucune absente de la carte ni des supports | « boutiques pas sur la carte du site » | livrable |
| E7 | Effet mesurable sur les ventes, preuve crédible pour des franchisés méfiants | « aucun effet mesurable » (2024) | issue |
| E8 | CDC prêt à envoyer à 5 agences | « prêt à envoyer à cinq agences » | livrable |
| E9 | Permettre de choisir la bonne agence | « choisir la bonne » | livrable (grille) |
| E10 | Utiliser les données disponibles : tickets par boutique et par semaine depuis 2022, carte fidélité (~30 %) | « On a les tickets… » | livrable |
| E11 | Le comité des franchisés juge | « c'est le comité… qui jugera » | issue |
| E12 | Pas de données personnelles ni de chiffres de franchisés exposés sans cadre `[inferred]` | RGPD, confidentialité commerciale | livrable |
| E13 | Les 5 agences reçoivent la même information, au même moment `[inferred]` | équité d'une consultation | livrable |
| E14 | Calendrier tenable de l'envoi au lancement `[inferred]` | réservation d'espace avant mars | livrable |

Contrainte : la moitié du budget vient de la cotisation marketing des franchisés. Je ne sais pas d'où vient l'autre moitié.

## Issue visée / Outcome zone
Les seuils sont fixés par le comité **avant l'envoi du CDC** et inscrits dans le CDC. Ils ne sont pas fixés après coup, ni par l'agence.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E8 | Offres reçues | 3 offres conformes `[proposed]` | 5 offres conformes | directrice marketing | à la remise |
| E7 | Écart de tickets hebdomadaires, boutiques exposées contre témoins, par rapport aux mêmes semaines de l'an passé | écart supérieur au bruit habituel d'une semaine à l'autre, calculé sur 2022-2025 `[proposed]` | marge brute additionnelle ≥ 90 k€ (coût total récupéré) `[proposed]` | comité | juin |
| E1 | Part des tickets contenant un pain au levain | à fixer, sans référence avant lancement (voir « Non testable ») | à fixer | comité | juin |
| E2 | Fréquence des 25-40 ans porteurs de la carte | non inférieure aux témoins `[proposed]` | à fixer | comité | juin |
| E11 | Confiance du comité | une majorité ne reconduirait pas telle quelle sa cotisation = échec `[proposed]` | majorité reconduirait | comité | réunion de juin |

## Critères vérifiables / Checks

### A. Le CDC est prêt à envoyer
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1, E2 : objectifs | Un lecteur qui n'a pas écrit le CDC cite chaque objectif et l'indicateur qui le mesure | 2 objectifs, 2 indicateurs nommés, aucun objectif sans indicateur | relecture | un membre du comité non rédacteur |
| 2 | E4 : budget | Chercher dans le CDC le montant, « HT » et le contenu du périmètre | « 90 000 € HT » une fois, avec création, achat d'espace, production, mesure listés comme inclus ; offre au-dessus déclarée non conforme | mécanique | directrice marketing ou finance |
| 3 | E4 : modèle de chiffrage | Remplir le tableau budgétaire imposé avec des valeurs d'essai | Lignes création / médias par canal / production / suivi ; le total se recalcule et un total > 90 000 est repérable | mécanique | finance (`calc-check`) |
| 4 | E5 : radio | Deux lecteurs répondent séparément à « la radio est-elle dans le budget, en option chiffrée à part, ou au choix de l'agence ? » | Même réponse, écrite dans le CDC | relecture | deux lecteurs non rédacteurs |
| 5 | E6 : liste des boutiques | Compter les boutiques de l'annexe et les comparer au registre du réseau | 38 lignes, adresse complète, département, aucune absente ni en double | mécanique | animation réseau |
| 6 | E6 : modèle de réponse | Ouvrir le modèle imposé aux agences | Matrice 38 boutiques × canaux à remplir, sans ligne optionnelle | mécanique | directrice marketing |
| 7 | E6 : carte du site | Sur la page rendue, compter les repères et comparer à la liste | 38/38, bonne adresse et bons horaires, avant l'envoi du CDC | mécanique | webmestre |
| 8 | E7 : protocole de mesure | Relire l'annexe « mesure » et refaire le calcul à blanc sur une semaine passée | Annexe présente : indicateur, période de référence, boutiques témoins ou déploiement décalé, qui calcule, quelles données sont fournies ; le calcul à blanc donne le même résultat entre deux personnes | relecture | contrôleur de gestion ou statisticien |
| 9 | E10 : données de référence | Recomposer les totaux annexés depuis l'extraction caisse | Chaque chiffre annexé (tickets, CA, semaines 2022-2026) se retrouve à l'unité | mécanique | finance (`calc-check`) |
| 10 | E12 : données nominatives | Chercher dans toutes les annexes nom, e-mail, numéro de carte, date de naissance individuelle | 0 occurrence ; données de carte agrégées uniquement | mécanique | DPO ou juriste |
| 11 | E12 : chiffres par boutique | Comparer ce qui est transmis aux agences avec l'accord donné par les franchisés | Chiffres par boutique transmis seulement agrégés par zone, ou avec accord écrit | relecture | juriste réseau ; chiffres visibles |
| 12 | Contenu : lacunes | Chercher dans le PDF tel qu'envoyé « [à compléter] », TODO, XXX, lorem, commentaire, modification suivie, nom d'un autre client, métadonnées | 0 occurrence | mécanique | directrice marketing |
| 13 | Contenu : cohérence | Extraire montant, dates, nombre de boutiques, tranche d'âge et poids des critères de tout le dossier | Une seule valeur par donnée, partout | mécanique | un relecteur extérieur |
| 14 | Contenu : annexes et liens | Ouvrir chaque annexe et chaque lien cité, dans les fichiers à envoyer | 100 % s'ouvrent et correspondent à leur intitulé | mécanique | un relecteur extérieur |
| 15 | E14 : ordre du calendrier | Ordonner envoi, questions, remise, soutenance, décision, réservations, 1er mars, fin mai, bilan | Dates croissantes, aucune interversion | mécanique | directrice marketing |
| 16 | E14 : faisabilité | Un acheteur d'espace confirme les délais de l'affichage et de la radio entre la décision et le 1er mars | Délai prévu ≥ délai minimal de réservation annoncé par lui | relecture | acheteur média |
| 17 | Règles du jeu | Chercher format, nombre de pages, date et heure limites, contact unique | Les 4 éléments présents | mécanique | directrice marketing |
| 18 | Matrice de conformité | Compter les exigences du CDC et les lignes du modèle de matrice | Une ligne par exigence, aucune exigence sans ligne | mécanique | un relecteur extérieur |
| 19 | Exigences vérifiables | Pour chaque exigence, dire ce que l'acheteur verra dans l'offre pour décider | Aucun « impactant », « innovant », « de qualité » sans observable | relecture | un relecteur extérieur |
| 20 | Pas de solution imposée | Repérer les marques, plateformes ou formats imposés | Chaque imposition est justifiée par écrit, sinon retirée | relecture | un relecteur extérieur |
| 21 | Recette de la livraison | Pour chaque exigence, chercher comment elle sera contrôlée à la livraison | Une phrase de contrôle par exigence | relecture | un relecteur extérieur |
| 22 | Lecture par le comité | 3 membres du comité lisent sans aide et répondent : que payons-nous, qu'obtenons-nous, comment le saurons-nous en juin ? | Les trois réponses sont justes et concordantes | relecture | 3 franchisés, avant envoi |
| 23 | E13 : équité | Relever dates et destinataires des envois du CDC et des réponses aux questions | 5 agences, même envoi, réponses communiquées aux 5 le même jour | terrain | directrice marketing ; journal d'envoi |

### B. La grille permet de choisir
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 24 | E9 : grille publiée | Additionner les pondérations publiées dans le CDC | Somme = 100, et c'est la grille réellement utilisée | mécanique | un relecteur extérieur |
| 25 | E9 : pondérations | Chaque membre du comité classe les critères à l'aveugle, puis on compare au classement des poids | Même ordre ; si l'ordre diffère, on corrige les poids avant publication | relecture | comité |
| 26 | E7, E9 : prix et références | Lire la règle de notation des références | Un prix créatif ne rapporte aucun point seul ; points seulement pour un cas avec avant/après sur les ventes ou la fréquentation | relecture | un relecteur extérieur |
| 27 | E9 : constance | 3 notateurs notent seuls la même offre d'essai | Écart par critère ≤ 2 points sur 10 `[proposed]` ; au-delà, le critère est mal formulé | relecture | directrice marketing, 2 franchisés |
| 28 | E4 : offre conforme | Recalculer le budget de chaque offre et regarder la matrice | Matrice complète, total recalculé ≤ 90 000 € HT | mécanique | finance (`calc-check`) |
| 29 | E6 : offre | Regarder la matrice 38 × canaux de chaque offre | 0 boutique sans exposition ; sinon offre non conforme | mécanique | animation réseau |
| 30 | E7 : plan de mesure | Lire la partie mesure de chaque offre | Elle accepte le protocole de l'annexe et nomme ce que l'agence s'engage à fournir (rapports de diffusion, accès aux données) | relecture | contrôleur de gestion |
| 31 | E9 : références | Appeler le client d'un cas cité | Le client confirme l'effet chiffré annoncé, avec la période | terrain | un franchisé ou la directrice |

### C. L'agence livre ce qui était promis
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 32 | E3 : diffusion | Comparer preuves de diffusion (captures, constats d'affichage, relevés radio) au plan | Chaque canal est actif aux dates du plan, entre le 1er mars et le 31 mai | relecture | directrice marketing |
| 33 | E4 : dépense | Rapprocher factures et justificatifs du devis | Espace acheté = devis à ± 5 % `[proposed]`, total ≤ 90 000 € HT | mécanique | finance (`calc-check`) |
| 34 | E6 : carte | Relancer la vérification de la ligne 7 au lancement et en semaine 6 | 38/38 aux deux dates | mécanique | webmestre |
| 35 | E6 : ciblage | Exporter les réglages de ciblage géographique des annonces | Chaque boutique est dans le rayon d'au moins une annonce | mécanique | acheteur média |
| 36 | E6 : affichage | Aller voir sur place dans un échantillon de boutiques | Affiche visible dans la zone, dans 10 boutiques sur 10 tirées au sort `[proposed]` | terrain | animateur réseau |
| 37 | E6 : mentions locales | Comparer adresse et horaires des supports au registre | 0 écart | mécanique | animation réseau |
| 38 | E1 : produit en rayon | Visiter des boutiques pendant la campagne | Gamme au levain en stock, au nom affiché, en semaines 1, 6 et 12 | terrain | animateur réseau |
| 39 | E2 : ciblage réseaux | Lire les rapports des plateformes | Part des impressions 25-40 ans ≥ 60 % `[proposed]` | mécanique | acheteur média |

### D. En juin : la campagne a-t-elle marché ?
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 40 | E7 : ventes | Calculer l'écart exposées/témoins selon l'annexe, sur tous les tickets | Résultat comparé au plancher et à la cible de la zone | terrain | contrôleur de gestion, pas l'agence |
| 41 | E1 : levain | Suivre la part de tickets avec levain, semaine par semaine | Hausse comparée au plancher et à la cible | terrain | contrôleur de gestion |
| 42 | E2 : carte fidélité | Comparer les visites des porteurs de carte 25-40 aux témoins | Résultat comparé au plancher et à la cible | terrain | contrôleur de gestion ; données agrégées |
| 43 | E4, E7 : coût | Recalculer le coût par ticket additionnel, tous coûts inclus | Même résultat qu'une seconde personne | mécanique | finance, autre que l'auteur |
| 44 | E6 : équité | Compter les boutiques dans le rapport de résultats | 38/38, aucune écartée | mécanique | un relecteur extérieur |
| 45 | E7 : buts déplacés | Comparer les définitions de juin à celles de l'annexe d'origine (empreinte) | Identiques | mécanique | juge |
| 46 | E11 : comité | Poser en juin trois questions écrites avant le lancement | Questions et réponses datées, non reformulées | terrain | comité |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Un CDC complet et propre, mais qui renvoie la mesure à « un suivi de performance » : les agences promettent de l'impact, et en juin personne ne peut conclure (2024 refait) → 8, 19, 45.
- Une agence primée au visuel superbe mais sans plan de mesure → 26, 30, 31.
- Les ventes montent, mais elles auraient monté de toute façon (Pâques, météo, hausse de prix) → 40 avec témoins.
- Les 38 boutiques sont à l'écran, mais l'une a une mauvaise adresse ou une affiche hors de sa zone → 7, 34, 35, 36, 37.
- La campagne fait venir du monde, mais le levain manque en rayon → 38.
- Hausse sur les porteurs de carte (30 %, peut-être pas représentatifs), prise pour celle de tout le réseau → 40 et 42 lues ensemble.
- La mesure est faite par l'agence, ou ses données sont inaccessibles → 9, 30, 40.
- Une offre qui coche toutes les cases mais sert mal le besoin gagne ou fait égalité → part cachée.

## Non testable en l'état / Not testable as stated
- **E2, « ramener les 25-40 ans »** : les tickets n'indiquent pas l'âge, et la carte ne couvre que 30 % des clients. Questions : la carte contient-elle une date ou une tranche d'âge ? Son usage pour cette mesure est-il couvert par le consentement des porteurs ?
- **E1, « faire connaître »** : pas de mesure de notoriété avant lancement. Questions : les tickets détaillent-ils les produits, pour suivre le levain ? Faut-il un mini-sondage en boutique (à chiffrer dans les 90 k€) ?
- **Plancher et cible E1, E2** : valeurs à décider par le comité, une fois les données de 2022-2026 dépouillées.
- **« La bonne agence »** : dépend du classement des critères par le comité (ligne 25).

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 24 | à écrire (~4) | script ou recomptage, par un autre que vous |
| relecture | 14 | à écrire (~4) | relecteurs extérieurs, comité, acheteur média |
| terrain | 8 | à écrire (~1) | animateurs réseau, contrôleur de gestion, comité en juin |

Un script ou un recomptage règle un peu plus de la moitié du plan, presque tout avant l'envoi du CDC. Il ne dit rien du résultat de juin, qui dépend de clients, de la météo et du comité. Aucun agent en boucle n'est prévu ici, donc pas de critère d'arrêt de boucle.

## Questions ouvertes / Open questions
1. **Équité contre mesure.** Les boutiques témoins sont des boutiques moins servies, ce qui heurte E6 après la plainte de 2024. Une piste : un **déploiement décalé** (chaque boutique est exposée, certaines 3 ou 4 semaines plus tard), à valider avec le comité.
2. Qui finance l'autre moitié des 90 k€ ?
3. Les tickets détaillent-ils les produits, et la carte contient-elle l'âge ?
4. Qui détient la part cachée (voir plus bas) ?

---

✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Vous écrivez le CDC avec la directrice marketing, donc vous en êtes l'auteur. Je n'écris pas la part cachée, car vous la liriez. Un juge qui n'a pas co-écrit le CDC l'écrit seul, par exemple un franchisé du comité qui n'a pas participé à la rédaction, ou le contrôleur de gestion.

Exigences à garder / Requirements to guard : E1, E2, E4, E6, E7, E9, E12, E13. Environ 9 lignes, au moins une par exigence.
Juge / Judge : lancer `criteres-reussite` avec `requester: judge`, avec ce brief et le plan visible ci-dessus. Garder le résultat pour soi.

Rappel : la grille de choix sera publiée aux agences, il ne peut donc pas y avoir de critère caché sur leurs offres. La part cachée teste le CDC et la grille, par exemple avec deux offres fictives. L'une sert le besoin, l'autre coche toutes les cases. Si la seconde gagne ou fait égalité, la grille est contournable.