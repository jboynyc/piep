# piep

## What is this?

This repo contains two elements:

1. A Racket `#lang` called `piep` that allows you to use Racket's [structured notation for SQL statements][racket-sql] as a standalone language to contruct SQL queries.
2. An IPython cell magic function, `%%piep`, that you can use to generate SQL queries from s-expressions within Jupyter notebooks.

## How can I use it?

The cell magic depends on the Racket lang, so you must first install that by running `raco pkg install piep_lang/`. To use the cell magic in a notebook, run `%load_ext piep_magic` in a cell of your notebook.

## What does it do exactly?

This Racket program evaluates to a SQL query.

```racket
#lang piep

(select rowid (datetime created) task contexts tags active notes_count
        #:from
        (left-join
         (select rowid * #:from tasks
                 #:where (and
                          (= active 1)
                          (like contexts "foo")
                          (like tags "bar")
                          (like task "spam")))
         (select (as (count note) notes_count) task_ref
                 #:from notes
                 #:group-by task_ref)
         #:on (= rowid task_ref)))
```

Instead of running this in DrRacket, you can also run it in a Jupyter notebook:

```
%%piep

(select rowid (datetime created) task contexts tags active notes_count
        #:from
        (left-join
         (select rowid * #:from tasks
                 #:where (and
                          (= active 1)
                          (like contexts "foo")
                          (like tags "bar")
                          (like task "spam")))
         (select (as (count note) notes_count) task_ref
                 #:from notes
                 #:group-by task_ref)
         #:on (= rowid task_ref)))
```

This also evaluates to a SQL query, which you can then use in your notebook, for example to construct a dataframe. 

```python
import pandas as pd
pd.read_sql(_, db_conn)
```

Congratulations, you've built a dataframe from s-expressions using tenuously assembled pieces of code!

## Disclaimer

This is a quick hack. Use at your own risk.

[racket-sql]: https://docs.racket-lang.org/sql/index.html "SQL: A Structured Notation for SQL Statements"
