# Detection of design pattern

---

# Recherche

## Requête Scopus

```
       ( ( TITLE-ABS-KEY ( "design pattern" )  OR  TITLE-ABS-KEY ( "design motif" ) )
  AND  ( TITLE-ABS-KEY ( detect* )  OR  TITLE-ABS-KEY ( identif* )  OR  TITLE-ABS-KEY ( recogni* ) ) )
  AND  PUBYEAR  >  1998  
  AND  ( LIMIT-TO ( SUBJAREA ,  "COMP" )  OR  LIMIT-TO ( SUBJAREA ,  "ENGI" ) )
  AND  ( LIMIT-TO ( DOCTYPE ,  "cp" )  OR  LIMIT-TO ( DOCTYPE ,  "ar" ) ) 
  AND  ( LIMIT-TO ( EXACTKEYWORD ,  "Design Patterns" )  OR  LIMIT-TO ( EXACTKEYWORD ,  "Design patterns" ) ) 
  AND  ( LIMIT-TO ( LANGUAGE ,  "English" ) ) 
  AND  ( EXCLUDE ( SUBJAREA ,  "SOCI" )  OR  EXCLUDE ( SUBJAREA ,  "BIOC" ) ) 
  AND  ( EXCLUDE ( SUBJAREA ,  "MATH" )  OR  EXCLUDE ( SUBJAREA ,  "DECI" ) 
     OR  EXCLUDE ( SUBJAREA ,  "MATE" )  OR  EXCLUDE ( SUBJAREA ,  "PHYS" ) 
     OR  EXCLUDE ( SUBJAREA ,  "BUSI" )  OR  EXCLUDE ( SUBJAREA ,  "EART" ) 
     OR  EXCLUDE ( SUBJAREA ,  "ENVI" )  OR  EXCLUDE ( SUBJAREA ,  "MEDI" ) ) 
  AND  ( EXCLUDE ( SUBJAREA ,  "AGRI" )  OR  EXCLUDE ( SUBJAREA ,  "NEUR" )  OR  EXCLUDE ( SUBJAREA ,  "PSYC" ) ) 
  AND  ( EXCLUDE ( SRCTYPE ,  "k" )  OR  EXCLUDE ( SRCTYPE ,  "d" ) ) 
```

## Résultats

403 Articles

---

# Répartition

* [2;135]   pierre, alex
    - 6 Désaccords
    - 3 3e avis
* [136;269] pierre, badr
    - 22 Désaccords
    - 5 3e avis
* [270;404] alex, badr
    - 4 désaccords
    - 1 3e avis

---

# Critère d'exclusion

1. not a contribution in software engineering (more than a use case of soft. eng.) 

2. not a full reference or research paper

3. not about software design pattern. (including architectural and interaction pattern)
  (https://en.wikipedia.org/wiki/Software_design_pattern)
  (https://en.wikipedia.org/wiki/Design_pattern)

4. the main contribution of the paper is not about detection of design pattern.

## Résultat du screening

1. 100 articles sur la détection de DP 
2. 91 article sur les méthodes de détection de DP

---


# Schéma de classification

Excepté où il est noté «disjoint», il est possible d'assigner un article à plus d'une catégories.

---

# Schéma de classification

##Detection strategy based on
 * AI/ML based
 * Graph based
 * Logic based (inference on rules, ontology)
 * Metric based
 * Automata based
 * Instrumentation based (trace included)
 * Pattern matching
 * Other

---

# Schéma de classification

##Language generality (disjoint)
 * Language dependant
 * Language independant

---

# Schéma de classification

##Analysis type (disjoint)
 * Static
 * Dynamic
 * Hybrid

---

# Schéma de classification

##Validation method
 * Benchmark
 * Use case
 * Experience
 * Survey
 * Other

---

# Schéma de classification

##Detection Level (disjoint)
 * Machine                [détails de bas niveau du programme]
 * Source (code, token)   [Présence d'identifiant + détails de bas niveau du programme]
 * Model (UML, formalism) [Présence d'identifiant]
 * Other

---

# Schéma de classification

##Detected pattern types
 * Creationnal
 * Structural
 * Behaviour
 * Other
-
 * Not specified

---

# Schéma de classification

##Pattern detection generality (disjoint)
 * Specific (method for a specific pattern)
 * Generic (general approach to pattern detection)
