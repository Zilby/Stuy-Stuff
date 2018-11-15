(in-package #:rizna)

(defun print-matrix (matrix &key (stream t))
  (format stream "~:{~0t~a~6t~a~11t~a~16t~a~%~}" matrix))

(defun add-coord (x y z)
  (let ((pt (list (list x y z 1))))
    (when *print-matrix* (format t "~%Adding point~%~a~&to edge matrix.~%" (print-matrix pt :stream nil)))
    (if *edge-env*
	(nconc *edge-env* pt)
	(setf *edge-env* pt))))

(define-rizna-op add-edge "l" :function (x0 y0 z0 x1 y1 z1)
  (add-coord x0 y0 z0)
  (add-coord x1 y1 z1))

(defun add-point (x y z)
  (add-edge x y z x y z))

(define-rizna-op add-box "p" :function (x1 y1 z1 width height depth) "a better way exists but too lazy"
  (add-point x1 y1 z1)
  (add-point (+ x1 width) y1 z1)
  (add-point x1 (+ y1 height) z1)
  (add-point x1 y1 (+ z1 depth))
  (add-point (+ x1 width) (+ y1 height) z1)
  (add-point x1 (+ y1 height) (+ z1 depth))
  (add-point (+ x1 width) y1 (+ z1 depth))
  (add-point (+ x1 width) (+ y1 height) (+ z1 depth)))

(defun draw-lines (matrix image &optional (color-vals #(0 0 0)))
  (loop for ((x0 y0) (x1 y1)) on matrix by #'cddr
     do (round-nums x0 y0 x1 y1)
       (bresenham-line x0 y0 x1 y1 image color-vals)))

;; (defmacro with-empty-matrices ((&rest vars) &body body)
;;   `(let ((,@vars))
;;      (progn
;;        ,@body
;;        (values ,@vars))))

;; (defmacro with-empty-matrices-new-image ((&rest vars) (i-var &key (type "P3") (x 300) (y 300) name) &body body)
;;   `(let ((,@vars) (,i-var (new-image ,type ,x ,y ,name)))
;;      (progn
;;        ,@body
;;        (values ,@vars ,i-var))))

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
  (unless transform (return-from matrix-apply nil))
  (mapcar #'(lambda (x) (reduce #'append x)) 
	  (mapcar #'(lambda (x) (matrix-mul (if (> (length transform) 1) 
						    (reduce #'m* transform)
						    (car transform))
					    (mapcar #'list x))) edge)))

(define-rizna-op matrix-apply-f "a" :function ()
     (format t "~%Applying transfrom matrix to edge matrix.~%") 
     (setf *edge-env* (matrix-apply *edge-env* *transform-env*))
     (draw-lines *edge-env* *image-env*))

(define-rizna-op draw-f "draw" :function ()
     (draw-lines *edge-env* *image-env*))

(define-rizna-op clear-f "w" :function ()
     (when *print-matrix* (format t "~%Reseting edge matrix.~%"))
     (setf *edge-env* nil))
