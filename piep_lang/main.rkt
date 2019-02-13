#lang racket

(module reader racket
  (provide (rename-out [my-read read])
           (rename-out [my-read-syntax read-syntax]))

  (define (my-read in)
    (syntax->datum
     (my-read-syntax #f in)))

  (define (my-read-syntax src in)
    (with-syntax ([s (read in)])
      #'(module piep racket
          (require sql)
          (define-syntax-rule (generate-sql-query sexp)
            (sql-statement->string (sql sexp)))
          (provide qry)
          (define qry
            (generate-sql-query s))
          (display qry)))))