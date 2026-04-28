# Exemplos de Fontes de Apoio

Estes exemplos mostram como repositórios podem usar fontes de apoio sem transformá-las em outra camada do ODA.

Eles são exemplos de formato e julgamento, não templates obrigatórios.

Leia como variações:

- [Uma Fonte Local](./01-uma-fonte-local.md)
  - o menor padrão útil de fonte local e dúvidas comuns de implementação
- [Instruction de Fontes de Apoio do Owner Raiz](./02-instruction-de-fontes-de-apoio-do-owner-raiz.md)
  - uma instruction de fontes do owner raiz com estilos mistos de entrada
- [Instructions Consumidoras](./03-instructions-consumidoras.md)
  - owners e overlays que referenciam IDs de fonte sem repetir detalhes de acesso
- [Múltiplas Fontes e Conflitos](./04-multiplas-fontes-e-conflitos.md)
  - várias fontes, ownership de claims, tratamento de conflito e uma skill de reconciliação
- [Resumo Local Como Guarda de Segurança](./05-resumo-local-como-guarda-de-seguranca.md)
  - quando um pequeno resumo duplicado é mais seguro do que depender só de acesso
- [Instruction de Interpretação Específica da Fonte](./06-instruction-de-interpretacao-especifica-da-fonte.md)
  - quando uma fonte precisa de policy durável de interpretação, mas não de operações exatas

## Dica de Leitura

Use a forma mais leve que deixe claro como a fonte deve ser usada.

Se uma fonte é óbvia e local, o exemplo pode ser pequeno.

Se uma fonte é externa, privada, viva ou propensa a conflito com outras evidências, dê ao agente guidance suficiente de localização, acesso, fallback e conflito para evitar adivinhação.

Se uma fonte precisar de policy detalhada de interpretação, prefira uma instruction específica por fonte apenas quando guidance de fonte mais leve não bastar.

Tenha cuidado com instructions repo-wide específicas por fonte porque elas normalmente exigem `applyTo: "**"` e podem virar contexto always-on.

## Dica de Nome

Instructions consumidoras normalmente devem referenciar um ID estável de fonte:

```md
Use supporting source `product-docs`.
```

Isso é mais claro do que depender de um título humano como `Sources > Product Documentation`, e não força um nome exato de arquivo ou uma estrutura rígida de headings.
