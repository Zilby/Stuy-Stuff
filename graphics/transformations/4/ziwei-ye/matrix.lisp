(in-package #:rizna)

(defvar *print-matrix* t)

(defun print-matrix (matrix &key (stream t))
  (format stream "~:{~0t~a~6t~a~11t~a~16t~a~%~}" matrix))

(defmacro add-point (matrix x y &optional (z 0))
  (let ((pt (gensym)))
    `(let ((,pt (list (list ,x ,y ,z 1))))
       (when ,*print-matrix* (format t "~%Adding point~%~a~&to edge matrix.~%" (print-matrix ,pt :stream nil)))
       (if ,matrix
	   (nconc ,matrix ,pt)
	   (setf ,matrix ,pt)))))

(defmacro add-edge (matrix x0 y0 z0 x1 y1 z1)
     `(progn
	(add-point ,matrix ,x0 ,y0 ,z0)
	(add-point ,matrix ,x1 ,y1 ,z1)))

(defun draw-lines (matrix image &optional (color-vals #(0 0 0)))
  (loop for ((x0 y0) (x1 y1)) on matrix by #'cddr
     do (round-nums x0 y0 x1 y1)
       (bresenham-line x0 y0 x1 y1 image color-vals)))

(defmacro with-empty-matrices ((&rest vars) &body body)
  `(let ((,@vars))
     (progn
       ,@body
       (values ,@vars))))

(defmacro with-empty-matrices-new-image ((&rest vars) (i-var &key (type "P3") (x 300) (y 300) name) &body body)
  `(let ((,@vars) (,i-var (new-image ,type ,x ,y ,name)))
     (progn
       ,@body
       (values ,@vars ,i-var))))

(defun scalar-mul (matrix val)
  (mapcar #'(lambda (row) (mapcar #'(lambda (x) (* x val)) row)) matrix))

(defun matrix-mul (m1 m2)
  (assert (= (length (car m1)) (length m2)) () "Cannot multiply.")
  (mapcar #'(lambda (row) (apply #'mapcar #'(lambda (&rest col)
					      (apply #'+ (mapcar #'* row col))) m2)) m1))

(defun m* (a b)
  (when (numberp a) (psetf a b))
  (etypecase b
    (number (scalar-mul a b))
    (list (matrix-mul a b))))

(defun matrix-apply (edge transform)
  (mapcar #'(lambda (x) (reduce #'append x)) 
	  (mapcar #'(lambda (x) (matrix-mul (if (> (length transform) 1) 
						    (reduce #'m* transform)
						    (car transform))
					    (mapcar #'list x))) edge)))

(defmacro matrix-apply-f (edge transform img)
  `(progn
     (format t "~%Applying transfrom matrix to edge matrix.~%") 
     (setf ,edge (matrix-apply ,edge ,transform))
     (draw-lines ,edge ,img)))
