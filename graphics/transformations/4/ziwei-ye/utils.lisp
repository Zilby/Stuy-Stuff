(in-package #:rizna)

(defun deg->rad (d) (* pi (/ d 180.0)))

(defmacro round-nums (&rest nums)
  `(setf ,@(mapcan (lambda (x) `(,x (round ,x))) nums)))
