<!-- Sortie brute de criteres-reussite 1.0.0 (avant exigences du thème), Sonnet, 0.14 $. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: logiciel (application web de prise de rendez-vous et rappels SMS)
author: non précisé (personne, équipe ou agent en boucle) `[inferred]`
judge: quelqu'un d'autre que l'auteur (non précisé)
---

# Critères de réussite : prise de rendez-vous du cabinet de kinésithérapie

Je me suis appuyé sur l'annexe logiciel (`criteres_logiciel.md`), qui était disponible. Le brief tient en une phrase, donc beaucoup d'exigences sont marquées `[inferred]`. Je pars du principe que vous commandez l'application et ne la développez pas. Si vous êtes l'auteur, ne lisez pas la part cachée. Relancez ce travail avec `requester: author` pour obtenir à la place une demande scellée à transmettre au juge.

## Synthèse / Summary
On livre une application où le patient réserve un créneau en ligne, où le kiné voit son planning, et où le patient reçoit un SMS de rappel la veille. « Terminé » veut dire ceci : aucun créneau ne peut être réservé deux fois, chaque rendez-vous apparaît au planning, chaque rappel part une seule fois à la bonne heure, et les données de santé ne fuient nulle part.

Le plan compte 42 lignes : 35 mécaniques (28 visibles, 7 cachées), 3 de relecture et 4 de terrain. Une boucle automatique peut en fermer environ 80 %. Elle ne dit rien de l'issue, c'est-à-dire de la baisse réelle des rendez-vous manqués, et elle ne dit rien non plus de la réception réelle des SMS.

La question ouverte principale est de savoir ce que « la veille » veut dire pour un rendez-vous du lundi. Il y en a d'autres plus bas.

Lignes bloquantes : 3, 4, 7, 8, 10, 12, 17, 20.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Les patients réservent un rendez-vous en ligne | « les patients réservent en ligne » | livrable |
| E2 | Le kiné voit son planning | « le kiné voit son planning » | livrable |
| E3 | Rappel SMS la veille du rendez-vous | « un rappel par SMS la veille » | livrable (la réception réelle relève de l'opérateur) |
| E4 | Un créneau ne peut pas être réservé deux fois, ni se chevaucher | [inferred] | livrable |
| E5 | Le kiné fixe ses disponibilités : horaires, durées, congés, blocages | [inferred] | livrable |
| E6 | Le patient peut annuler ou déplacer son rendez-vous | [inferred] | livrable |
| E7 | Les données de santé et personnelles sont protégées : RGPD, hébergement HDS, effacement | [inferred] | livrable |
| E8 | Le SMS repose sur un consentement et on peut le refuser | [inferred] | livrable |
| E9 | L'application est utilisable sur téléphone et accessible | [inferred] | livrable |
| E10 | Le coût et les abus de SMS sont bornés | [inferred] | livrable |
| E11 | Le cabinet y gagne : moins de rendez-vous manqués, moins de temps au téléphone | [inferred] | issue |

Hypothèse : un seul kiné et un seul lieu. Les limites (budget, échéance) ne sont pas dans le brief.

## Issue visée / Outcome zone
Le plancher et la cible sont fixés par le kiné avant la mise en service. Les valeurs ci-dessous sont des propositions `[proposed]`.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E11 | Taux de rendez-vous manqués | pas pire que la mesure de départ (à relever avant le lancement) | baisse relative ≥ 30 % | le kiné | à 3 mois |
| E3 | SMS remis (accusé de l'opérateur) | 90 % | ≥ 97 % | le kiné | sur le premier mois |
| E1 | Part des rendez-vous pris en ligne | 20 % | ≥ 50 % | le kiné | à 3 mois |

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1, parcours nominal | Test de bout en bout : choisir un créneau, saisir les coordonnées, valider | Page de confirmation affichée, rendez-vous en base, visible au planning du kiné | mécanique | développeur ; données synthétiques |
| 2 | E1/E5, créneaux proposés | Récupérer tous les créneaux offerts sur 60 jours | Aucun créneau hors horaires, sur une pause, un jour férié, un congé, dans le passé, ou au-delà de l'horizon de réservation | mécanique | développeur |
| 3 | E4, concurrence | 20 requêtes simultanées sur le même créneau | Exactement 1 réussit ; les 19 autres reçoivent un refus clair ; 1 seul rendez-vous en base | mécanique | développeur |
| 4 | E4, règle côté serveur | Appeler l'API directement sur un créneau pris, ou sur un créneau fermé par le kiné | Refus (409 ou équivalent), sans rendez-vous créé | mécanique | développeur |
| 5 | E1, validation | Envoyer à l'API des numéros et e-mails invalides, des champs vides, des formats +33, 06 et 07 | Les invalides sont refusés côté serveur ; les formats valides sont normalisés au même format | mécanique | développeur |
| 6 | E1, confirmation rendue | Lire la page et le message de confirmation après réservation | Date, heure, adresse du cabinet et lien d'annulation présents ; aucune valeur vide | mécanique | développeur |
| 7 | E2, planning fidèle | Créer, annuler et déplacer des rendez-vous, puis comparer le planning à la base | Chaque rendez-vous actif apparaît une fois, à la bonne heure, trié ; aucun fantôme | mécanique | développeur |
| 8 | E2/E7, droits | Appeler l'API du planning sans identifiant, puis avec l'identifiant d'un autre patient | Refus (401 ou 403) ; un patient ne lit jamais le rendez-vous d'un autre | mécanique | développeur |
| 9 | E5, blocage manuel | Le kiné bloque un créneau ou pose un congé | Les créneaux disparaissent de l'offre en ligne ; les rendez-vous déjà pris sur la période sont signalés au kiné | mécanique | développeur |
| 10 | E3, envoi la veille | Horloge simulée, prestataire SMS factice : 50 rendez-vous répartis sur plusieurs jours | Exactement 1 SMS par rendez-vous, envoyé le jour calendaire précédent, entre 17 h et 19 h heure de Paris `[proposed]` | mécanique | développeur |
| 11 | E3, contenu du SMS | Lire le SMS rendu pour 20 patients types | Date, heure, nom du cabinet et moyen d'annuler présents ; aucun motif de soin ni pathologie ; aucun placeholder | mécanique | développeur |
| 12 | E3, unicité | Lancer la tâche d'envoi deux fois de suite, puis redémarrer le service en cours d'envoi | Toujours 1 seul SMS par rendez-vous | mécanique | développeur |
| 13 | E3, rendez-vous modifiés | Annuler un rendez-vous, puis en déplacer un autre, avant l'heure d'envoi | Aucun SMS pour l'annulé ; le SMS du déplacé porte la nouvelle date | mécanique | développeur |
| 14 | E3, cas limites de « la veille » | Rendez-vous du lundi ; rendez-vous pris après l'heure d'envoi pour le lendemain | Comportement conforme à la règle tranchée par le cabinet (voir Q1) ; aucun cas sans traitement | mécanique | développeur |
| 15 | E3, changement d'heure | Rendez-vous le 26/10/2026 à 8 h, puis le 29/03/2027 à 8 h | 1 SMS chacun, la veille à l'heure locale prévue ; aucun doublon ni oubli | mécanique | développeur |
| 16 | E3, panne du prestataire | Le prestataire factice répond erreur ou délai dépassé | Nouvelles tentatives bornées, puis échec visible au kiné ; aucune perte silencieuse | mécanique | développeur |
| 17 | E3, réception réelle | Envoi réel sur 5 téléphones, plusieurs opérateurs, noms accentués | Reçu en moins de 5 min `[proposed]`, émetteur lisible, accents intacts, date lisible | terrain | kiné ou secrétariat, avant ouverture |
| 18 | E8, consentement | Réserver sans cocher la case, puis répondre STOP | Case non précochée ; sans consentement, aucun SMS ; après STOP, plus aucun SMS pour ce numéro | mécanique | développeur |
| 19 | E6, annulation | Ouvrir le lien d'annulation, puis tester un lien altéré ou celui d'un autre rendez-vous | Créneau libéré, planning mis à jour, SMS supprimé ; lien altéré refusé ; jeton non devinable | mécanique | développeur |
| 20 | E7, fuite dans les traces | Planter une valeur-canari (nom, motif) dans une réservation, puis chercher dans URL, logs, outil d'erreurs et analytics | Canari trouvé nulle part hors de la base et du planning | mécanique | développeur ; données synthétiques |
| 21 | E7, conformité | Lire le certificat HDS de l'hébergeur, le registre RGPD, la mention d'information et la durée de conservation | Certificat valide, mention affichée à la réservation, durée écrite | relecture | juriste ou DPO |
| 22 | E7, effacement | Demande d'effacement d'un patient portant le canari ; chercher dans la base, ses fichiers annexes, les logs, les exports, les sauvegardes | Canari absent partout, ou présent seulement là où une durée de rétention est écrite | mécanique | développeur ; copie des fichiers |
| 23 | E7, sécurité de base | Tester l'accès en HTTP, l'accès sans connexion, les connexions répétées échouées | HTTPS imposé ; mots de passe hachés ; verrouillage ou ralentissement après échecs répétés | mécanique | développeur |
| 24 | E9, appareils réels | Réserver sur un vieil Android, Safari iOS, grande police, 4G | Réservation terminée en moins de 2 min `[proposed]`, sans élément coupé ; 2 patients non techniciens y arrivent sans aide | terrain | secrétariat, avant ouverture |
| 25 | E9, accessibilité | Navigation clavier, libellés, contrastes sur le parcours de réservation | Parcours complet sans souris ; libellés présents ; contrastes conformes | relecture | personne formée à l'accessibilité |
| 26 | Contenu, trous | Parcourir tous les écrans rendus (confirmation, erreur, planning vide, annulation, SMS, e-mails) | Aucun TODO, `[à compléter]`, lorem, `{{ }}` ou champ vide visible | mécanique | développeur |
| 27 | Contenu, cohérence | Comparer l'adresse, le téléphone, les horaires et la durée affichés à la configuration | Valeurs identiques partout où elles apparaissent | mécanique | développeur |
| 28 | Éléments nommés | Suivre chaque lien des SMS et e-mails ; vérifier les variables d'environnement et clés requises en production | Tous les liens répondent 200 ; aucune clé manquante au démarrage | mécanique | développeur |
| 29 | Charge | 30 patients simultanés `[proposed]` à l'ouverture de nouveaux créneaux, sur un environnement équivalent à la production | p95 < 2 s ; erreurs < 1 % ; aucune double réservation | mécanique | développeur |
| 30 | Fuseau | Réserver depuis un appareil réglé sur un autre fuseau | Heures affichées et enregistrées en Europe/Paris | mécanique | développeur |
| 31 | E10, coût et abus | Soumettre 100 réservations depuis une même adresse ou vers un même numéro ; chiffrer un mois de volume simulé | Plafond de SMS par numéro et par jour appliqué ; limitation du débit du formulaire ; coût mensuel ≤ budget `[à fournir]` | mécanique | développeur |
| 32 | Reprise après incident | Restaurer une sauvegarde sur un environnement vierge | Planning identique à l'original ; tâche de rappel opérationnelle | mécanique | développeur |
| 33 | E2, usage réel | Le kiné prépare sa journée avec le planning, sans aide, lors d'une répétition | Il dit qui vient et à quelle heure en moins de 30 s `[proposed]` ; ses retours sont consignés | terrain | le kiné |
| 34 | E3, formulation | Faire lire le SMS à 3 patients non informés | Les 3 comprennent le jour, l'heure, le lieu et comment annuler | relecture | kiné et 3 patients ; pas de données réelles |
| 35 | E11, issue | Comparer rendez-vous manqués, part de réservations en ligne et SMS remis à la zone ci-dessus | Au-dessus du plancher ; cible visée | terrain | le kiné, à 1 mois puis à 3 mois |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Les tests unitaires de l'envoi passent avec une horloge simulée, mais le SMS réel part à la mauvaise heure ou deux fois lors du changement d'heure du 25/10/2026 → lignes 15, 12, 17.
- Le planning affiche bien les rendez-vous, mais le chevauchement de durées différentes (30 et 45 min) n'est testé que créneau par créneau → ligne 3 (et H1).
- Le motif de consultation, saisi librement, est masqué à l'écran mais reste dans les logs ou le SMS → lignes 11, 20 (et H3).
- La suite ne teste que le parcours nominal d'un patient seul avec un bon réseau → lignes 3, 24, 29.
- Un rendez-vous annulé disparaît de l'écran, mais le SMS part quand même → ligne 13.
- Le patient peut lire ou annuler le rendez-vous d'un autre en changeant l'identifiant dans l'URL → lignes 8, 19 (et H7).
- Tout est vert, mais personne n'a vérifié qu'un patient reçoit réellement le SMS → ligne 17.
- Un agent en boucle modifie les tests ou ajoute un cas spécial pour les valeurs de test → section « Critère d'arrêt ».

## Non testable en l'état / Not testable as stated
- E3 « la veille » : pour un rendez-vous du lundi, le rappel part-il le dimanche, ou le vendredi ? Quelle heure d'envoi ? Quel comportement pour un rendez-vous pris après l'heure d'envoi ? Une réponse du cabinet suffit à rendre la ligne 14 décidable.
- E6 : y a-t-il un délai limite d'annulation en ligne (par exemple 24 h avant) ? Que se passe-t-il au-delà ?

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 28 | 7 | scripts, lancés par le juge hors de l'espace de l'auteur |
| relecture | 3 | 0 | juriste ou DPO, spécialiste accessibilité, 3 patients lecteurs |
| terrain | 4 | 0 | kiné et secrétariat, avant l'ouverture, puis à 1 et 3 mois |

Une boucle peut fermer les 35 lignes mécaniques, soit environ 80 % du plan. Elle ne peut pas fermer la conformité juridique, l'accessibilité, la réception réelle des SMS, l'usage par le kiné ni l'issue (E11), qui dépendent des patients et des opérateurs.

## Critère d'arrêt de la boucle / Loop stopping criterion
À appliquer seulement si l'auteur est un agent qui itère jusqu'au vert.
- La boucle s'arrête quand toutes les lignes mécaniques visibles et cachées passent. Le juge les lance hors de l'espace de l'agent ; le rapport de l'agent ne compte jamais.
- Les lignes de relecture et de terrain ne relèvent pas de la boucle. En cas d'échec, l'agent reçoit le numéro d'exigence et le symptôme visible, jamais l'entrée cachée ni la valeur attendue.
- L'instrument de mesure est protégé : fichiers de tests, fixtures, scripts de notation et configuration restent identiques à une somme de contrôle que garde le juge. Aucun test n'est ignoré, supprimé ou affaibli, et le nombre de tests et la couverture ne baissent pas.
- Aucun cas particulier pour les valeurs de test n'existe dans le code (recherche des valeurs littérales des fixtures dans les sources).
- Test des tests : désactiver la tâche de rappel, puis la détection de double réservation. La suite doit échouer dans les deux cas.

## Questions ouvertes / Open questions
- Q1 : règle exacte de « la veille » (jour, heure, week-end), voir plus haut.
- Q2 : un seul kiné ou plusieurs ? Un seul lieu ?
- Q3 : types de séance (première séance, suivi, durées différentes) ? Faut-il une ordonnance, et la demande-t-on en ligne ?
- Q4 : budget SMS mensuel, plafond de coût, et mesure de départ des rendez-vous manqués.
- Q5 : qui héberge, et le prestataire est-il certifié HDS ?
- Q6 : l'auteur est-il une personne ou un agent en boucle ?

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part
Chaque ligne teste une exigence déjà connue de l'auteur, avec d'autres entrées.

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E4, chevauchement de durées (garde la ligne 3) | Réserver un rendez-vous de 45 min à 9 h, puis tenter 9 h 30 en 30 min, 9 h 15 et 8 h 30 en 45 min, par appels API directs, en parallèle | Aucun chevauchement accepté ; le créneau suivant libre après la fin est accepté | mécanique | développeur ; données synthétiques |
| H2 | E3, jeu de 200 rendez-vous aléatoires (garde 10, 12, 15) | Jeu inconnu de l'auteur, incluant les 25-26/10/2026, le 29/03/2027, un lundi et un dimanche ; horloge accélérée | Nombre de SMS égal au nombre attendu, zéro doublon, heure locale correcte ; aucune valeur de test littérale dans le code | mécanique | développeur |
| H3 | E7, motif libre (garde 11, 20) | Saisir un motif avec le canari « HIDDEN-7731 » et un nom de 40 caractères avec accents et apostrophe | Canari absent du SMS, des logs, des URL et des traces d'erreur ; SMS en 2 segments au plus, date non tronquée | mécanique | développeur |
| H4 | E2, rejeu de 500 opérations aléatoires (garde 7) | Créations, annulations et déplacements aléatoires, avec recharges | Planning égal à la base après chaque opération | mécanique | développeur |
| H5 | E8, numéro partagé (garde 18) | Deux patients d'une même famille partagent un numéro ; l'un répond STOP ; saisir aussi le numéro en formats 06 et +33 6 | Comportement documenté et cohérent ; aucun SMS à un numéro désinscrit, quel que soit le format | mécanique | développeur |
| H6 | E6/E2, accès croisé (garde 8, 19) | Avec le lien du rendez-vous A, modifier l'identifiant, le jeton et la casse pour atteindre B ; essayer des identifiants consécutifs | Tous refusés ; aucun identifiant devinable | mécanique | développeur |
| H7 | E1/E4, charge sur autre créneau (garde 29, 3) | 60 patients simultanés sur 10 créneaux voisins, avec des annulations en cours de route | Aucune double réservation, p95 < 2 s, planning cohérent avec la base | mécanique | développeur |

Pourquoi ces lignes sont les plus exposées : H2, H3 et H4 portent sur des lignes dont un agent pourrait coder les valeurs de test, et H1, H6 et H7 reprennent des tests visibles avec d'autres entrées. H5 couvre un cas que le parcours nominal ignore.

Lignes visibles à surveiller : la 14 dépend de la réponse à Q1, et la 17 ne vaut que si elle est faite avant l'ouverture.