# Lecture 1: Agents

- **Date:** September 7, 2023
- **Duration:** 20 minutes

## What is an Agent?

An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.

- Agents and environments interact continuously.

- Rational agents try to maximize a performance measure.

- PEAS description of task environment:

  - Performance measure
  - Environment
  - Actuators
  - Sensors

- Environs:

  - Fully observable vs. partially observable
  - Deterministic vs. stochastic
  - Episodic vs. sequential
  - Static vs. dynamic
  - Discrete vs. continuous
  - Single agent vs. multi-agent

- Agent types:
    
      - Simple reflex agents
      - Model-based reflex agents
      - Goal-based agents
      - Utility-based agents
      - Learning agents

## Simple Reflex Agents

- Select actions based on current percept, ignoring rest of percept history.

- Condition-action rules: `if condition then action`

- Example: printer agent

  - Environment: a network of printers, users, and print jobs

  - Sensors: input from keyboard, mouse, network, printer

  - Actuators: printer

  - Performance measure: number of print jobs completed per hour

  - Condition-action rules:
    
        - `if (job is mine) and (printer is free) then print`
        - `if (job is mine) and (printer is busy) then wait`
        - `if (job is not mine) and (printer is free) then ignore`
        - `if (job is not mine) and (printer is busy) then ignore`