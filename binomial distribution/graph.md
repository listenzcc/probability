# Summary of Graphs

This document contains the summary and placeholders for the graphs referenced in the binomial distribution documents.

## Prompts

1. Draw the plantuml graph for the knowledge of the german tank problem.
2. Place the expectation and variance formula into the plantuml, and add necessary explaining.

## PlantUML Diagram for German Tank Problem

```plantuml
@startuml
title Knowledge of the German Tank Problem

package "German Tank Problem" {
    class "Bayesian Analysis" {
        + p(T=t | m, k)
        + E(T) = (m-1)(k-1)/(k-2)
        + Var(T) = (k-1)(m-1)(m-k+1)/((k-3)(k-2)^2)
    }
    class "Frequency Analysis" {
        + Pr(M=m)
        + E(m) = k(t+1)/(k+1)
    }
    class "Probability Distribution" {
        + p(n | m, k)
        + p(m | t, k)
    }
}

"German Tank Problem" --> "Bayesian Analysis"
"German Tank Problem" --> "Frequency Analysis"
"German Tank Problem" --> "Probability Distribution"

@enduml
```

### Explanation

- **Bayesian Analysis**: This section includes the posterior probability \( p(T=t | m, k) \), the expectation \( E(T) \), and the variance \( Var(T) \).
- **Frequency Analysis**: This section includes the probability \( Pr(M=m) \) and the expectation \( E(m) \).
- **Probability Distribution**: This section includes the probability distributions \( p(n | m, k) \) and \( p(m | t, k) \).

## Graphs

### doc-1.md

![Graph for doc-1](./binomial-distribution-img/doc-1-graph.png)

### doc-2.md

![Graph for doc-2](./binomial-distribution-img/doc-2-graph.png)

### doc-3.md

![Graph for doc-3](./binomial-distribution-img/doc-3-graph.png)

### doc-4.md

![Graph for doc-4](./binomial-distribution-img/doc-4-graph.png)

### doc-5.md

![Graph for doc-5](./binomial-distribution-img/doc-5-graph.png)

### doc-6.md

![Graph for doc-6](./binomial-distribution-img/doc-6-graph.png)
