
```dataview  

TABLE file.frontmatter.source, file.frontmatter.classe

WHERE type = "Sottoclasse"  

SORT file.frontmatter.source ASC, file.name ASC  

```


```dataview  
TABLE length(rows) AS "n° Dominio"
WHERE type = "Sottoclasse" AND Dominio
FLATTEN Dominio
GROUP BY Dominio
SORT length(rows) DESC, type DESC
```