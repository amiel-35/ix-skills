# ix-skills

Skills de knowledge-work atomiques — portables sur Claude, GPT, Gemini, mystaffy.

78 skills en 10 catégories. Chaque skill encode un **processus cognitif**, pas une expertise métier.

[🇬🇧 English version](README.md)

---

## Skills disponibles

### 🧠 Cognitif — atomes de processus

Opérations primitives sur un contenu, un problème ou une décision. Chaque skill encode un seul geste cognitif — ils sont conçus pour se chaîner, pas se substituer.

| id | Rôle | Contrainte clé |
|---|---|---|
| `critique` | Identifier les failles d'un contenu sans proposer de solution | Analyse seulement — **ne corrige pas** |
| `correction` | Transformer une critique en directives actionnables | Transforme une critique — **ne ré-analyse pas** |
| `simplify` | Épurer un contenu sans changer le fond | Préserve toute l'information — supprime la friction |
| `rephrase` | Restituer le sens réel d'un contenu dense ou ambigu | Réinterprète — le sens peut évoluer, pas seulement la forme |
| `explorer` | Générer un espace d'options sans trancher | Largeur — **ne choisit pas** |
| `decision` | Arbitrer avec trade-offs visibles et recommandation nette | Choisit parmi des options existantes — **n'en génère pas** |
| `deliver` | Transformer un artifact en livrable partageable | Mise en forme et calibrage audience |
| `research` | Construire un socle factuel sourcé avant toute décision | Sources obligatoires — aucune affirmation non sourcée |
| `synthese` | Condenser un long contenu en synthèse actionnable | Compression avec perte — le détail est sacrifié intentionnellement |
| `decomposer` | Structurer un problème complexe en sous-problèmes indépendants | Les sous-problèmes doivent être indépendants — pas de dépendances croisées |
| `revue-feedback` | Évaluer un feedback avant de l'accepter ou le refuser | Évalue une critique reçue — pas votre propre artifact |

#### Distinctions clés

**`critique` vs `revue-feedback`**
`critique` analyse *votre propre artifact* (un document, un plan, une proposition) pour en trouver les failles. `revue-feedback` traite *un feedback que quelqu'un d'autre vous a donné* — il évalue si vous devez l'accepter, le nuancer ou le refuser avant de répondre. L'un est éditorial, l'autre est diplomatique.

**`simplify` vs `rephrase` vs `synthese`**
- `simplify` supprime le bruit en conservant toute l'information — le résultat est plus court mais complet.
- `rephrase` réécrit un contenu dense ou ambigu pour rendre le sens réel lisible — il réinterprète, ne coupe pas seulement.
- `synthese` sacrifie délibérément le détail pour extraire l'essentiel — compression avec perte qui produit une synthèse actionnable.

**`explorer` vs `decision`**
Conçus pour fonctionner en séquence. `explorer` cartographie l'espace des options sans s'engager (d'abord en largeur). `decision` arbitre parmi des options existantes avec des trade-offs explicites et une recommandation (en profondeur). Lancer `decision` sans `explorer` risque de figer le choix trop tôt sur un espace incomplet.

**`critique` vs archétypes Advisory (ex. `dixieme-homme`, `contrarian`)**
`critique` est un contrôle qualité sur *votre propre artifact* — éditorial, il trouve les failles dans ce que vous avez produit. Les archétypes Advisory challengent *une croyance, un plan ou une décision* depuis une perspective spécifique — ils opèrent au niveau du raisonnement et des convictions, pas de la qualité textuelle. Utilisez `critique` pour améliorer un document ; utilisez un archétype Advisory pour stress-tester une conclusion.

---

### ⚔️ Conseil — archétypes de perspective

Chaque skill impose une posture cognitive spécifique. Ils ne sont pas interchangeables — choisir en fonction de ce qu'on veut stress-tester. Lancer `chairman` après plusieurs pour synthétiser.

---

#### `contrarian` — Points de défaillance et hypothèses non vérifiées

**Origine :** L'*advocatus diaboli* (avocat du diable), formalisé dans le droit canon catholique. L'Église exigeait un critique désigné pour plaider contre toute canonisation proposée, pour garantir la rigueur. Adopté dans la gestion de la décision et l'analyse de renseignement pour institutionnaliser la dissidence.

**Objectif :** Forcer la confrontation avec la façon la plus probable dont votre plan échoue — avant de vous engager.

**Fonctionnement :** Identifie le seul argument le plus solide contre votre décision, fait surface les hypothèses non validées, et nomme la condition dans laquelle tout s'effondre. Délibérément à sens unique vers l'échec, pas une revue équilibrée.

**Quand l'utiliser :** Vous avez un plan auquel vous croyez et voulez en trouver la vulnérabilité principale avant de le présenter ou l'exécuter. Différent de `dixieme-homme` (qui construit une thèse adverse complète) ou de `red-team` (qui raisonne comme un adversaire externe).

---

#### `executor` — Est-ce que ça tient dans la réalité ?

**Origine :** La technique du *pré-mortem*, développée par Gary Klein (1989). Plutôt que demander "qu'est-ce qui pourrait mal tourner ?", on imagine que le plan a déjà échoué et on remonte pour expliquer pourquoi.

**Objectif :** Ancrer les plans abstraits dans la réalité opérationnelle avant le lancement.

**Fonctionnement :** Teste si le plan est réellement exécutable — ressources manquantes, délais irréalistes, dépendances cachées, facteurs humains ignorés par la réflexion stratégique. La perspective est celle de quelqu'un qui doit livrer, pas concevoir.

**Quand l'utiliser :** Après qu'un plan est formé, avant que l'exécution commence. Particulièrement utile pour les plans construits par des personnes qui ne seront pas celles qui les exécutent.

---

#### `expansionist` — L'upside manquant

**Origine :** Le concept de *possible adjacent* du théoricien de la complexité Stuart Kauffman — à tout moment, les possibilités adjacentes sont déterminées par ce qui existe déjà. Appliqué à la stratégie pour révéler les options qu'on n'a pas considérées parce qu'elles n'étaient pas évidentes depuis la position de départ.

**Objectif :** Éviter le rétrécissement de scope et les leviers manqués en cartographiant ce qui est adjacent à la position actuelle.

**Fonctionnement :** Cartographie les marchés adjacents, partenariats possibles, angles inexploités et leviers non nommés. Délibérément optimiste et génératif — pas une analyse de risques.

**Quand l'utiliser :** Vous avez défini une stratégie ou une offre et voulez vérifier si vous avez laissé de l'upside évident sur la table.

---

#### `firstprinciples` — La vraie question sous la question

**Origine :** Raisonnement par premiers principes aristotélicien et méthode socratique. Popularisé en technologie par Elon Musk — plutôt que demander "comment acheter des fusées moins cher ?", SpaceX a demandé "quels sont les coûts réels des matières premières d'une fusée ?" et a construit à partir de là.

**Objectif :** Dissoudre les fausses contraintes en revenant aux vérités fondamentales. Séparer ce qui est réellement vrai de ce qui est simplement conventionnel.

**Fonctionnement :** Supprime la pensée analogique ("on fait comme ça parce que tout le monde fait comme ça") pour trouver la vraie question à laquelle répondre, et les vraies contraintes par opposition aux contraintes héritées.

**Quand l'utiliser :** Un problème semble insoluble, les réponses conventionnelles semblent insuffisantes, ou vous suspectez de résoudre le mauvais problème.

---

#### `outsider` — Lu à froid, sans contexte implicite

**Origine :** La technique du "regard de l'étranger" issue de la communication et du renseignement — vérifier si un document ou un plan est lisible par quelqu'un sans aucun background, exposant tout le savoir partagé implicite.

**Objectif :** Faire surface le contexte implicite que les experts oublient n'être pas évident pour quiconque est extérieur à la pièce.

**Fonctionnement :** Lit votre contenu comme quelqu'un qui vient d'entrer — aucun contexte, aucun historique partagé, aucun jargon. Signale tout ce qui nécessite un savoir implicite pour être compris, et identifie ce qu'un lecteur naïf mal interpréterait.

**Quand l'utiliser :** Avant de partager avec un nouveau stakeholder, une audience externe, ou quiconque hors de votre équipe immédiate.

---

#### `outside-in` — Forces externes avant les solutions internes

**Origine :** Les Cinq Forces de Porter et l'analyse de l'environnement stratégique. L'insight central : les forces externes à l'organisation (marché, concurrence, réglementation, technologie, comportement client) contraignent ce qui est possible *avant* que les choix internes deviennent pertinents.

**Objectif :** Éviter la pensée de l'intérieur vers l'extérieur — arrêter de partir de "qu'est-ce qu'on veut faire" pour partir de "qu'est-ce que l'environnement impose."

**Fonctionnement :** Cartographie les forces externes qui façonnent l'espace de décision avant de générer toute option interne. L'environnement est traité comme une contrainte, pas comme un décor.

**Quand l'utiliser :** Au début d'une analyse stratégique, à l'entrée sur un nouveau marché, ou quand les plans internes semblent déconnectés de la réalité externe.

---

#### `dixieme-homme` — Thèse adverse complète contre le consensus

**Origine :** La *doctrine du 10e homme*, institutionnalisée par l'AMAN — la Direction du renseignement militaire israélien — après l'échec catastrophique du renseignement lors de la guerre du Kippour (1973). L'échec fut attribué à la *conceptzia* : un modèle mental partagé si dominant que les signaux le contredisant étaient systématiquement ignorés. Le protocole : si 9 analystes sont d'accord, le 10e doit construire le cas le plus solide possible pour la conclusion opposée — pas trouver des failles, mais construire une contre-thèse complète. Popularisé internationalement par le film *World War Z* (2013), où Israël avait institutionnalisé la règle de "croire l'incroyable."

**Objectif :** Briser le groupthink à la racine en rendant la dissidence obligatoire, pas optionnelle.

**Fonctionnement :** Produit une thèse complète et rigoureuse argumentant le contraire du consensus actuel — avec ses propres preuves, sa logique et ses implications. Ce n'est pas l'avocat du diable (pointer les failles) ni le red-team (perspective adverse) : c'est une interprétation alternative complète des mêmes faits.

**Différences clés :**
- vs `contrarian` : contrarian trouve la faiblesse principale de votre plan. `dixieme-homme` argumente une conclusion totalement différente à partir des mêmes faits.
- vs `red-team` : red-team adopte la perspective d'un adversaire externe. `dixieme-homme` argumente contre le consensus de votre propre équipe depuis l'intérieur.
- vs `critique` : critique analyse un artifact pour ses failles. `dixieme-homme` construit un contre-récit face à une croyance partagée.

**Quand l'utiliser :** Fort alignement sur une conclusion avec suspicion de groupthink. Décisions à fort enjeu où un consensus erroné est catastrophique.

---

#### `chairman` — Arbitrer des perspectives contradictoires

**Origine :** Synthèse structurée — conçu comme le meta-skill qui intègre les outputs de plusieurs lentilles Advisory en un verdict unique.

**Objectif :** Passer de perspectives concurrentes à une décision actionnable unique avec des trade-offs explicites.

**Fonctionnement :** Prend les outputs d'autres analyses Advisory (contrarian, expansionist, red-team, etc.) et produit une synthèse : quels arguments tiennent, lesquels s'annulent, quelle est la voie recommandée, quels sont les risques résiduels.

**Quand l'utiliser :** Après avoir lancé deux skills Advisory ou plus sur le même problème et avoir besoin d'une décision unique. Utile aussi quand des stakeholders réels ont des positions genuinement contradictoires.

---

#### `red-team` — Raisonnement depuis la perspective adverse

**Origine :** Méthodologie Red Team CIA et NSA. Une équipe dédiée est chargée de raisonner et d'agir *en tant qu'adversaire* — non pas pour trouver des vulnérabilités, mais pour planifier l'attaque exactement comme l'adversaire la planifierait. Formalisée dans la communauté du renseignement américain dans les années 1970 après que les échecs de la Guerre Froide aient révélé des angles morts persistants causés par le mirror-imaging (supposer que l'adversaire pense comme vous).

**Objectif :** Exposer les angles morts que les défenseurs ne peuvent pas voir parce qu'ils raisonnent du mauvais côté du problème.

**Fonctionnement :** Habite pleinement la position de l'adversaire — ses objectifs, contraintes, ressources et raisonnement. Produit la stratégie que l'adversaire utiliserait réellement, pas celle qu'on craint qu'il utilise.

**Différences clés :**
- vs `contrarian` : contrarian trouve les failles dans votre plan depuis le point de vue d'un critique neutre. `red-team` les trouve depuis la perspective de quelqu'un qui cherche activement à vous battre.
- vs `dixieme-homme` : `dixieme-homme` argumente contre le consensus interne. `red-team` adopte les objectifs et le raisonnement d'un adversaire externe.

**Quand l'utiliser :** Stratégie concurrentielle, analyse de sécurité, préparation à une négociation, tout scénario avec un adversaire actif qui a ses propres objectifs.

---

#### `futurs-alternatifs` — Trois futurs plausibles avec signaux avancés

**Origine :** Planification par scénarios, développée par Herman Kahn à la RAND Corporation dans les années 1950 pour la stratégie nucléaire. Raffinée par la Group Planning de Shell sous Pierre Wack dans les années 1970 — Shell était la seule grande compagnie pétrolière à avoir anticipé le choc pétrolier de 1973 parce qu'elle avait construit des scénarios plutôt que des prévisions. Adoptée ensuite par la CIA pour le renseignement géopolitique et par les stratèges d'entreprise du monde entier.

**Objectif :** Se préparer à l'incertitude réelle plutôt qu'optimiser pour une seule prévision qui pourrait être fausse.

**Fonctionnement :** Produit trois futurs distincts et plausibles — pas meilleur/pire/base (c'est de l'analyse de sensibilité), mais des trajectoires genuinement différentes qui partent d'hypothèses différentes sur l'évolution du monde. Chaque futur est accompagné de signaux avancés : les indicateurs précoces qui diront *lequel* se matérialise, pour ajuster avant que ce soit évident.

**Quand l'utiliser :** Décisions à long horizon où la prédiction est impossible. Stratégie sous incertitude profonde. Planification devant rester robuste face à de multiples futurs possibles.

---

### 🗺️ Stratégie & Intelligence

Outils de renseignement structuré — chacun audite une dimension différente d'un raisonnement ou d'un plan avant de s'engager.

---

#### `ach` — Matrice d'hypothèses concurrentes

**Ce qu'il fait :** Met 3–4 hypothèses concurrentes à l'épreuve des preuves disponibles. Pour chaque information, marque si elle soutient, contredit ou est neutre vis-à-vis de chaque hypothèse. Retient celle que les preuves éliminent le moins — pas celle avec laquelle on a commencé.

**Ce qu'il ne fait pas :** Ne valide pas une conclusion. Ne confirme pas ce qu'on croit déjà.

**Quand l'utiliser :** Vous avez une explication pour quelque chose et voulez vérifier que vous n'en êtes pas amoureux. Se combine naturellement avec `key-assumptions` (hypothèses cachées de chaque thèse) et `indicateurs` (signaux qui diront laquelle se réalise).

---

#### `key-assumptions` — Faire surface les hypothèses cachées

**Ce qu'il fait :** Extrait les prémisses implicites d'un raisonnement, d'une décision ou d'un plan — ce qui est tenu pour acquis sans être dit. Qualifie chaque hypothèse (solide / fragile / inconnue) et identifie les critiques dont l'effondrement ferait tout tomber.

**Ce qu'il ne fait pas :** Ne valide pas le raisonnement. Ne vérifie pas les faits. Il rend la fondation visible — c'est à vous d'en tirer les conséquences.

**Quand l'utiliser :** Avant de s'engager sur un plan, avant de présenter une analyse à un décideur, ou quand vous suspectez que ce que vous appelez "faits" sont en réalité des hypothèses non testées.

> Se combine avec `ach` (qui teste les hypothèses contre les preuves) et `quality-check` (qui audite les sources elles-mêmes).

---

#### `indicateurs` — Définir ce qu'on va surveiller

**Ce qu'il fait :** Définit à l'avance les signaux observables qui diront si un plan tient, si une hypothèse se réalise, ou si un pivot s'annonce. Produit des signaux de confirmation (le plan fonctionne) et des signaux d'alerte (quelque chose cloche), plus les signaux faibles à surveiller.

**Ce qu'il ne fait pas :** Ne suit pas les KPIs en temps réel (`tableau-de-bord-kpi` fait ça). N'évalue pas la performance actuelle. Il définit le dispositif de surveillance avant le lancement.

**Quand l'utiliser :** Après qu'une décision ou un plan est formé, avant le début de l'exécution. Particulièrement puissant après `futurs-alternatifs` (indicateurs avancés par scénario) ou `ach` (signaux qui confirmeraient ou invalideraient l'hypothèse retenue).

---

#### `quality-check` — Auditer la solidité des preuves brutes

**Ce qu'il fait :** Évalue la solidité structurelle des informations sur lesquelles un raisonnement, une décision ou une analyse repose — avant qu'elles deviennent une fondation. Vérifie le type de source, la corroboration, la fraîcheur, les biais potentiels, et signale les lacunes informationnelles.

**Ce qu'il ne fait pas :** N'évalue pas les conclusions. N'évalue pas le raisonnement lui-même. Uniquement la qualité de la matière première.

**Quand l'utiliser :** Avant de prendre une décision qui repose sur des données externes, des chiffres de marché ou des sources citées. Triage essentiel avant `decision` ou `note-strategique` quand on n'est pas sûr de la solidité des sources.

> `quality-check` audite les sources d'information. `key-assumptions` audite les prémisses cachées d'un raisonnement. Les deux sont de l'hygiène pré-décision, à deux niveaux différents.

---

#### `note-strategique` — Note stratégique, conclusion en premier

**Ce qu'il fait :** Produit une note stratégique structurée et directement partageable — pour un décideur, un board ou un dirigeant. Commence par la conclusion, puis l'argument, les options, la recommandation avec trade-offs explicites. Deux pages maximum sans justification.

**Ce qu'il ne fait pas :** Ne commence pas par le contexte pour enterrer la recommandation à la fin. Si vous n'avez pas encore de position claire, lancez `decision` d'abord.

**Quand l'utiliser :** Vous avez une recommandation à faire et devez la packager pour un décideur. Le livrable est directement partageable.

---

#### `strategie-prix` — Stratégie de prix avec trade-offs

**Ce qu'il fait :** Formule une stratégie de pricing en liant valeur perçue, segmentation client et trade-offs business. Compare les modèles de prix (freemium, value-based, usage-based, tiered…) et produit une recommandation avec hypothèses explicites.

**Ce qu'il ne fait pas :** Ne produit pas une grille tarifaire. Ne recommande pas un prix sans énoncer les hypothèses qui le sous-tendent.

**Quand l'utiliser :** Lancement produit, repositionnement, ou pression concurrentielle sur les prix. Nécessite du contexte sur l'offre, les clients cibles et les benchmarks concurrentiels si disponibles.

---

#### `business-case-draft` — Structure de décision d'investissement

**Ce qu'il fait :** Structure une décision d'investissement avec coûts explicites, bénéfices attendus, scénarios de risque et hypothèses financières. Distingue coûts certains et coûts estimés. Marque clairement ce qui est hypothèse vs fait. Si les données sont trop fragiles, le dit et suggère `note-strategique` comme alternative allégée.

**Ce qu'il ne fait pas :** N'invente pas de chiffres.

**Quand l'utiliser :** Vous avez des chiffres et devez cadrer une décision achat/build/invest. Sans chiffres, utilisez `note-strategique`.

---

#### `tam-sam-som` — Sizing de marché avec méthode

**Ce qu'il fait :** Estime le TAM, SAM et SOM via des méthodes top-down et bottom-up avec hypothèses explicites. Surface la méthode, les chiffres et le degré d'incertitude. Web search obligatoire en mode standard/deep.

**Ce qu'il ne fait pas :** Ne produit pas de chiffres de mémoire sans le signaler. Un TAM/SAM/SOM sans hypothèses n'est pas un sizing, c'est une supposition.

**Quand l'utiliser :** Préparation d'un pitch, validation d'une opportunité de marché, ou construction d'un business case.

---

### 🔍 Recherche & Analyse

Chaque outil construit un socle factuel sur un objet analytique spécifique — paysage concurrentiel, cahier des charges, budget, métriques SaaS, coûts, données financières ou narratif data.

---

#### `analyse-concurrentielle` — Paysage concurrentiel avec logique de différenciation

**Ce qu'il fait :** Structure une analyse concurrentielle autour de la logique de différenciation — pas une liste de concurrents. Identifie les forces en présence, compare les acteurs sur un framework commun, surface les zones de différenciation et les risques de positionnement. Web search obligatoire en mode standard/deep.

**Ce qu'il ne fait pas :** Ne produit pas une liste à puces de concurrents. Ne fait pas de recommandations stratégiques — utilisez `decision` pour ça.

**Quand l'utiliser :** Avant une entrée marché, une décision de positionnement ou une narrative fundraising. Se combine avec `note-strategique` ou `decision` en aval.

---

#### `analyse-cdc` — Analyse d'un cahier des charges

**Ce qu'il fait :** Analyse un CDC reçu depuis la perspective du répondant. Surface les exigences explicites, implicites, les zones grises, les contradictions, et les questions bloquantes à poser avant tout engagement.

**Ce qu'il ne fait pas :** Ne résume pas le CDC — il le critique. Ne produit pas de plan de réponse.

**Quand l'utiliser :** Vous recevez un CDC, un appel d'offres ou un document d'exigences et devez comprendre ce qui est vraiment demandé avant de vous engager. Le livrable alimente une stratégie de réponse ou une réunion de clarification.

---

#### `budget-variance-analysis` — Diagnostic budget vs réel

**Ce qu'il fait :** Analyse les écarts entre budget et réalisé. Identifie les variances significatives, les qualifie par nature (volume, prix, mix, timing, opérationnel), et produit des hypothèses correctives et des points de vigilance.

**Ce qu'il ne fait pas :** N'invente pas de causes ou de chiffres. Ne prend pas de décisions de gestion — produit un diagnostic factuel.

**Quand l'utiliser :** Revue mensuelle ou trimestrielle, analyse P&L, ou quand il faut expliquer la performance à un board ou contrôleur.

---

#### `metriques-saas` — Santé du modèle économique SaaS

**Ce qu'il fait :** Lit les métriques clés SaaS ensemble — CAC, LTV, NRR, churn, payback — et les interprète comme un système, pas en isolation. Surface les implications pour la santé du modèle, la soutenabilité de la croissance et les priorités de pilotage.

**Ce qu'il ne fait pas :** Ne produit pas de benchmarks de mémoire en mode standard/deep. Ne recommande pas d'actions — produit un diagnostic.

**Quand l'utiliser :** Préparation board, fundraising, revue opérationnelle, ou quand les tendances métriques sont contradictoires et qu'on veut comprendre ce qu'elles signifient ensemble.

---

#### `total-cost-analysis` — Coût total sur le cycle de vie (TCO)

**Ce qu'il fait :** Structure une analyse TCO couvrant coûts directs, coûts cachés (implémentation, formation, intégration, migration, sortie) et risques financiers sur un horizon donné. Distingue coûts confirmés, estimés et risques non quantifiés.

**Ce qu'il ne fait pas :** Ne regarde pas le prix affiché seul. N'invente pas de chiffres sans les marquer comme hypothèses.

**Quand l'utiliser :** Avant tout achat ou décision fournisseur significatif où le prix visible ne capture pas l'impact économique réel. Complément essentiel de `offer-comparison` et `vendor-scorecard`.

---

#### `financial-narrative` — Chiffres → histoire exécutive

**Ce qu'il fait :** Transforme des données financières brutes (P&L, KPIs, reporting) en narrative claire et message-first pour un board ou dirigeant. Commence par les messages clés, contextualise les chiffres, relie les variations à des facteurs explicatifs.

**Ce qu'il ne fait pas :** N'invente pas de chiffres ou de tendances. Ne reproduit pas les données brutes. Ne déforme pas les chiffres pour raconter une meilleure histoire.

**Quand l'utiliser :** Présentations board, updates investisseurs, revues trimestrielles — chaque fois que des chiffres doivent être communiqués à une audience qui a besoin du "so what" avant le détail.

> Différent de `data-storytelling` : `financial-narrative` est spécifiquement pour les données financières avec une audience board/dirigeant. `data-storytelling` traite tout type de données pour tout type d'audience.

---

#### `data-storytelling` — Données → narratif avec insight

**Ce qu'il fait :** Transforme n'importe quelles données (métriques, tableaux, résultats d'analyse) en narratif clair avec un insight principal et une recommandation. Réorganise les données autour de l'insight — pas dans leur ordre brut.

**Ce qu'il ne fait pas :** Ne raconte pas une histoire qui ne repose pas sur les données. N'empile pas des chiffres sans angle narratif.

**Quand l'utiliser :** Revues produit, restitutions user research, reporting opérationnel — toute présentation de données où l'audience a besoin de comprendre ce que ça signifie et ce qu'il faut en faire.

---

### 📊 Métriques & Pilotage

Outils pour définir et évaluer des systèmes de mesure — des objectifs aux dashboards en passant par les grilles de sélection fournisseur.

---

#### `okr` — Objectif vague → OKR structuré

**Ce qu'il fait :** Transforme une intention stratégique vague en OKR structuré — un Objectif inspirant associé à 3–4 Key Results mesurables. Refuse les KR non mesurables et propose des formulations quantifiées à la place.

**Ce qu'il ne fait pas :** Ne valide pas des KR sans métrique. Ne confond pas KR avec tâches ou initiatives.

**Quand l'utiliser :** Planning trimestriel, alignement stratégique, ou quand le leadership a une direction mais pas d'objectifs mesurables. Le livrable alimente `tableau-de-bord-kpi` et `indicateurs`.

---

#### `tableau-de-bord-kpi` — Structure d'un dashboard KPI

**Ce qu'il fait :** Définit et structure un dashboard KPI depuis des objectifs business, OKRs ou un contexte métier. Distingue KPIs directement mesurables, KPIs estimables (avec hypothèses), et KPIs problématiques (source fiable manquante). Refuse les métriques de vanité.

**Quand l'utiliser :** Après que les OKRs sont définis, ou quand un dispositif de pilotage doit être mis en place pour une équipe, un produit ou une BU.

---

#### `offer-comparison` — Comparaison pondérée avec recommandation

**Ce qu'il fait :** Compare des offres fournisseurs déjà reçues sur une grille pondérée normalisée et produit une recommandation argumentée. Rend la méthode de scoring et l'incertitude visibles — ne cache pas les trade-offs.

**Ce qu'il ne fait pas :** N'évalue pas des offres qu'on n'a pas encore reçues. Si les propositions sont trop différentes en scope, une normalisation manuelle est nécessaire d'abord.

**Quand l'utiliser :** Après réception de plusieurs devis pour un achat significatif.

> Pipeline : `vendor-scorecard` → `offer-comparison` → `total-cost-analysis` → `decision`.

---

#### `vendor-scorecard` — Grille d'évaluation fournisseur réutilisable

**Ce qu'il fait :** Construit une grille de scoring fournisseur depuis un contexte achat — critères, pondérations, échelle de scoring, zones de commentaires qualitatifs. Produit l'**outil** de scoring, pas la décision.

**Ce qu'il ne fait pas :** Ne score pas les fournisseurs (c'est `offer-comparison`). N'invente pas de pondérations sans les justifier.

**Quand l'utiliser :** Avant le lancement d'une consultation, pour aligner les parties prenantes sur les critères d'évaluation. Réutilisable pour les consultations futures du même type.

---

#### `compliance-checklist` — Checklist de conformité légale

**Ce qu'il fait :** Génère une checklist de conformité couvrant les obligations légales, contractuelles et réglementaires — RGPD, droit du travail, réglementation sectorielle — depuis un contexte projet ou un document.

**Ce qu'il ne fait pas :** Ne remplace pas un conseil juridique ou réglementaire professionnel. Nécessite toujours une validation experte avant utilisation opérationnelle.

**Quand l'utiliser :** Avant tout lancement produit, contractualisation, ou changement opérationnel à implications légales. Une pré-validation structurée pour orienter la conversation avec un juriste, pas la remplacer.

---

### ⚖️ Juridique & Contrats

Outils pré-juridiques — tous nécessitent une validation professionnelle avant utilisation. Ils orientent les revues, font surface les risques et produisent des projets. Aucun ne remplace un juriste.

---

#### `legal-risk-flag` — Scan rapide des signaux d'alerte

**Ce qu'il fait :** Lit rapidement un document juridique ou contractuel et extrait les signaux de risque prioritaires avec des niveaux de sévérité gradués (critique / élevé / moyen). Conçu pour la rapidité — une évaluation flash avant de décider si une revue approfondie est nécessaire.

**Ce qu'il ne fait pas :** Ne réalise pas une analyse complète. Signale, ne conclut pas. Ne remplace jamais un juriste.

**Quand l'utiliser :** Vous recevez un document et devez décider en quelques minutes s'il faut escalader à un juriste, ou sur quelles clauses concentrer la revue.

> Utiliser `legal-risk-flag` en premier (scan rapide), puis `contract-review` pour l'analyse clause par clause complète.

---

#### `contract-review` — Revue clause par clause avec redlines

**Ce qu'il fait :** Analyse un contrat clause par clause, identifie les déviations par rapport aux positions standard, produit des redlines prioritaires avec justification et langage alternatif proposé.

**Ce qu'il ne fait pas :** Ne fournit pas de conseil juridique. Le livrable doit être revu par un professionnel qualifié avant utilisation ou négociation.

**Quand l'utiliser :** Avant de signer un contrat significatif. Plus rapide qu'une revue complète par un juriste pour le premier passage — puis le juriste valide.

---

#### `cgv-checker` — Clauses déséquilibrées dans les CGV/CGU

**Ce qu'il fait :** Identifie les clauses déséquilibrées, inhabituelles ou sensibles dans des conditions générales de vente ou d'utilisation, selon la position de lecture (acheteur, utilisateur, abonné).

**Ce qu'il ne fait pas :** N'évalue pas la validité juridique complète des CGV. Ne remplace pas un conseil juridique.

**Quand l'utiliser :** Avant d'accepter les CGV d'un fournisseur ou d'une plateforme significatifs, ou lors de la rédaction de ses propres CGV.

> Différent de `contract-review` : `cgv-checker` est pour les CGV standard (contrats d'adhésion). `contract-review` est pour les contrats négociables avec clauses sur mesure.

---

#### `conformite-rgpd` — Checklist conformité RGPD

**Ce qu'il fait :** Produit une checklist de conformité RGPD depuis une spécification technique, une description produit ou un document de traitement de données. Distingue traitements observés, traitements inférés, et obligations à confirmer.

**Ce qu'il ne fait pas :** Ne remplace pas un DPO ou un professionnel juridique qualifié. Nécessite une validation experte avant utilisation opérationnelle.

**Quand l'utiliser :** Avant de lancer un produit ou une feature traitant des données personnelles. Un auto-diagnostic structuré en premier passage avant la revue DPO.

---

#### `nda-draft` — Projet de NDA adapté au contexte

**Ce qu'il fait :** Génère un projet d'accord de confidentialité adapté au contexte — type de parties, sujet des échanges, durée. Produit un document prêt pour revue juridique, pas pour signature immédiate.

**Ce qu'il ne fait pas :** Ne fournit pas de conseil juridique. Nécessite toujours une validation par un juriste avant signature.

**Quand l'utiliser :** Vous avez besoin d'un point de départ pour une négociation NDA et ne voulez pas partir d'un template générique.

---

#### `contrat-fournisseur` — Contrat fournisseur côté acheteur

**Ce qu'il fait :** Analyse **ou** rédige un contrat fournisseur ou prestataire depuis la perspective de l'acheteur. Surface les conditions déséquilibrées, les clauses à renégocier (SLA, responsabilité, résiliation, pénalités, exclusivité, renouvellement) et les risques contractuels. Peut aussi produire un premier projet quand aucun contrat n'existe encore.

**Ce qu'il ne fait pas :** Ne remplace pas un conseil juridique. Nécessite une validation professionnelle avant utilisation.

**Quand l'utiliser :** Avant de signer un contrat fournisseur, avant d'entrer en négociation, ou lors de la rédaction des conditions initiales d'une nouvelle relation fournisseur.

---

### 👥 RH & People

Outils pour l'ensemble du cycle de vie des collaborateurs — recrutement, intégration, développement, évaluation, organisation et droit du travail. Le contexte droit du travail français est intégré là où c'est pertinent.

---

#### `fiche-poste` — Fiche de poste structurée

**Ce qu'il fait :** Produit une fiche de poste structurée et publiable depuis un brief RH ou un besoin de recrutement. Distingue requis et souhaitable, identifie les zones floues, et produit un livrable qui alimente le workflow de recrutement en aval.

**Quand l'utiliser :** Au lancement d'un processus de recrutement. Le livrable alimente `interview-loop-planner`.

---

#### `entretien-professionnel` — Entretien professionnel obligatoire

**Ce qu'il fait :** Prépare un entretien professionnel obligatoire (Code du Travail, art. L6315-1) — obligatoire tous les 2 ans pour tout salarié. Produit une trame, des questions et un gabarit de compte-rendu conformes aux exigences légales.

**Ce qu'il ne fait pas :** Pas la même chose qu'un entretien annuel d'évaluation. C'est un entretien de développement professionnel obligatoire légalement, pas une évaluation de performance.

**Quand l'utiliser :** Tous les 2 ans par salarié, ou après certains événements spécifiques (retour de congé maternité, longue maladie…) selon la loi française.

---

#### `interview-guide-recruteur` — Guide d'entretien côté recruteur

**Ce qu'il fait :** Produit un guide d'entretien complet pour recruteur ou manager — questions STAR structurées, annotations recruteur, mises en situation, grille de scoring pondérée 1–4, red flags gradués, et fiche de synthèse Go/No-go.

**Quand l'utiliser :** Pour un round d'entretien spécifique. S'utilise idéalement en aval de `interview-loop-planner` qui définit les rounds et compétences.

---

#### `interview-loop-planner` — Conception du processus de recrutement complet

**Ce qu'il fait :** Conçoit la boucle d'entretien complète pour un recrutement — nombre de rounds, compétences par round, scorecard consolidé et planning. Produit des round_briefs qui alimentent directement `interview-guide-recruteur`.

**Quand l'utiliser :** Avant de démarrer les entretiens pour un recrutement significatif. Garantit que chaque round évalue des dimensions différentes.

> Pipeline : `fiche-poste` → `interview-loop-planner` → `interview-guide-recruteur` (un par round).

---

#### `onboarding-plan` — Plan d'intégration 30-60-90 jours

**Ce qu'il fait :** Construit un plan d'intégration structuré couvrant les 30, 60 et 90 premiers jours — objectifs, relations clés, livrables et critères de succès par phase.

**Quand l'utiliser :** Avant l'arrivée d'un nouveau collaborateur, pour donner au manager et au collaborateur une feuille de route commune.

---

#### `offboarding-structure` — Plan de départ avec continuité

**Ce qu'il fait :** Structure un plan d'offboarding couvrant la passation de connaissances, la checklist administrative, le guide d'entretien de sortie et la cartographie des risques de continuité.

**Quand l'utiliser :** Dès qu'un collaborateur donne sa démission. Plus tôt on commence, meilleur est le transfert de connaissances.

---

#### `people-review` — Revue talent collective

**Ce qu'il fait :** Structure une revue de talents collective avec matrice de positionnement (performance × potentiel), plan de succession, évaluation des risques de rétention et départ, et actions prioritaires par profil.

**Quand l'utiliser :** Revues talents annuelles ou bi-annuelles, avant un changement organisationnel, ou lors de la préparation d'un workforce plan.

---

#### `performance-review-helper` — Préparation de l'entretien annuel

**Ce qu'il fait :** Prépare un entretien annuel avec bilan structuré de l'année écoulée et objectifs SMART pour la suivante. Supporte la préparation du manager et l'auto-évaluation du collaborateur.

**Ce qu'il ne fait pas :** Pas l'entretien professionnel obligatoire (`entretien-professionnel`). Celui-ci est sur la performance — résultats, objectifs, contexte de rémunération.

**Quand l'utiliser :** En amont des campagnes d'entretiens annuels.

---

#### `plan-developpement-competences` — Plan de développement des compétences

**Ce qu'il fait :** Construit un plan de développement individuel ou collectif avec actions de formation, calendrier, indicateurs de succès et budget. Relie les lacunes identifiées à des parcours de développement concrets.

**Quand l'utiliser :** Après un entretien annuel, une people review, ou un diagnostic de compétences.

---

#### `grille-remuneration` — Grille de rémunération

**Ce qu'il fait :** Structure une grille de rémunération par famille de métier et niveau de séniorité — fourchettes salariales, critères de positionnement (équité interne, benchmarks marché) et règles de gouvernance (qui peut proposer quoi).

**Quand l'utiliser :** Lors de la montée en échelle d'une équipe, pour avoir des décisions de rémunération cohérentes et défendables sur les recrutements et collaborateurs existants.

---

#### `contrat-emploi` — Contrat de travail

**Ce qu'il fait :** Analyse ou rédige un contrat de travail, une offre d'embauche ou un avenant RH. Surface les clauses clés et les points d'attention. Produit un langage contractuel conforme.

**Ce qu'il ne fait pas :** Ne fournit pas de conseil juridique. Nécessite une validation par un avocat en droit du travail avant utilisation.

**Quand l'utiliser :** Rédaction d'un nouveau contrat, revue d'un contrat reçu, ou préparation d'un avenant (changement de poste, temps partiel…).

---

#### `lettre-cadrage-disciplinaire` — Lettre de cadrage disciplinaire

**Ce qu'il fait :** Rédige un projet de courrier de cadrage disciplinaire factuel et proportionnel — documentant les faits observés, leur impact et le changement de comportement attendu. Calibré à la gravité de la situation.

**Ce qu'il ne fait pas :** Ne produit pas une lettre de sanction formelle. Doit être validé par un avocat en droit du travail avant envoi.

**Quand l'utiliser :** Quand un entretien documenté est nécessaire avant une procédure disciplinaire formelle, ou pour créer une trace écrite d'un problème comportemental.

---

#### `org-design-brief` — Brief de réorganisation

**Ce qu'il fait :** Formalise une cible organisationnelle avec diagnostic de l'état actuel, rationale du design, risques humains et séquencement — avant toute annonce ou mise en œuvre. Surface ce que la nouvelle structure résout, les nouveaux risques qu'elle crée, et comment phaser la transition.

**Quand l'utiliser :** Avant d'annoncer une réorganisation. Utile aussi comme pré-travail avant d'impliquer l'équipe de direction dans le design.

---

### 💻 Produit & Tech

Outils pour l'ensemble du cycle de développement produit — du cadrage d'un besoin à la spécification, conception, construction et maintenance.

---

#### `brief` — Besoin vague → brief structuré

**Ce qu'il fait :** Transforme un besoin, une demande ou une idée vague en brief structuré et actionnable — objectif, contraintes, critères de succès et exclusions. Le livrable est utilisable comme input pour tout skill de production en aval.

**Ce qu'il ne fait pas :** Ne clarifie pas un brief incomplet quand on ne sait pas encore ce qu'on veut (utilisez `cadrage` pour ça). Ne produit pas de spec.

**Quand l'utiliser :** Vous savez ce que vous voulez construire mais devez le structurer avant de le transmettre.

---

#### `cadrage` — Clarifier avant de produire

**Ce qu'il fait :** Explore et clarifie un besoin vague ou incomplet — surface l'intention, les contraintes, les hypothèses et les points de décision avant tout lancement de production. Produit un rapport de clarification et des prochaines étapes recommandées.

**Ce qu'il ne fait pas :** Ne produit pas de brief ou de spec directement. C'est l'étape qui rend `brief` possible quand l'input est trop flou.

**Quand l'utiliser :** La demande est trop ambiguë pour être briefée directement. Quand il faut s'aligner sur ce qui est vraiment demandé avant de s'engager.

> `cadrage` pose les bonnes questions. `brief` écrit la réponse structurée. À enchaîner quand le besoin est flou.

---

#### `analysis` — Décomposer avant de spécifier

**Ce qu'il fait :** Décompose un besoin complexe en lots indépendants et priorisés avant la spec ou la livraison. Produit une décomposition structurée qui alimente un PRD, un sprint ou un plan projet.

**Quand l'utiliser :** Le sujet est dense ou multi-dimensionnel et doit être découpé avant que quiconque puisse le spécifier ou l'estimer. En amont de `prd` ou `feature-spec` pour les initiatives complexes.

---

#### `prd` — Product Requirements Document complet

**Ce qu'il fait :** Produit un PRD complet — contexte, formulation du problème, objectifs, exigences fonctionnelles et non-fonctionnelles, périmètre exclu, métriques de succès et questions ouvertes.

**Quand l'utiliser :** Vous avez besoin d'un document produit complet pour aligner l'équipe, communiquer avec l'ingénierie ou cadrer un investissement significatif.

---

#### `feature-spec` — Spécification fonctionnelle au niveau feature

**Ce qu'il fait :** Produit une spec fonctionnelle complète pour une feature — user stories, exigences MoSCoW, critères d'acceptation, cas limites et métriques de succès.

**Quand l'utiliser :** Une feature est validée et doit être spécifiée pour l'ingénierie. Plus granulaire qu'un PRD — opère au niveau d'une feature ou d'un epic.

---

#### `product-spec` — Spec actionnable allégée

**Ce qu'il fait :** Produit une spec actionnable depuis un brief ou un besoin cadré. Plus légère qu'un PRD, plus structurée qu'un brief — une spec rapide sur laquelle les équipes peuvent agir.

**Quand l'utiliser :** Vous avez besoin de quelque chose entre un brief et un PRD complet. Bien adapté aux petites features, MVPs ou contextes d'itération rapide.

> Hiérarchie : `brief` → `product-spec` → `feature-spec` → `prd` (de plus en plus détaillé).

---

#### `persona` — Personas utilisateurs structurés

**Ce qu'il fait :** Produit des personas utilisateurs structurés depuis des données de recherche ou un brief produit — objectifs, frustrations, comportements, contexte et déclencheurs de décision. Conçu pour être actionnable, pas décoratif.

**Quand l'utiliser :** Au début d'une initiative produit, ou quand l'équipe a des hypothèses divergentes sur pour qui elle construit.

---

#### `journey-map` — Parcours utilisateur avec frictions et opportunités

**Ce qu'il fait :** Produit une carte de parcours utilisateur couvrant étapes, actions, émotions, points de friction et opportunités d'amélioration. Structurée depuis la perspective de l'utilisateur, pas des features du produit.

**Quand l'utiliser :** Avant de redesigner une expérience, d'identifier où investir en UX, ou d'aligner une équipe transverse sur la façon dont les utilisateurs vivent réellement le produit.

---

#### `mockup` — Mockup HTML autonome

**Ce qu'il fait :** Produit un mockup HTML autonome et présentable depuis un brief, une spec ou des références visuelles. Un livrable visuel pour l'alignement et le feedback.

**Ce qu'il ne fait pas :** Pas un prototype fonctionnel. Pas du code prêt pour la production.

**Quand l'utiliser :** Vous avez besoin de quelque chose de visuel pour présenter à des stakeholders, valider avec des utilisateurs ou communiquer un layout avant d'investir en design ou ingénierie.

---

#### `reformulation-us` — Réécriture de user stories mal rédigées

**Ce qu'il fait :** Réécrit des user stories existantes vagues, centrées développeur ou non testables en user stories propres et testables avec structure correcte et critères d'acceptation explicites.

**Quand l'utiliser :** En backlog refinement, quand des stories sont tirées dans un sprint sans être prêtes, ou après une phase de découverte où les stories ont été rédigées informellement.

---

#### `ticket-triage` — Catégorisation et routing de tickets support

**Ce qu'il fait :** Catégorise un ticket support entrant, lui attribue une priorité P1–P4 basée sur l'impact et l'urgence, identifie les informations manquantes pour la prise en charge, et route vers l'équipe ou la file appropriée.

**Quand l'utiliser :** Traitement de tickets support ou bugs entrants, particulièrement dans les contextes à fort volume où une priorisation cohérente est nécessaire.

---

#### `code-review` — Revue de code sur 4 dimensions

**Ce qu'il fait :** Revue du code sur sécurité, performance, correction et maintenabilité. Pour chaque finding : identifie le problème, explique l'impact, propose un correctif. Filtre par confiance — ne remonte que les problèmes haute priorité.

**Quand l'utiliser :** Avant de merger une PR, lors d'un audit codebase, ou lors d'une prise en main d'un nouveau codebase.

---

#### `system-design` — Conception d'architecture technique

**Ce qu'il fait :** Conçoit un système ou une architecture technique — composants, flux de données, contrats API, stockage, décisions de scalabilité et trade-offs explicites. Documente ce qui a été décidé et pourquoi, y compris les options rejetées.

**Quand l'utiliser :** Avant de construire un nouveau système, lors d'une refonte d'architecture existante, ou quand une équipe a besoin d'un blueprint technique partagé.

---

#### `tech-debt` — Audit de dette technique avec plan de remédiation

**Ce qu'il fait :** Identifie, catégorise (structurelle / qualité de code / dépendances / documentation / couverture de tests) et priorise la dette technique avec un plan de remédiation réaliste. Distingue les quick wins du travail structurel.

**Quand l'utiliser :** Avant un sprint significatif, en planning ingénierie trimestriel, quand la vélocité a dégradé, ou avant une due diligence d'acquisition.

> `code-review` évalue un changeset spécifique (une PR, un fichier). `tech-debt` audite les problèmes structurels accumulés sur l'ensemble du codebase.

---

### 🚀 Business & Sales

Outils pour l'exécution commerciale — rédaction d'offres, négociation, appels d'offres, communications stakeholders, comptes-rendus et rétrospectives.

---

#### `offre-commerciale` — Contenu d'une offre client

**Ce qu'il fait :** Produit le contenu structuré d'une offre client — compréhension du contexte, solution proposée, argument de valeur, logique de prix et prochaines étapes. Focus sur le contenu et l'argument, pas la mise en forme finale.

**Ce qu'il ne fait pas :** Ne formate pas le document final (utilisez `deliver` pour ça). Ne négocie pas.

**Quand l'utiliser :** En réponse à une demande entrante, après un call de découverte, ou quand une proposition doit être structurée avant d'être mise en deck ou document.

---

#### `negotiation-brief` — Position structurée avant une négociation

**Ce qu'il fait :** Prépare une position de négociation complète — objectifs, non-négociables, points tradables, BATNA (meilleure alternative en cas d'absence d'accord) et logique de concession. Conçu pour la préparation, pas pour être remis à l'autre partie.

**Ce qu'il ne fait pas :** Pas un script de négociation. Pas un template pour l'autre partie.

**Quand l'utiliser :** Avant toute négociation à fort enjeu — fournisseur, partenariat, client, emploi. Plus la position est claire en entrant, meilleur est le résultat.

---

#### `rfp-draft` — Appel d'offres

**Ce qu'il fait :** Génère un appel d'offres structuré — contexte, périmètre, exigences, critères d'évaluation, livrables attendus et calendrier.

**Quand l'utiliser :** Vous êtes l'acheteur et devez solliciter des offres structurées auprès de plusieurs fournisseurs. Le livrable alimente `offer-comparison` et `vendor-scorecard`.

---

#### `stakeholder-comms` — Communications adaptées à l'audience

**Ce qu'il fait :** Rédige des communications adaptées à un stakeholder spécifique — synthèse exécutive pour un board, briefing technique pour une équipe ingénierie, mise à jour de statut pour un client, annonce partenaire. Adapte le registre, la profondeur et le format à l'audience.

**Quand l'utiliser :** Vous avez quelque chose à communiquer et le message doit atterrir différemment selon les audiences. Particulièrement utile pour les mauvaises nouvelles, les annonces de changement ou les mises à jour complexes.

---

#### `compte-rendu` — Notes brutes → compte-rendu structuré

**Ce qu'il fait :** Transforme des notes brutes de réunion en compte-rendu structuré — décisions prises, actions assignées (owner + date), questions ouvertes et prochaines étapes. Distingue ce qui a été décidé de ce qui a été discuté.

**Quand l'utiliser :** Après toute réunion ayant produit des décisions ou des actions. Le livrable est directement partageable et maintient la responsabilisation claire.

---

#### `retrospective` — Rétrospective blameless

**Ce qu'il fait :** Produit une rétrospective blameless structurée — séparant faits observés et interprétations, identifiant les causes racines sans attribution de blame, et produisant des actions concrètes et assignées.

**Ce qu'il ne fait pas :** Pas une séance de doléances. Pas une évaluation des individus. Blameless signifie le système, pas les personnes.

**Quand l'utiliser :** À la fin d'un sprint, d'un projet, d'un incident ou d'une initiative significative. La contrainte blameless est ce qui rend le livrable actionnable plutôt que défensif.

---

## Pipelines typiques

```
critique → correction → deliver
explorer → decision   → deliver
research → analyse-concurrentielle → decision
brief    → prd → feature-spec
          simplify  (standalone)
          rephrase  (standalone)
```

---

## Installation

### Claude Code

Claude Code scanne `~/.claude/skills/` au démarrage — un sous-répertoire par skill, contenant chacun un `SKILL.md`.

```bash
git clone https://github.com/amiel-35/ix-skills /tmp/ix-skills
for f in /tmp/ix-skills/skills/*.md; do
  id=$(basename "$f" .md)
  mkdir -p ~/.claude/skills/$id
  cp "$f" ~/.claude/skills/$id/SKILL.md
done
```

Ou pour installer un seul skill :

```bash
mkdir -p ~/.claude/skills/critique
cp skills/critique.md ~/.claude/skills/critique/SKILL.md
```

### Claude.ai

**Option A — upload direct (un skill à la fois)**

Dans **Settings → Skills**, glisser-déposer `skills/<id>.md` directement.

**Option B — bundle `.skill` (par lot)**

```bash
git clone https://github.com/amiel-35/ix-skills
cd ix-skills
pip install -r requirements.txt
python3 build.py --target claude-ai
```

Glisser les fichiers `dist/*.skill` dans **Settings → Skills**.

### mystaffy

```bash
python3 build.py --target mystaffy
# ou pour re-générer le format ix-memory natif :
python3 build.py --target ix-memory
```

### GPT / Gemini / autre LLM

Copier-coller le contenu de `skills/<id>.md` comme system prompt. Le frontmatter YAML est ignoré sans effet de bord.

---

## Structure

```
ix-skills/
├── skills/                 ← source canonique (un .md + .mystaffy.json par skill)
├── scripts/
│   └── migrate_from_ix_memory.py
├── dist/                   ← .skill pour claude.ai (gitignore)
├── mystaffy-dist/          ← artefacts mystaffy (gitignore)
├── .claude-plugin/
│   └── plugin.json
├── build.py                ← packager multi-cibles
├── requirements.txt
└── CLAUDE.md               ← guide de contribution
```

---

## Packager

```bash
python3 build.py --validate
python3 build.py
python3 build.py critique
python3 build.py --target claude-ai
python3 build.py --target mystaffy --domain cognitif
python3 build.py --target ix-memory
```

---

## Contribuer

Fork, modifie, PR. Lire `CLAUDE.md` pour les conventions.

---

## Licence

MIT
