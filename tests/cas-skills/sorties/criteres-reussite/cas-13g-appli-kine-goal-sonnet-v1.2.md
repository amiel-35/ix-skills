<!-- Sortie brute de criteres-reussite 1.2.0, Sonnet, 0.18 $, 2 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: logiciel (application web de prise de rendez-vous avec rappels SMS, données de santé)
author: Claude Code, en boucle avec /goal
judge: à désigner. Vous acceptez, mais vous ne pouvez pas exécuter de scripts, donc il faut quelqu'un d'autre qui exécute (voir « Critère d'arrêt »)
requester: judge (vous), déduit de « c'est moi qui accepterai ». Ce plan est peut-être écrit dans la session de l'agent qui fera le travail, donc je n'écris pas de part cachée, seulement une demande scellée
---

# Critères de réussite : application de rendez-vous du cabinet de kinésithérapie

## Synthèse

**Ce qui est livré.** Les patients réservent en ligne, chacun des deux kinés voit son planning, et les patients reçoivent un rappel SMS la veille. Le volume est d'environ 120 RDV par semaine.

**Ce que « terminé » veut dire.** L'application passe tous ses tests automatiques. Les vérifications humaines et de terrain, que la boucle ne peut pas faire, sont ensuite passées sur vrais téléphones, avec de vrais patients, pendant un pilote de deux semaines.

**Chiffres.** 44 lignes : 30 mécaniques, 5 de relecture, 9 de terrain. Une boucle peut en fermer environ les deux tiers, mais ce tiers ne porte pas ce qui compte le plus : le vrai SMS reçu, la conformité de l'hébergement des données de santé, le pilote.

**Hypothèses `[inferred]`.**
- L'annexe `criteres_logiciel.md` n'était pas disponible. J'ai appliqué la méthode seule.
- Les données d'un cabinet de kiné sont des données de santé, donc hébergement HDS à vérifier.
- Le patient réserve sans créer de compte.
- Un évaluateur de `/goal` ne lit que la conversation (étape 13).

**Point à régler avant de lancer la boucle.** Vous ne pouvez pas exécuter les tests. Il faut une personne ou une session indépendante de l'agent qui écrit ou relit les scripts, les gèle et les rejoue. Sans cela, personne ne peut distinguer un vrai résultat d'un résultat inventé.

**Lignes bloquantes :** 3, 9, 10, 14, 20, 24, 28, 43.

## Exigences

| E | Exigence | Source | Livrable / issue |
|---|---|---|---|
| E1 | Les patients réservent en ligne | « les patients réservent en ligne » | livrable (le taux d'usage est une issue, voir E10) |
| E2 | Chaque kiné voit son planning | « chaque kiné voit son planning » | livrable |
| E3 | Rappel SMS la veille | « rappel par SMS la veille » | livrable (envoi) ; issue (le patient vient) |
| E4 | Pas de double réservation, ni de créneau fantôme | [inferred] thème | livrable |
| E5 | Données de santé protégées : hébergement HDS, accès, journaux, effacement, consentement SMS | [inferred] thème | livrable |
| E6 | Reprise sur panne : fournisseur SMS, application, sauvegarde | [inferred] thème | livrable |
| E7 | Absences, congés, RDV pris par téléphone, changement d'horaires | [inferred] thème | livrable |
| E8 | Accessible (patients âgés, mobile, clavier) | [inferred] thème | livrable |
| E9 | Vous restez propriétaire et autonome (comptes, modifications courantes) | « je ne suis pas développeur » | livrable |
| E10 | Moins d'oublis de RDV ; la réservation en ligne est adoptée | implicite | issue |

**Limites.** Environ 120 RDV par semaine, soit environ 520 SMS par mois. Budget et délai ne sont pas indiqués.

## Issue visée

| E | Issue | Plancher (échec en dessous) | Cible | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E10 | Taux de RDV non honorés | pas pire qu'avant : mesurez votre taux actuel avant le démarrage | baisse de [proposed] un tiers | vous, avant le travail | 8 semaines après le lancement |
| E10 | Part des RDV pris en ligne | [proposed] 20 % | [proposed] 50 % | vous | 3 mois après le lancement |
| E3 | Rappels reçus par les patients | [proposed] 95 % des RDV du lendemain | 99 % | vous | pilote (ligne 43) |

## Critères vérifiables

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 parcours nominal | Test de bout en bout : choisir un kiné et un créneau, saisir nom et mobile, confirmer | Le RDV apparaît dans le planning du bon kiné ; la confirmation affiche date, heure, kiné | mécanique | script gelé ; développeur indépendant |
| 2 | E1/E7 créneaux proposés | Lister les créneaux sur 4 semaines | Aucun créneau passé, hors horaires, en congé ou déjà pris | mécanique | idem |
| 3 | E4 concurrence | 20 requêtes simultanées sur le même créneau | Exactement 1 réussit ; les 19 autres voient un message clair et des créneaux voisins | mécanique | idem |
| 4 | E1 patients réels | Vous observez 5 personnes (dont 2 de plus de 65 ans), sans aide, sur leur téléphone | Au moins 4 sur 5 réservent en moins de 3 minutes [proposed] | terrain | vous, avec un observateur |
| 5 | E1 annulation | Annuler par le lien reçu, avant et après le délai limite (à fixer) | Avant : le créneau est libéré et le kiné prévenu. Après : refus clair avec le numéro du cabinet | mécanique | script ; développeur |
| 6 | E1 saisie | Téléphone invalide ou non mobile, nom vide, double soumission | Message clair, aucun RDV créé ou un seul RDV | mécanique | idem |
| 7 | E1/E3 lacunes | Chercher « TODO », « XXX », « lorem », « [à compléter] », champs vides, noms factices, dans les pages **rendues**, le texte du SMS et l'e-mail, dans tous les états | 0 occurrence | mécanique | script ; développeur |
| 8 | E2 planning | Connexion d'un kiné, vue jour et semaine, 30 RDV de test | Tous les RDV de ce kiné, à l'heure locale, avec nom et type | mécanique | script |
| 9 | E2/E5 isolation | Un patient change l'identifiant dans l'adresse ; un kiné tente l'API du collègue (si l'interdiction est confirmée) | Refus à chaque fois ; aucune donnée d'un autre patient n'est renvoyée | mécanique | développeur indépendant, test d'intrusion simple |
| 10 | E2/E5 sans connexion | Appeler pages et API du planning sans être connecté | Refus (401/403) partout | mécanique | idem |
| 11 | E7 congés | Un kiné bloque une plage qui contient déjà un RDV | Les créneaux disparaissent. Le RDV existant est signalé au kiné et n'est pas gardé en silence | mécanique | script |
| 12 | E7 RDV téléphonique | Le cabinet saisit un RDV à la main | Le créneau n'est plus réservable en ligne ; le RDV est visible dans le planning | mécanique | script |
| 13 | E2 appareil réel | Sur la tablette ou le téléphone de chaque kiné, créer une réservation en ligne | Elle apparaît dans le planning en moins de 60 s [proposed], lisible | terrain | chaque kiné |
| 14 | E3 rappel | Horloge simulée, 30 RDV demain | 30 SMS, un par RDV, à l'heure fixée (voir questions), un RDV du lundi rappelé le dimanche | mécanique | script ; développeur |
| 15 | E3 doublons | Relancer la tâche d'envoi, redémarrer le serveur en cours d'envoi | Toujours un seul SMS par RDV | mécanique | idem |
| 16 | E3 annulé ou tardif | RDV annulé avant l'envoi ; RDV créé après l'heure d'envoi pour le lendemain | Annulé : aucun SMS. Tardif : comportement conforme à la décision fixée (voir questions) | mécanique | idem |
| 17 | E3 contenu | Lire le SMS généré | Cabinet, date, heure, kiné, lien d'annulation ; aucun motif de soin ni pathologie ; accents corrects ; 2 segments au plus (320 caractères) [proposed] | mécanique | script |
| 18 | E3 changement d'heure | RDV le lundi 26/10/2026 à 8h, simulation du passage à l'heure d'hiver du 25/10 | Heure du RDV inchangée, rappel envoyé à l'heure locale prévue, ni avancé ni retardé d'une heure | mécanique | script |
| 19 | E6 panne SMS | Fournisseur simulé en panne : coupé, lent, refus d'authentification, quota épuisé | Nouvelles tentatives, puis liste visible au cabinet des patients non rappelés ; pas de plantage ; pas de doublon au retour | mécanique | script |
| 20 | E3 SMS réels | Envoyer de vrais rappels à 3 téléphones d'opérateurs différents | Reçus en moins de 5 minutes [proposed], expéditeur lisible, accents corrects | terrain | vous, avec 3 volontaires |
| 21 | E5 refus SMS | Un patient répond STOP ou demande à ne plus en recevoir | Plus aucun SMS ; le RDV reste valide ; aucun usage commercial | mécanique | script |
| 22 | E5 information | Lire le texte affiché à la réservation | Le patient est informé de l'envoi du SMS, de sa finalité et de son droit de refus | relecture | juriste ou DPO ; vous |
| 23 | E3/E6 plafond d'envoi | Provoquer une boucle d'envoi en test | Pas plus d'un SMS par RDV ; plafond journalier [proposed] de 2× le volume attendu, alerte au cabinet | mécanique | script |
| 24 | E5 hébergement | Le prestataire retenu est vérifié sur la liste officielle des hébergeurs certifiés HDS, certificat en cours de validité | Hébergeur certifié ; la simple mention écrite d'un statut « non conforme » est un échec | relecture | juriste ou DPO, indépendant de l'agent |
| 25 | E5 transport | Scan de l'adresse publique | HTTPS partout, HTTP redirigé, base de données non joignable depuis Internet | mécanique | développeur indépendant |
| 26 | E5 secrets | Chercher clés SMS et mots de passe dans le code, l'historique, les journaux et le code envoyé au navigateur | 0 occurrence | mécanique | script |
| 27 | E5 journaux | Faire des réservations avec un nom et un numéro repères, puis lire les journaux | Ni nom ni numéro en clair | mécanique | script |
| 28 | E5 effacement | Demander l'effacement d'un patient portant des repères uniques, puis chercher dans la base, les journaux, les exports, la file de SMS et les sauvegardes | Introuvable partout ; pour les sauvegardes, un délai maximal écrit et respecté [proposed 35 jours] | mécanique | développeur indépendant |
| 29 | E6 restauration | Restaurer la dernière sauvegarde sur un environnement vierge | Nombre de RDV et somme de contrôle identiques ; remise en route en 4 h au plus [proposed] ; coûteux [costly], à faire une fois | terrain | développeur indépendant |
| 30 | E6 application en panne | Application coupée : chaque kiné cherche sa liste du lendemain | Il peut l'obtenir à partir d'une copie vieille de 24 h au plus | terrain | chaque kiné, avec vous |
| 31 | E5 connexion | 10 mots de passe faux de suite ; réinitialisation du mot de passe | Compte verrouillé ou ralenti ; la réinitialisation fonctionne | mécanique | script |
| 32 | E4 charge | 50 visiteurs et 10 réservations en une minute | Aucune erreur ; 95 % des pages en moins de 2 s [proposed] | mécanique | script |
| 33 | E8 audit | Audit automatique d'accessibilité du parcours de réservation | 0 anomalie critique | mécanique | script |
| 34 | E8 manuel | Parcours au clavier, zoom à 200 %, lecteur d'écran | Réservation possible sans souris, rien de tronqué | relecture | relecteur indépendant |
| 35 | E8 mobile | iPhone (Safari) et Android (Chrome) réels, écran de 360 px | Pas de défilement horizontal ; boutons utilisables | terrain | vous |
| 36 | E1 liens | Parcourir tous les liens et pages annoncés | Aucun lien mort ; chaque page citée existe | mécanique | script |
| 37 | E1 infos cabinet | Comparer adresse, horaires, durées de séance, tarifs affichés avec votre liste | Identiques ; chaque chiffre a une source | relecture | vous |
| 38 | E5 mentions légales | Lire mentions légales et politique de confidentialité | Identité réelle du cabinet, responsable du traitement, contact pour les droits ; aucun texte générique | relecture | juriste ou DPO ; vous |
| 39 | E9 propriété | Vous vous connectez vous-même, comme propriétaire, à l'hébergement, au compte SMS, au dépôt du code et au nom de domaine | Les quatre fonctionnent ; l'accès ne dépend pas de l'agent | terrain | vous |
| 40 | E9 autonomie | Suivre le mode d'emploi pour ajouter un kiné, changer les horaires, poser un congé | Chaque opération faite sans aide en moins de 10 minutes [proposed] | terrain | vous |
| 41 | E7 horaires | Changer les horaires d'un kiné | Les nouveaux créneaux sont modifiés, les RDV existants hors horaires sont signalés | mécanique | script |
| 42 | E5 test en production | Compter les lignes de test en production ; couper le réseau pendant les tests | 0 patient factice en production ; les tests n'envoient aucun SMS réel | mécanique | script |
| 43 | E3/E10 pilote | 2 semaines en parallèle de votre agenda actuel | 0 RDV perdu ou divergent ; au moins 95 % des RDV du lendemain rappelés | terrain | vous et les deux kinés |
| 44 | Boucle : instrument | Somme de contrôle des tests et des fixtures, nombre de tests | Identiques au gel ; aucun test sauté, supprimé ou affaibli | mécanique | juge indépendant |

## Ce qui passerait et serait faux

- Les tests passent avec un SMS simulé, mais le vrai SMS ne part pas (clé, expéditeur refusé, filtrage par l'opérateur) → ligne 20.
- Le planning est correct pour le kiné connecté, mais un patient ou le collègue atteint des données par une adresse directe → lignes 9 et 10.
- Un patient « effacé » disparaît de l'écran mais reste dans les journaux ou les sauvegardes → ligne 28.
- Le statut d'hébergement est écrit noir sur blanc dans un document, mais l'hébergeur n'est pas certifié → ligne 24.
- Le rappel est bon en général mais décalé d'une heure lors du changement d'heure du 25 octobre → ligne 18.
- Tout marche un patient à la fois, et deux patients réservent le même créneau → ligne 3.
- L'agent modifie ou saute un test pour finir → ligne 44.
- Les écrans sont conformes, mais un patient de 70 ans n'arrive pas à réserver → ligne 4.

## Non testable en l'état

- **Conservation des données** (E5) : durée non fixée. Combien de temps garde-t-on un RDV passé ?
- **Qualité de la prise en charge ressentie** : critère à observer plutôt qu'à tester. Quels signes reconnaîtriez-vous (moins d'appels, moins d'oublis) ?

## Couverture

| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 30 | demandées | scripts gelés, rejoués par le juge qui exécute |
| relecture | 5 | — | développeur, juriste ou DPO, vous |
| terrain | 9 | — | vous, les deux kinés, volontaires |

La boucle peut fermer les lignes mécaniques, soit environ deux tiers des lignes. Elle ne peut pas fermer le vrai SMS, l'hébergeur HDS, la lisibilité par de vrais patients, la restauration ni le pilote. Atteindre le but de la boucle signifie « prêt pour acceptation », pas « accepté ».

## Critère d'arrêt de la boucle

Deux cas s'appliquent.

**Évaluateur qui ne lit que la conversation (étape 13).**
- Il ne peut fermer que les lignes mécaniques visibles : 1, 2, 3, 5, 7, 9, 10, 14 à 19, 21, 23, 26, 27, 28, 42, 44.
- Il ne peut pas distinguer une sortie fabriquée d'une sortie réelle. Son verdict ne vaut jamais acceptation.
- Les lignes de relecture, de terrain et la part cachée sont jouées après la boucle, hors de la session de l'agent, par un juge qui exécute.

**Juge qui exécute (étape 12), après la boucle.**
- Les scripts mécaniques sont écrits ou relus ligne à ligne par une personne indépendante, puis gelés avant le premier tour. Un script écrit par l'agent et non relu compte comme relecture.
- La boucle s'arrête quand toutes les lignes mécaniques visibles passent et que les lignes mécaniques cachées, rejouées par le juge hors de l'espace de travail de l'agent, passent aussi. Jamais sur le rapport de l'agent.
- Les tests, fixtures et scripts de notation restent inchangés, sans test sauté ni supprimé.
- Un échec renvoie l'agent avec l'exigence en cause et le symptôme visible, jamais l'entrée cachée ni la valeur attendue.

**Texte du but à donner à `/goal` :**

> But : l'application de rendez-vous du cabinet est prête pour acceptation.
> Une ligne ne compte comme réussie que si tu montres dans la conversation la commande exacte et sa sortie brute complète. Aucun résumé n'est accepté.
> Lignes visibles à fermer : 1, 2, 3, 5, 7, 9, 10, 14, 15, 16, 17, 18, 19, 21, 23, 26, 27, 28, 42 et 44.
> Règles de protection de l'instrument :
> 1. Les tests ont été écrits ou relus par le juge et gelés avant le début. Tu ne modifies ni les tests, ni les fixtures, ni les scripts de notation.
> 2. À chaque tour, tu affiches la somme de contrôle des fichiers de test et le nombre de tests, et ils doivent être identiques à ceux du gel.
> 3. Aucun test n'est sauté, supprimé, marqué comme attendu en échec, ni affaibli.
> Tu n'envoies aucun vrai SMS et tu n'utilises aucune vraie donnée de patient.
> Le but est atteint quand toutes les lignes listées passent avec ces preuves. Les lignes de relecture, de terrain et les contrôles supplémentaires sont réservés au juge, après la boucle.

## Questions ouvertes

- À quelle heure part le rappel « la veille » (par exemple 18 h) ? Que fait-on d'un RDV pris après cette heure pour le lendemain ?
- Jusqu'à quelle heure avant le RDV un patient peut-il annuler seul ?
- Chaque kiné voit-il seulement son planning, ou aussi celui de l'autre ? Qui saisit les RDV pris par téléphone ?
- Faut-il gérer les séries de séances prescrites (10 séances), les types de séances et leurs durées, les mineurs ?
- Quelle durée de conservation des données ? Quel hébergeur HDS et quel fournisseur SMS ? Budget mensuel de SMS ?
- Quel est votre taux actuel de RDV non honorés ? Il fixe le plancher.
- Qui est le juge qui exécute, et pour combien d'heures ?

✂ ----- À TRANSMETTRE AU JUGE -----

## Demande de part cachée

Environ 14 lignes cachées, au moins deux par exigence gardée. Le juge choisit les exigences à garder.

Juge : lancez `criteres-reussite` avec `requester: judge`, ce brief et le plan visible ci-dessus, dans une session que l'agent qui construit l'application ne peut pas lire, et gardez pour vous ce qui en sort.