---
type: Indice
---

```dataview
TABLE file.frontmatter.source
WHERE contains(type, [[Ancestry]])
SORT file.frontmatter.source ASC, file.name ASC
```