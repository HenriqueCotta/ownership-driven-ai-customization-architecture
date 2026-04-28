# Resumo Local Como Guarda de Segurança

## Situação

Um repositório depende de uma fonte externa de policy para restrições de cobrança.

A fonte de policy é autoritativa, mas o acesso às vezes falha em ambientes locais.

O time quer que o agente evite mudanças inseguras quando a fonte estiver indisponível.

## Entrada de Fonte

```md
## finance-policy

Where: policy workspace `billing-policy`
Access: policy-docs MCP, if available.
Use for: tax, invoice, refund, and compliance constraints.
Freshness: verify before changing invoice or refund behavior.
If unavailable: do not relax existing finance constraints; mark policy verification blocked.
If it conflicts: owns finance compliance constraints.
```

## Instruction de Owner

```md
---
applyTo: "src/billing/**"
---

# Billing

Invoices must remain tax-inclusive at display boundaries.

Local safety summary: existing invoice displays are tax-inclusive. If supporting source `finance-policy` is unavailable, this summary may preserve current behavior, but it must not justify a new tax rule.

Before changing invoice or refund semantics, use supporting source `finance-policy`.
```

## Por Que Esta Duplicação É Aceitável

A frase duplicada é curta, estável e defensiva.

Ela impede que o agente relaxe um invariante importante quando a fonte não pode ser acessada.

Ela não copia taxas detalhadas, exceções regionais nem texto procedural de policy.

## Versão Ruim

```md
# Billing

The current tax rate is 17.5%. Region A uses exception X. Region B uses exception Y. Discounts use policy rule ABC. Refund timing follows the current finance spreadsheet.
```

Isso transforma a instruction em espelho stale.

Se esses fatos importam, o agente precisa da fonte autoritativa atual.

## Lição do Exemplo

Duplique guardrails duráveis com parcimônia.

Use-os para preservar segurança quando acesso falhar, não para evitar consultar a fonte antes de fazer uma mudança dependente de policy.
