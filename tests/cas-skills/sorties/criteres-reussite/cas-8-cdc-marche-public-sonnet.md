<!-- Sortie brute de criteres-reussite 1.0.0 (avec les annexes documents et travaux), Sonnet, 0.32 $, 4 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: document (partie technique d'un cahier des charges, MAPA) et logiciel (site + portail qui seront livrés)
author: chargée de mission numérique (seule), puis le prestataire retenu pour le site
judge: directeur général des services (DGS)
---

# Critères de réussite : partie technique du CCTP, refonte du site et portail de démarches

## Synthèse

- **Ce que tu livres :** un texte, le CCTP technique. Le site, le choix du prestataire et la réception dépendent d'autres acteurs, donc je les traite comme des issues à viser, pas comme des acquis.
- **Ce que veut dire « prêt » :** un développeur extérieur et un agent d'un autre service lisent le CCTP sans te poser de question. Chaque exigence a un chiffre ou un observable. Chaque exigence dit comment elle sera vérifiée à la réception. Une offre qui ne fait que cocher les cases ne peut pas gagner.
- **Plan :** 56 lignes visibles : 21 mécaniques, 27 de relecture, 8 de terrain. Le plan a trois parties : cahier prêt à publier (1-31), choix du prestataire (32-34), réception du site (35-56).
- **Délai :** du 17 octobre au 2 décembre, il reste 46 jours. Les lignes 7-9 (éditeur de la cantine) et 10 (FranceConnect) dépendent de tiers qui répondent lentement. Je les lancerais en premier.
- **Part cachée non écrite :** tu es l'autrice. Un avertissement du type « ne pas lire » ne garderait rien de caché. Tu trouveras en fin de document une demande scellée à transmettre au DGS.
- **Vérificateur technique :** le DGS n'est probablement pas en mesure de vérifier le RGAA, l'API ou la sécurité. Aucun vérificateur technique n'est nommé pour les lignes 11, 35-37, 44-46 et 52 (voir les questions ouvertes).

Lignes bloquantes : 2, 5, 8, 21, 23, 35, 38, 44, 46, 48.

## Exigences

| E | Exigence | Source | Cahier ou issue |
|---|---|---|---|
| E1 | Refonte du site internet | « refonte du site internet » | cahier (exigence) + issue (site) |
| E2 | Portail de 3 démarches : inscriptions périscolaires, réservation de salles, demandes de bacs | « création d'un portail de démarches en ligne » | cahier + issue |
| E3 | Accessibilité RGAA | « obligation d'accessibilité (RGAA) » | cahier + issue |
| E4 | Données hébergées en France | « hébergement des données en France » | cahier + issue |
| E5 | Reprise des 400 pages actuelles | « reprise des 400 pages » | cahier + issue |
| E6 | Interfaçage avec le logiciel de facturation de la cantine (API mal documentée) | « interfaçage… API mal documentée » | cahier + issue |
| E7 | Connexion FranceConnect, souhaitée | « connexion par FranceConnect souhaitée » | cahier + issue |
| E8 | Agents autonomes pour mettre à jour le site après formation | « les agents… mettront à jour le site eux-mêmes » | cahier + issue |
| E9 | « Un site moderne et simple » | souhait des élus | cahier (à rendre observable) |
| E10 | « Les habitants trouvent en trois clics » | souhait des élus | cahier (à rendre observable) + issue |
| E11 | Formulaires utilisables sur téléphone | [inferred] de l'échec 2019 : « formulaires pas accessibles sur téléphone » | cahier + issue |
| E12 | Maintenance sur trois ans | « plus la maintenance sur trois ans » | cahier + issue |
| E13 | Budget d'environ 60 k€ HT, maintenance en plus | « Budget estimé : 60 k€ HT » | cahier |
| E14 | Critères d'attribution : technique 60 %, prix 40 % | « valeur technique 60 %, prix 40 % » | cahier |
| E15 | Publication le 2 décembre | « Publication prévue le 2 décembre » | cahier |
| E16 | Offres comparables entre elles et notables sans interprétation | [inferred] (CCTP publié à des candidats concurrents) | cahier |
| E17 | Réversibilité : récupérer contenus et données sans dépendre du prestataire | [inferred] (maintenance sur 3 ans) | cahier + issue |
| E18 | Protection des données personnelles (familles, enfants) | [inferred] (inscriptions périscolaires) | cahier + issue |
| E19 | Sécurité du portail | [inferred] (démarches nominatives) | cahier + issue |
| E20 | Réception sur le site réel, avec de vrais agents et de vrais téléphones | « conforme sur le papier » (échec 2019) | cahier + issue |

Je n'ai pas de volume de familles ni de pic d'inscriptions, donc la ligne 51 (charge) en dépend (voir questions ouvertes).

## Issue visée

Le DGS fixe ces seuils avant le 2 décembre, pas après avoir vu les offres.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E14, E16 | Offres recevables | 2 [proposed] | 4 ou plus [proposed] | DGS | date limite de remise |
| E13 | Prix | au moins 1 offre recevable sous le plafond fixé par le DGS | au moins 2 offres ≤ 60 k€ HT de création, maintenance en plus [proposed] | DGS | ouverture des plis |
| E8 | Autonomie des agents | chaque agent réussit 80 % des tâches types sans aide [proposed] | 100 % | DGS | réception (ligne 48) et 3 mois après (ligne 56) |
| E10 | Trouvabilité | 70 % des testeurs réussissent chaque tâche [proposed] | 90 % [proposed] | DGS | réception (ligne 50) |
| E2, E11 | Part des démarches faites en ligne | à fixer après relevé de l'existant | à fixer | DGS | 6 mois après, soit après une rentrée scolaire |
| E20 | Réception | aucune réserve bloquante à la réception provisoire | aucune réserve à la réception définitive | DGS | réception |

## Critères vérifiables

### A. Le cahier est prêt à publier

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E16, E20 : matrice des exigences | Dans le CCTP, chaque exigence porte un numéro, une méthode de vérification à la réception et la preuve attendue du prestataire | 0 case vide sur toutes les lignes | mécanique | toi ou un script ; pas de donnée sensible |
| 2 | Tous : PDF tel que publié (pas le Word) | Chercher « [à compléter] », TODO, XXX, lorem, commentaires, modifications suivies, nom de l'autre marché ou collectivité, métadonnées | 0 occurrence | mécanique | un script, lancé par le DGS |
| 3 | E1, E2, E5, E12, E13, E15 : cohérence des chiffres | Extraire 400 pages, 22 communes, 31 000 habitants, 60 k€ HT, 3 ans et les dates dans CCTP, règlement, acte d'engagement et bordereau de prix | valeurs identiques partout | mécanique | script ou `calc-check` |
| 4 | E2 : les 3 démarches | Un lecteur hors projet liste, pour chacune des trois, les acteurs, les étapes, les pièces, la destination de la demande et le volume annuel | aucun « à définir » ; chaque démarche validée par son service (périscolaire, salles, déchets) | relecture | agent de chaque service |
| 5 | E5 : inventaire des 400 pages | Comparer l'inventaire annexé (URL, type, pièces jointes, responsable) à un crawl du site actuel | autant de lignes que de pages crawlées, écarts justifiés par écrit | mécanique | script |
| 6 | E5 : règle de reprise | Un lecteur dit qui trie, qui réécrit, qui migre, et jusqu'à quelle date | chaque tâche a un responsable (collectivité ou prestataire) | relecture | lecteur hors projet |
| 7 | E6 : documentation de la cantine | Vérifier que les annexes existent, ou que le CCTP dit qu'il n'y en a pas ; l'éditeur, la version et la liste des flux (lecture/écriture) sont nommés | fichiers présents, liens ouvrables | mécanique | script |
| 8 | E6 : engagement de l'éditeur | Lire l'écrit de l'éditeur (courriel ou courrier) | il confirme l'ouverture de l'API, un délai et un coût (ou l'absence de coût) | relecture | toi ; le DGS contresigne |
| 9 | E6, E16 : accès à l'API avant les offres | Le règlement prévoit une période de questions, ou une session avec l'éditeur, avant la date limite | dates et modalités écrites | relecture | juriste marchés |
| 10 | E7 : statut de FranceConnect | Un lecteur répond : exigence ou option ? qui demande l'habilitation ? avec quel délai ? | réponses sans ambiguïté ; si option, ligne de prix séparée | relecture | lecteur hors projet |
| 11 | E3 : définition de la conformité | Chercher la version du RGAA, un taux exigé chiffré, l'échantillon (pages types, formulaires des 3 démarches, espace usager), l'audit par un tiers, la déclaration d'accessibilité | les 5 éléments présents ; taux ≥ 100 % des critères applicables [proposed] ; version du RGAA en vigueur à la publication [à vérifier] | relecture | spécialiste accessibilité |
| 12 | E3, E8 : accessibilité des contenus saisis par les agents | L'exigence demande que l'outil guide l'agent (alternative textuelle, titres, documents) et que la formation le couvre | exigence présente avec un moyen observable | relecture | spécialiste accessibilité |
| 13 | E4 : périmètre de l'hébergement | L'exigence couvre données, sauvegardes, statistiques, polices, anti-robot, messagerie transactionnelle, accès du support | liste exhaustive ; le candidat nomme hébergeur, sous-traitants et lieux | relecture | DSI ou développeur |
| 14 | E8 : autonomie | Le CCTP liste les tâches types, le nombre et les profils d'agents, la durée minimale de formation et le seuil de réussite | ≥ 10 tâches [proposed] ; seuil chiffré ; durée en heures | relecture | lecteur technique + un agent futur éditeur |
| 15 | E11 : appareils de référence | Le CCTP liste des téléphones et navigateurs (ancien Android, Safari iOS), une largeur minimale et le texte agrandi | liste nommée ; exigence « démarche complète sur téléphone » | relecture | développeur |
| 16 | E9, E10 : tâches de trouvabilité | Chaque tâche du test (10 à 15) a une source (statistiques, appels en mairie, recherches) ; seuil de réussite chiffré | 100 % des tâches sourcées ; « trois clics » remplacé par un test sur des habitants | relecture | toi ; un élu relit |
| 17 | E12 : engagements de maintenance | Pour chaque engagement : délai de prise en compte et de correction par gravité, disponibilité en %, méthode de mesure, pénalité | 0 engagement sans chiffre, unité et méthode | mécanique | script |
| 18 | E17 : réversibilité | Le CCTP exige un export complet (contenus, demandes, comptes) en format ouvert, la propriété des données et le sort du code | trois éléments présents | relecture | juriste marchés |
| 19 | E18 : données personnelles | Rôle du prestataire, durée de conservation, minimisation, registre | clauses présentes ; avis écrit du DPO | relecture | DPO de la communauté |
| 20 | E13 : budget | Estimation interne par poste (création, 3 démarches, reprise, API, FranceConnect, formation, audit RGAA, maintenance 3 ans) | total création ≤ 60 k€ HT ; maintenance chiffrée à part | relecture | toi + finances |
| 21 | E14 : poids | Additionner les sous-critères de valeur technique et le prix | technique = 60, prix = 40, total = 100 | mécanique | script |
| 22 | E14, E16 : sous-critères observables | Pour chaque sous-critère, le CCTP dit quelle pièce de l'offre sera lue et ce qui la fera bien noter | 0 sous-critère sans pièce ni observable (pas de « innovant » ni « de qualité ») | relecture | juriste marchés + DGS |
| 23 | E14 : formule du prix | Appliquer la formule du règlement à 3 offres fictives | notes recalculées = notes attendues ; le prix couvre création + maintenance 3 ans + options retenues | mécanique | script ou `calc-check` |
| 24 | E16 : cadre de réponse | Comparer les lignes du cadre aux exigences de la ligne 1 | mêmes numéros, ni plus ni moins | mécanique | script |
| 25 | E16 : pas de solution imposée | Chercher des noms de CMS, de marques ou d'éditeurs, hors l'éditeur de la cantine | 0 occurrence non justifiée (« ou équivalent » si nécessaire) | mécanique | script |
| 26 | E15 : calendrier | Calculer les durées entre publication, date limite, analyse, démarrage et mise en ligne | publication le 2 déc. ; remise ≥ 21 jours calendaires, fêtes comprises [proposed] ; dates dans l'ordre | mécanique | script ; confirmer avec le service marchés |
| 27 | E20 : réception en deux temps | Le CCTP prévoit une réception à la livraison et une après une période de fonctionnement réel | deux étapes, durée, levée des réserves écrites (à aligner avec le CCAP) | relecture | juriste marchés |
| 28 | E14, E16 : conformité aux règles de la commande publique | Avis écrit du service marchés sur les critères et leur pondération | avis rendu ; remarques traitées | relecture | juriste marchés |
| 29 | Tous : lecture à froid | Un lecteur hors projet n'a que le CCTP ; il dit en une phrase ce qui doit être livré et liste les 3 démarches | restitution identique à tes E1-E8 | relecture | agent d'un autre service |
| 30 | E16 : ambiguïtés | Un développeur extérieur liste les points où il poserait une question | chaque point a sa réponse dans le texte ou dans la période de questions | relecture | développeur / DSI voisin |
| 31 | E14 : pondération conforme à l'intention | Le DGS et un élu classent les sous-critères sans voir les poids | classement identique à l'ordre des poids | relecture | DGS + un élu |

### B. Choix du prestataire

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 32 | E8, E3, E6 : références | Appeler 2 références contactables de projets comparables avec 3 questions fixes (agents autonomes ? RGAA validé par audit ? interface livrée ?) | réponses notées | relecture | toi + une autre personne |
| 33 | E8, E11, E20 : soutenance imposée | Le règlement prévoit un scénario imposé sur nos données (une démarche, 3 modifications de contenu par un agent) | scénario écrit ; grille de notation écrite | relecture | commission d'analyse |
| 34 | E14 : notation | Deux évaluateurs notent chaque sous-critère séparément | écart > 2 points sur 10 [proposed] discuté et motivé | relecture | toi + une personne technique |

### C. Réception du site

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 35 | E3, E20 : audit RGAA | Audit par un tiers sur l'échantillon défini (ligne 11), sur le site livré | taux ≥ cible du CCTP ; déclaration d'accessibilité publiée | relecture | auditeur indépendant |
| 36 | E3 : scan automatisé | Lancer un outil sur toutes les pages-types et tous les formulaires | 0 erreur bloquante ; le scan ne couvre qu'une partie des critères, donc il ne remplace pas la ligne 35 | mécanique | développeur |
| 37 | E3 : clavier et lecteur d'écran | Faire les 3 démarches complètes au clavier seul et avec un lecteur d'écran | chaque démarche aboutit jusqu'à la confirmation | terrain | personne formée à l'accessibilité |
| 38 | E11, E20 : téléphones réels | Faire les 3 démarches complètes sur les appareils de la ligne 15, texte agrandi compris | chaque démarche aboutit ; confirmation reçue | terrain | agents + 3 habitants |
| 39 | E5 : liens et anciennes URL | Crawler le site livré ; tester chaque ancienne URL de l'inventaire | 0 lien interne cassé ; chaque ancienne URL redirige (301) vers la bonne page ou renvoie 410 avec décision écrite | mécanique | script |
| 40 | E5 : fidélité de la reprise | Tirer 20 pages au hasard [proposed] ; comparer texte, images, documents et dates | identiques, ou différence listée avec décision | relecture | agent hors projet |
| 41 | Tous : traces d'oubli sur le site réel | Parcourir toutes les pages, tous les formulaires, courriels et PDF de confirmation, pages d'erreur et 404 | 0 placeholder, 0 champ vide | mécanique | script |
| 42 | E4 : domaines tiers | Capturer les appels réseau de chaque type de page et chaque étape de démarche ; résoudre et localiser les domaines | tout domaine contacté est dans la liste déclarée et hébergé en France ; 0 hors France | mécanique | développeur |
| 43 | E4 : sauvegardes | Restaurer une sauvegarde dans un environnement vierge | site et demandes retrouvés ; lieu des sauvegardes confirmé par écrit | terrain | hébergeur, témoin de la communauté |
| 44 | E6 : écriture dans le logiciel de la cantine | Jouer 30 cas [proposed] (inscription, modification, annulation, deux parents, deux enfants) ; vérifier dans le logiciel de facturation, pas sur l'écran du portail | chaque dossier est présent et exact ; puis 5 cas réels en production | mécanique | agent cantine + développeur |
| 45 | E6 : API en panne et rejeu | Couper l'API ; rejouer deux fois la même demande | message clair ; demande conservée puis transmise au rétablissement ; 1 seul dossier | mécanique | développeur |
| 46 | E18, E19 : étanchéité entre usagers | Avec la session de A, appeler l'API/l'URL de la demande de B en changeant l'identifiant | accès refusé côté serveur | mécanique | développeur |
| 47 | E7 : FranceConnect (si retenu) | Se connecter avec une identité de test puis en production ; refaire une connexion ; essayer sans FranceConnect | pas de compte en double ; chemin alternatif prévu au CCTP | terrain | agent + développeur |
| 48 | E8, E20 : test d'autonomie | Les agents qui mettront à jour le site font les tâches de la ligne 14 sur l'environnement de la communauté, sans le prestataire, après la formation | seuil du CCTP atteint ; contenus produits accessibles (titres, alternatives) | terrain | DGS ou observateur avec grille |
| 49 | E8 : guide d'administration | Une personne qui n'a pas suivi la formation fait 3 tâches avec le guide seul | 3 tâches réussies ; captures conformes à la version livrée | relecture | agent hors formation |
| 50 | E10 : trouvabilité | 5 à 8 habitants ou agents non impliqués font les tâches de la ligne 16 depuis l'accueil, sur téléphone | seuil de réussite de la zone d'issue ; clics médians relevés | terrain | toi + observateur |
| 51 | E2 : charge | Simuler le pic d'inscriptions (nombre de familles à préciser) avec marge ×2 [proposed] sur un environnement comme la production | p95 < 3 s [proposed] ; erreurs < 1 % [proposed] | mécanique | développeur |
| 52 | E19 : sécurité | Scan de vulnérabilités et tests de base (OWASP) | 0 vulnérabilité critique ou haute | mécanique | développeur / prestataire sécurité |
| 53 | E17 : export | Exporter tous les contenus et demandes en format ouvert ; rouvrir hors du système | export complet et lisible | mécanique | développeur |
| 54 | E17 : droits | Se connecter en administrateur avec les comptes de la communauté ; vérifier nom de domaine, hébergement et dépôts | comptes et domaine au nom de la communauté | mécanique | toi |
| 55 | E12 : maintenance | Pendant la période de fonctionnement réel, provoquer 2 incidents (dont un critique) | délais mesurés ≤ engagements de la ligne 17 | terrain | toi |
| 56 | E8 : 3 mois après | Compter les mises à jour faites par les agents sans prestataire | seuil du DGS (zone d'issue) | terrain | DGS |

## Ce qui passerait et serait faux

- Chaque formulaire passe le scan RGAA mais ne se remplit ni au lecteur d'écran, ni sur un vieux téléphone. C'est l'échec de 2019. → lignes 35, 37, 38
- Le portail affiche « demande enregistrée » mais n'écrit rien dans le logiciel de la cantine. L'écran est vrai, l'état est faux. → lignes 44, 45
- L'hébergeur est en France, mais les statistiques, les polices ou la messagerie sont hors de France. → lignes 13, 42
- Les 400 pages sont comptées, mais des liens, des pièces jointes ou des anciennes URL sont cassés. → lignes 5, 39, 40
- Une offre au prix très bas gagne les 40 % avec une maintenance à 0 €. → lignes 17, 23
- La formation est belle sur le papier mais les agents échouent seuls, ou publient du contenu inaccessible. → lignes 14, 48, 49
- Une offre recopie les phrases du CCTP sans engagement. → lignes 22, 24, 33
- « Trois clics » est respecté avec un méga-menu de 40 entrées que personne ne comprend. → ligne 50

## Non testable en l'état

- E9 « moderne et simple » : aucun observable. Question : « quels trois sites un élu montrerait-il comme exemples, et que préfère-t-il dans chacun ? »
- E10 « trois clics » : un nombre de clics ne dit pas si l'habitant trouve. Question : « les élus acceptent-ils un test sur des tâches réelles à la place ? » (ligne 16).
- E7 « souhaitée » : exigence ou option ? Question : « peux-tu payer FranceConnect s'il n'est pas livré ? » (ligne 10).
- E4 « en France » : localisation seule, ou aussi protection contre les lois hors UE ? Question : « quel niveau de qualification demande-t-on à l'hébergeur ? »
- E13 : le chiffrage est-il réaliste pour tout ce périmètre ? Question : « as-tu une estimation poste par poste ? » (ligne 20).

## Couverture

| Type | Visible | Caché | Qui |
|---|---|---|---|
| mécanique | 21 | environ 11 au total, à écrire par le juge | script, lancé par le DGS ou la personne technique |
| relecture | 27 | | juriste marchés, DPO, spécialiste accessibilité, développeur, agents |
| terrain | 8 | | réception et 3 mois après |

Environ 38 % des lignes sont mécaniques, mais elles portent surtout sur la forme (cohérence, traces d'oubli, domaines, API). Aucune boucle automatique ne couvre le cahier : savoir si un texte sert le besoin est une affaire de relecture. À la réception, un script ferme les liens, les domaines, l'API et l'étanchéité. Il ne dit rien sur l'accessibilité réelle, l'autonomie des agents ni la facilité à trouver l'information, qui relèvent du terrain.

## Questions ouvertes

1. Rédiges-tu aussi le règlement de consultation, le CCAP et le bordereau de prix ? Les lignes 21 à 28 les touchent.
2. Qui, côté communauté, peut vérifier le RGAA, l'API et la sécurité (lignes 11, 35-37, 44-46, 52) : DSI, collectivité voisine, assistant à maîtrise d'ouvrage ?
3. Combien de familles utiliseront les inscriptions périscolaires, et quel est le pic (rentrée, vacances) ? Sans cela, la ligne 51 n'est pas chiffrable.
4. L'éditeur de la cantine a-t-il confirmé par écrit l'accès à l'API, son coût et son délai ?
5. Les 60 k€ incluent-ils la reprise des 400 pages, l'audit RGAA et la formation ?

✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée

Requirements to guard: E3, E4, E5, E6, E8, E10, E11, E14, E20. About 11 lines, at least one per requirement listed.
Judge: run `criteres-reussite` with `requester: judge`, this brief and the visible plan above, and keep what it writes to yourself.

Remarque pour le juge : les critères d'attribution seront publiés aux candidats, donc aucun critère caché sur leurs offres. La part cachée doit tester le CCTP lui-même : par exemple une offre fictive qui coche toutes les cases sans servir le besoin ne doit pas gagner. Elle doit aussi vérifier si les exigences sont les mêmes pour tous.