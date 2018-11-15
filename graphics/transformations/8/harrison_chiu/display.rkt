#lang racket

(require "contracts.rkt")

(provide (contract-out
          (pixels->image
           (-> exact-nonnegative-integer? ; rows
               exact-nonnegative-integer? ; cols
               color/c ; bg color
               (listof pixel/c) ; pixels
               image/c))
          (image->string
           (-> image/c
               string?))))

(define pixels->image
  (lambda (rows cols color pixs)
    (define img-pixs (make-vector (+ (* rows cols)) color))
    (map (lambda (pix)
           (define row (floor (first pix)))
           (define col (floor (second pix)))
           (define color (third pix))
           (define index (+ (* row rows)
                            col))
           (when (< index (vector-length img-pixs))
             (vector-set! img-pixs 
                          index
                          color)))
         pixs)
    (list rows cols 255 img-pixs)))

(define image->string
  (lambda (img)
    (string-join
     #:before-first "P3 "
     (append
      (list (number->string (first img))
            (number->string (second img))
            (number->string (third img)))
      (vector->list 
       (vector-map (lambda (color)
                     (string-join (map number->string color)))
                   (fourth img)))))))
