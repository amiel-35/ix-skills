# TODO — ix-skills

Idées et chantiers à faire après, pas des tâches en cours. Une entrée par
chantier, datée, avec ce qu'on sait déjà.

## Design thinking : enchaînements de méthodes standard (2026-09-20)

**Idée.** Les skills atomiques couvrent déjà les quatre phases du double
diamant. Ce qui manque n'est pas un skill, c'est le câblage : des prompts
d'enchaînement qui décrivent, pour chaque méthode standard, quels skills
s'appellent dans quel ordre, avec quoi en entrée, et surtout ce que chaque
étape passe à la suivante.

**Ce qu'on a appris le 2026-09-20** (passe « désolutionner », cf. CHANGELOG) :

- Une référence ou une solution nommée fonctionne comme une cible pour un
  modèle, même donnée « pour info ». Donc `explorer` ne doit recevoir que
  l'intention et les contraintes justifiées, jamais le brief entier ; les
  hypothèses non justifiées lui sont passées comme « réponse par défaut à
  écarter », pas comme contexte.
- La variance vient du brief, pas du modèle : plusieurs instances
  d'`explorer` à une contrainte positive chacune, jamais une pile
  d'interdictions.
- Chaîne validée sur le CDC N1 FN Safer : `cadrage` → `questioning` →
  passation (intention + contraintes justifiées + défaut à écarter) →
  `explorer` 4 options. Elle retrouve le choix fait à la main en août
  (fil rouge Safer, ateliers) et en pose deux autres à côté.

**Cartographie double diamant → skills existants**

| Phase | Skills |
|---|---|
| Découvrir | `research`, `outside-in`, `persona`, `journey-map` |
| Définir | `cadrage` ou `brief`, `questioning`, `firstprinciples`, `problem-framing` |
| Développer | `explorer` (une ou plusieurs instances), `futurs-alternatifs`, `mockup` |
| Livrer | `decision`, `prioritize`, `product-spec`, `deliver` |

**Méthodes standard à décrire, chacune comme un prompt d'enchaînement**

- Brainstorming et tri : N instances `explorer` en parallèle, une
  contrainte positive chacune → `synthese` pour dédoublonner → `prioritize`
  ou `decision` pour refermer. Décider si le tri passe par `chairman` quand
  plusieurs points de vue ont produit les options.
- Tri de cartes (card sorting, architecture d'information) : pas de skill
  dédié aujourd'hui. Voir si `decomposer` + `prioritize` suffisent, ou si
  un atome « regrouper / nommer des groupes » manque.
- « Comment pourrait-on… » (How might we) : `firstprinciples` pour
  remonter au vrai problème, puis `questioning` pour formuler les HMW.
- Crazy 8 : huit instances `explorer` à `nb_options: 1`, huit contraintes
  différentes, puis `chairman`.
- Vote par points (dot voting) : `prioritize` avec critères explicites,
  ou `decision` si les options sont exclusives.
- Regroupement par affinités (affinity mapping) : `synthese` ou
  `decomposer`, à tester.
- Critique de prototype : `critique`, puis `red-team` si l'enjeu le
  justifie, puis `correction` pour consolider.
- Rétrospective : `retrospective` existe déjà.

**Forme à décider.** Soit un dossier `pipelines/` avec un fichier par
méthode (prompt d'enchaînement lisible par un humain et par un agent),
soit des scripts Workflow réutilisables (`.claude/workflows/`). Le doc
source du mécanisme désolutionner est dans
`~/Projets/Bike-routing/docs/briefer_une_ia_pour_du_design.md`.

**À ne pas oublier.** Chaque prompt d'enchaînement doit dire ce qu'il passe
à l'étape suivante, pas seulement quel skill il appelle. C'est là que ça
casse.
