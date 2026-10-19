<!-- Sortie brute de criteres-reussite 1.2.0, Sonnet, 0.21 $, 2 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: logiciel (application web de prise de rendez-vous avec rappels SMS)
author: non précisé [inferred : une personne ou une équipe de développement ; à préciser si c'est un agent en boucle]
judge: non précisé, « quelqu'un d'autre que l'auteur »
requester: author [inferred : rien dans la demande ne permet de dire qui la formule, donc traité comme auteur ; aucune part cachée n'est écrite, seulement une demande scellée]
---

# Critères de réussite — Application de rendez-vous pour un cabinet de kinésithérapie

## Synthèse / Summary
On livre une application où les patients réservent en ligne, où le kiné consulte son planning et où chaque patient reçoit un SMS de rappel la veille. « Terminé » veut dire ceci : aucun créneau n'est réservé deux fois, le planning du kiné correspond exactement aux réservations, chaque rendez-vous valide reçoit un seul SMS au bon moment, et les données de santé sont hébergées et effaçables comme la règle l'exige.

44 lignes : 34 mécanique, 3 relecture, 7 terrain. Une boucle automatique peut en fermer environ trois quarts. Cela couvre la logique de réservation et de rappel, mais pas l'arrivée réelle des SMS, l'usage sur de vrais téléphones, la conformité de l'hébergement ni le résultat voulu (moins d'absences).

Hypothèses faites sans interlocuteur, marquées [inferred] :
- Un seul cabinet, avec un ou plusieurs kinés (non précisé).
- Le patient réserve sans compte, avec nom et téléphone mobile.
- Les données de rendez-vous chez un kiné sont des données de santé (à confirmer par le DPO).
- L'annexe logiciel (partie A) a été appliquée. La partie B ne l'a pas été, car il n'y a pas de session en direct.
- La charge est déduite du brief : quelques patients en même temps, pas un pic de masse.

Lignes bloquantes / Blocking lines : 1, 3, 4, 10, 12, 14, 21, 24, 28.
Noyau / Core : sans objet, le plan a moins de 45 lignes.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Un patient réserve un créneau en ligne | « les patients réservent en ligne » | livrable |
| E2 | Le kiné voit son planning, complet et exact | « le kiné voit son planning » | livrable |
| E3 | Chaque patient reçoit un SMS de rappel la veille | « un rappel par SMS la veille » | livrable (envoi) / issue (réception) |
| E4 | Aucun créneau n'est réservé deux fois ni hors disponibilités | [inferred] | livrable |
| E5 | Le patient peut annuler ou déplacer son rendez-vous, et le rappel suit | [inferred] | livrable |
| E6 | Le numéro est utilisable pour un SMS, le patient est informé, et il peut refuser le rappel | [inferred] | livrable |
| E7 | Données de santé : hébergement conforme, minimisation, pas de fuite dans les journaux ni chez des tiers | [inferred] | livrable |
| E8 | Un patient peut obtenir l'effacement de ses données, jusque dans les fichiers | [inferred] | livrable |
| E9 | Un patient ne voit rien des autres ; seul le kiné authentifié voit le planning | [inferred] | livrable |
| E10 | Les heures sont justes (Europe/Paris, changement d'heure) | [inferred] | livrable |
| E11 | Une panne du SMS ou du service ne perd aucune réservation | [inferred] | livrable |
| E12 | Le cabinet règle horaires, absences et saisies manuelles (réservations par téléphone) sans développeur | [inferred] | livrable |
| E13 | Utilisable sur mobile et accessible | [inferred] | livrable |
| E14 | Résiste aux abus et à la charge normale | [inferred] | livrable |
| E15 | Aucun trou de contenu dans ce que voit le patient ; liens et chiffres existent et concordent | [inferred] | livrable |
| E16 | Moins de rendez-vous manqués, et les patients adoptent la réservation en ligne | [inferred : but du rappel] | issue |

Limites, pas des exigences : budget, délai et coût des SMS ne sont pas donnés dans le brief.

## Issue visée / Outcome zone
| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E16 | Taux de rendez-vous non honorés | Pas pire que le taux actuel du cabinet (à relever avant le démarrage) | Réduit d'un tiers [proposed] | Le kiné, avant le démarrage | 3 mois après la mise en service |
| E16 | Part des rendez-vous pris en ligne | À fixer par le cabinet | À fixer par le cabinet | Le kiné | 3 mois après la mise en service |
| E3 | SMS délivrés, selon le rapport de la passerelle | 90 % des envois [proposed] | 97 % [proposed] | Le kiné, sur avis du fournisseur SMS | Chaque mois |

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 — Parcours nominal | Test bout en bout : choisir un type de séance et un créneau, saisir nom et mobile, confirmer | Écran de confirmation affiché ; le rendez-vous est dans le planning du kiné en moins d'une minute [proposed] | mécanique | Développeur autre que l'auteur ; données synthétiques |
| 2 | E1, E12 — Créneaux proposés | Interroger l'API des créneaux sur un cabinet de test (horaires, durées, jours fériés, absences configurés) | 0 créneau proposé hors horaires, un jour férié, pendant une absence ou dans le passé | mécanique | Développeur autre que l'auteur |
| 3 | E4 — Concurrence | Lancer 20 réservations simultanées du même créneau | Exactement 1 réussit ; 19 reçoivent un message clair avec d'autres créneaux ; 1 seule ligne en base | mécanique | Développeur autre que l'auteur |
| 4 | E4 — Règles côté serveur | Appeler directement l'API de réservation : créneau pris, passé, hors horaires, durée non permise | Chaque appel refusé avec une erreur, aucun enregistrement créé | mécanique | Développeur autre que l'auteur |
| 5 | E1 — Confirmation | Chercher dans la confirmation rendue : date, heure, adresse du cabinet, moyen d'annuler | Les quatre éléments sont présents et exacts | mécanique | Développeur autre que l'auteur |
| 6 | E5 — Annulation | Annuler par le lien reçu, sans compte | Créneau de nouveau réservable, planning à jour, aucun SMS envoyé pour ce rendez-vous | mécanique | Développeur autre que l'auteur |
| 7 | E5, E3 — Déplacement | Déplacer un rendez-vous d'un jour à un autre, puis lancer la tâche de rappel avec l'horloge simulée | Rappel envoyé la veille de la nouvelle date seulement, avec la nouvelle heure ; aucun pour l'ancienne | mécanique | Développeur autre que l'auteur |
| 8 | E2 — Planning exact | Semer 30 rendez-vous variés (dont annulés et déplacés), comparer le planning affiché à la base | Mêmes 30 rendez-vous au même jour et à la même heure ; 0 manquant, 0 en trop, 0 annulé affiché comme actif | mécanique | Développeur autre que l'auteur |
| 9 | E2 — Planning en conditions réelles | Le kiné utilise le planning pendant une semaine, parallèlement à son agenda habituel | 0 écart signalé entre les deux sur la semaine | terrain | Le kiné, relevé à la fin de la semaine |
| 10 | E9 — Accès au planning | Appeler les routes du planning sans connexion, puis avec un jeton de patient | Refus (401/403) dans les deux cas ; aucune donnée renvoyée | mécanique | Développeur autre que l'auteur |
| 11 | E9 — Connexion du kiné | 20 tentatives de mot de passe erroné | Verrouillage ou temporisation dès 5 essais [proposed] ; aucune information ne dit si l'identifiant existe | mécanique | Développeur autre que l'auteur |
| 12 | E3 — Sélection des rappels | Horloge fixée, jeu de rendez-vous : lendemain, autre jour, annulé, passé, déjà rappelé | SMS envoyé uniquement pour les rendez-vous confirmés du lendemain ; exactement 1 par rendez-vous | mécanique | Développeur autre que l'auteur |
| 13 | E3 — Moment d'envoi | Faire tourner la tâche avec l'horloge simulée sur plusieurs jours, dont un lundi et un lendemain de férié | Envoi dans la plage horaire décidée par le cabinet (question ouverte 1), avec la règle choisie pour lundi et lendemain de férié | mécanique | Développeur autre que l'auteur |
| 14 | E3 — Une seule fois | Lancer la tâche deux fois de suite, puis la tuer en cours de route et la relancer | Chaque patient reçoit exactement 1 SMS ; 0 doublon, 0 oubli | mécanique | Développeur autre que l'auteur |
| 15 | E10 — Changement d'heure | Rendez-vous à 09:00 le lundi 26 octobre 2026 (lendemain du passage à l'heure d'hiver), réservé avant le changement | « 09:00 » affiché partout (patient, planning, SMS) ; rappel envoyé la veille à l'heure locale prévue | mécanique | Développeur autre que l'auteur |
| 16 | E3, E15 — SMS rendu | Produire chaque variante de SMS (réservation, déplacement) et chercher les motifs `TODO`, `TBD`, `XXX`, `lorem`, `[à compléter]`, `{{`, `undefined`, `null` ; compter les segments | 0 motif trouvé ; date, heure et nom du cabinet présents ; longueur ≤ 2 segments [proposed] | mécanique | Développeur autre que l'auteur |
| 17 | E3, E7 — Contenu du SMS | Lire les SMS : un lecteur sans lien avec le projet dit ce qu'il comprend | Il identifie le cabinet, le jour et l'heure, et sait comment annuler ; le SMS ne contient aucune information de soin (pathologie, type de séance) | relecture | Lecteur sans enjeu ; DPO pour la partie données |
| 18 | E11 — Passerelle SMS en panne | Réserver, puis lancer les rappels avec la passerelle injoignable | La réservation est enregistrée et confirmée ; l'échec est consigné ; le kiné voit la liste des rappels non envoyés ; un nouvel essai a lieu | mécanique | Développeur autre que l'auteur |
| 19 | E11 — Un numéro en échec | Parmi 10 envois, 1 numéro refusé par la passerelle | Les 9 autres partent ; l'échec est visible côté kiné | mécanique | Développeur autre que l'auteur |
| 20 | E3 — Réception réelle | Envoyer les rappels de la veille à 10 vrais téléphones d'opérateurs différents | Chaque SMS arrive dans l'heure [proposed] qui suit l'envoi, avec un expéditeur lisible ; relevé tenu | terrain | Le cabinet et un développeur, avant la mise en service |
| 21 | E6 — Numéro utilisable | Saisir un fixe (01…), des lettres, un numéro trop court, puis +33 6…, 06…, 07… | Les trois premiers cas sont refusés avec un message ; les mobiles valides sont acceptés et normalisés | mécanique | Développeur autre que l'auteur |
| 22 | E6 — Information du patient | Lire le formulaire et la page de confidentialité : usage du numéro, responsable, durée, droits | Chaque point est présent, sans trou, et le SMS de rappel n'a pas de contenu promotionnel | relecture | DPO ou juriste autre que l'auteur |
| 23 | E6 — Refus du rappel | Réserver en refusant le rappel, puis lancer la tâche | Aucun SMS envoyé ; réservation conservée | mécanique | Développeur autre que l'auteur |
| 24 | E7 — Hébergement | Vérifier le certificat de l'hébergeur, son périmètre (le service réellement utilisé) et le contrat | L'hébergement est conforme à ce que la règle exige pour des données de santé, pas seulement « documenté » | relecture | Juriste ou DPO autre que l'auteur |
| 25 | E7 — Minimisation et tiers | Capturer le trafic des pages de réservation | Champs collectés = nom, mobile, créneau, type de séance ; 0 appel à un tiers (statistiques, polices, publicité) sans consentement | mécanique | Développeur autre que l'auteur |
| 26 | E7 — Journaux | Faire un test avec un nom et un téléphone « canari », puis chercher dans journaux, suivi d'erreurs et journaux de la passerelle | Canari trouvé uniquement aux endroits listés avec leur durée de conservation | mécanique | Développeur autre que l'auteur, sur copie |
| 27 | E8 — Effacement | Planter un canari, demander l'effacement, chercher dans le fichier de base et ses fichiers annexes, journaux, caches, exports, sauvegardes, passerelle SMS [costly pour sauvegardes et fournisseur] | Canari introuvable, ou son emplacement écrit avec sa durée de conservation | mécanique | Développeur autre que l'auteur, sur copie |
| 28 | E9 — Rien sur les autres | Chercher noms, numéros et identifiants d'autres patients dans toutes les réponses côté patient (HTML, JSON, scripts) | 0 occurrence ; réserver avec un numéro déjà connu ne révèle rien sur le patient existant | mécanique | Développeur autre que l'auteur |
| 29 | E5, E9 — Jeton d'annulation | Essayer un jeton modifié, le jeton d'un autre rendez-vous, un jeton après le rendez-vous | Refus dans tous les cas | mécanique | Développeur autre que l'auteur |
| 30 | E13 — Mobile réel | 5 personnes qui ne connaissent pas l'outil (dont 2 de plus de 65 ans) réservent sur leur téléphone (iOS Safari, Android Chrome, écran 360 px) | Les 5 réussissent en moins de 3 minutes [proposed] sans aide | terrain | Le cabinet ; observateur autre que l'auteur |
| 31 | E13 — Audit automatique | Lancer un audit d'accessibilité sur les pages de réservation et de confirmation | 0 erreur critique | mécanique | Développeur autre que l'auteur |
| 32 | E13 — Clavier et lecteur d'écran | Réserver au clavier seul, puis avec un lecteur d'écran | Parcours terminé dans les deux cas | terrain | Personne maîtrisant ces outils, autre que l'auteur |
| 33 | E14 — Abus | Un script tente de prendre 50 créneaux avec un numéro ou une adresse IP | Au plus 3 rendez-vous futurs par numéro [proposed] ; le reste est refusé | mécanique | Développeur autre que l'auteur |
| 34 | E14 — Charge | 20 réservations simultanées sur un environnement comparable [proposed] | Page de créneaux en moins de 2 s au 95e centile ; 0 erreur | mécanique | Développeur autre que l'auteur |
| 35 | E11 — Service injoignable | Répétition à blanc : couper le service le matin d'une journée de consultations | Le kiné peut quand même connaître les patients et horaires du jour (résultat à obtenir, moyen laissé libre) | terrain | Le kiné, avant la mise en service |
| 36 | E12 — Absence sur rendez-vous existants | Déclarer une absence couvrant 3 rendez-vous déjà pris | Le kiné est averti avec la liste des patients concernés ; aucun n'est laissé en silence | mécanique | Développeur autre que l'auteur |
| 37 | E12, E4 — Saisie manuelle | Le kiné enregistre un rendez-vous pris par téléphone | Ce créneau n'est plus proposé en ligne ; le patient reçoit son rappel s'il a un mobile | mécanique | Développeur autre que l'auteur |
| 38 | E15 — Pages rendues | Produire toutes les pages vues par un patient et le kiné (états, erreurs, 404) et chercher les motifs de la ligne 16 | 0 occurrence dans les pages rendues | mécanique | Développeur autre que l'auteur |
| 39 | E15 — Liens et éléments cités | Suivre chaque lien des pages et des SMS (annulation, confidentialité, mentions) | Tous répondent 200 ; mentions légales et page de confidentialité existent | mécanique | Développeur autre que l'auteur |
| 40 | E15 — Chiffres concordants | Comparer adresse, téléphone et horaires du cabinet entre pages, confirmation et SMS | Identiques et conformes à la configuration | mécanique | Développeur autre que l'auteur |
| 41 | E1 — Rechargement, retour, double clic | Double clic sur « Confirmer », retour arrière, rechargement de la confirmation | 1 seul rendez-vous créé ; l'écran reste cohérent | mécanique | Développeur autre que l'auteur |
| 42 | Tous — Les tests eux-mêmes | Retirer volontairement la fonction visée par chaque test des lignes bloquantes | Chacun de ces tests échoue | mécanique | Développeur autre que l'auteur |
| 43 | E16 — Rendez-vous non honorés | Relever le taux avant et 3 mois après la mise en service | Dans la zone de la section « Issue visée » | terrain | Le kiné ; relevé daté |
| 44 | E16 — Adoption | Relever la part des rendez-vous pris en ligne à 3 mois | Dans la zone de la section « Issue visée » | terrain | Le kiné |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Tous les SMS passent avec une passerelle simulée qui répond toujours « OK », alors qu'un fixe saisi ne recevra jamais rien → lignes 21, 20.
- Un rendez-vous annulé ou déplacé est quand même rappelé à son ancienne date → lignes 6, 7.
- Les tests tournent en UTC avec une horloge simulée et tout est bon, mais le lundi 26 octobre le rappel part une heure trop tôt ou trop tard → ligne 15.
- Le planning paraît juste sur 3 rendez-vous et en manque 5 sur 30 → ligne 8.
- Les noms d'autres patients sont masqués à l'écran mais présents dans le JSON → ligne 28.
- L'hébergement est « documenté » avec la mention « non certifié » → ligne 24.
- L'effacement vide l'écran mais le nom reste dans le fichier de base ou chez le fournisseur SMS → ligne 27.
- Une absence posée sur des rendez-vous existants les laisse silencieusement dans le planning → ligne 36.
- Le test d'envoi lit seulement le journal de l'application (« envoyé ») et non le rapport de livraison de la passerelle → lignes 20, 18.

## Non testable en l'état / Not testable as stated
- E3 — « la veille » n'est pas défini (heure d'envoi ; rendez-vous du lundi ou du lendemain de férié ; rendez-vous tôt le matin) — À quelle heure, et quel jour pour un lundi ? Sans réponse, la ligne 13 ne peut pas avoir de seuil.
- E5 — Délai limite d'annulation en ligne absent du brief — Après quel délai le patient doit-il téléphoner ?
- E8 — Durée de conservation des rendez-vous passés absente — Combien de temps, et efface-t-on ou anonymise-t-on ?
- E7 — Qualification « données de santé » et exigence d'hébergement : à trancher par le DPO avant la ligne 24.

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 34 | voir demande scellée | scripts, exécutés par le juge (développeur autre que l'auteur) |
| relecture | 3 | — | DPO ou juriste ; lecteur sans enjeu |
| terrain | 7 | — | le cabinet (kiné, patients, téléphones), avant et 3 mois après la mise en service |

Une boucle peut fermer les 34 lignes mécaniques, soit environ trois quarts du plan. Elle ne dit rien de l'arrivée réelle des SMS, de l'hébergement, de l'usage sur de vrais téléphones ni de la baisse des absences : les lignes 20, 24, 30, 32, 35, 43 et 44 pèsent donc davantage que leur nombre.

## Questions ouvertes / Open questions
1. À quelle heure part le rappel, et que se passe-t-il pour un rendez-vous du lundi ou du lendemain de férié ?
2. Un seul kiné ou plusieurs agendas ? Chaque praticien voit-il uniquement le sien ?
3. Le cabinet prend-il aussi des rendez-vous par téléphone (ligne 37 repose sur cette hypothèse) ?
4. Quel fournisseur SMS et quel hébergeur sont prévus, et où sont-ils situés ?
5. Délai d'annulation et durée de conservation (voir « Non testable »).
6. Si l'auteur est un agent qui itère jusqu'à ce que les tests passent : relancer cette compétence avec `author` renseigné pour obtenir le critère d'arrêt (tests gelés par le juge avant la première boucle, somme de contrôle, aucun test supprimé ou affaibli).

✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Environ 12 lignes cachées, au moins deux par exigence gardée. Le juge choisit les exigences à garder.
Juge : lancer `criteres-reussite` avec `requester: judge`, ce brief et le plan visible ci-dessus, dans une session que l'auteur ne peut pas lire, et garder pour soi ce qui en sort.