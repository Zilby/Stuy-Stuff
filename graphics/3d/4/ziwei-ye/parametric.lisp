(in-package #:rizna)

(defparameter *hermite* '((2 -2 1 1)
			 (-3 3 -2 -1)
			 (0 0 1 0)
			 (1 0 0 0)))

(defparameter *brezier* '((-1 3 -3 1)
			 (3 -6 3 0)
			 (-3 3 0 0)
			 (1 0 0 0)))

(defmacro parametric (type &body body) "totally sane code that generates either a 2d or 3d parametric lambda function"
	  (assert (member type '(:2d :3d)) () "Type has to be either :2d or :3d.")
	  (macrolet ((when-3d (&body body) `(when (eql type :3d) ,@body))
		     (maybe-eval-range (var) ``(when (consp ,',var) (setf ,',var (eval ,',var))))
		     (common-procedure () ``(let ,let-param
					      ,@body)))
	    (let* ((x0 (gensym)) (y0 (gensym)) (z0 (gensym))
		   (lambda-list (remove nil `(step 
					      ,(when-3d 'step2)
					      &key (range '(0 (* pi 2))) ,(when-3d '(range2 '(0 (* pi 2)))))))
		   (let-param (remove nil `((param (+ (* param (- (cadr range) (car range))) (car range)))
					    ,(when-3d '(param2 (+ (* param2 (- (cadr range2) (car range2))) (car range2))))))))
	      `(lambda ,lambda-list
		 ,(maybe-eval-range (car range))
		 ,(maybe-eval-range (cadr range))
		 ,(when-3d `(progn 
			      ,(maybe-eval-range (car range2))
			      ,(maybe-eval-range (cadr range2))))
		 (let ((x 0) (y 0) (z 0) ,x0 ,y0 ,z0)
		   (declare (ignorable ,x0 ,y0 ,z0))
		   (iter:iter (iter:for param iter:initially 0.0 then (+ param step))
			      (iter:until (>= param 1.01))
			      ,(if (eql type :3d) `(iter:iter (iter:for param2 iter:initially 0.0 then (+ param2 step2))
							      (iter:until (>= param2 1.01))
							      ,(common-procedure)
							      (add-point x y z))
				   `(progn
				      ,(common-procedure)
				      (when ,x0 (add-edge ,x0 ,y0 ,z0 x y z))
				      (setf ,x0 x ,y0 y ,z0 z)))))))))

(defun simple-parametric (&key (x-func (constantly 0)) (y-func (constantly 0)) (z-func (constantly 0)))
  (parametric :2d (setf x (funcall x-func param)
		      y (funcall y-func param)
		      z (funcall z-func param))))

(defun simple-parametric-surface (&key (x-func (constantly 0)) (y-func (constantly 0)) (z-func (constantly 0)))
  (parametric :3d (setf x (funcall x-func param param2)
		      y (funcall y-func param param2)
		      z (funcall z-func param param2))))

;; (defun draw-parametric ((step matrix) func)
;;   (when (and (not (symbolp func)) (not (functionp func))) (setf func (eval func)))
;;   (funcall func step matrix))

(define-rizna-op draw-circle "c" :function (cx cy r)
		 (funcall (simple-parametric :x-func (lambda (p) (+ cx (* (cos p) r)))
					     :y-func (lambda (p) (+ cy (* (sin p) r))))
			  1/20))

(defun brezier-points (param p1 p2 p3 p4)
  (let* ((params `((,(expt param 3) ,(expt param 2) ,param 1)))
	 (points  (list p1 p2 p3 p4))
	 (p (car (reduce #'m* (list params *brezier* points)))))
    (values (first p) (second p) (third p))))

(define-rizna-op draw-brezier "b" :function (bx0 by0 bz0 bx1 by1 bz1 bx2 by2 bz2 bx3 by3 bz3)
		 (funcall (parametric :2d (multiple-value-bind (a b c) 
					    (brezier-points param 
							    (list bx0 by0 bz0)
							    (list bx1 by1 bz1)
							    (list bx2 by2 bz2)
							    (list bx3 by3 bz3))
					  (setf x a y b z c)))
			  1/20 :range '(0 1)))

(defun hermite-points (param p1 p2 p3 p4)
  (let* ((params `((,(expt param 3) ,(expt param 2) ,param 1)))
	 (points  (list p1 p3 (mapcar #'- p2 p1) (mapcar #'- p4 p3)))
	 (p (car (reduce #'m* (list params *hermite* points)))))
    (values (first p) (second p) (third p))))

(define-rizna-op draw-hermite "h" :function (hx0 hy0 hz0 hx1 hy1 hz1 hx2 hy2 hz2 hx3 hy3 hz3)
  (funcall (parametric :2d (multiple-value-bind (a b c) 
			       (hermite-points param 
					       (list hx0 hy0 hz0)
					       (list hx1 hy1 hz1)
					       (list hx2 hy2 hz2)
					       (list hx3 hy3 hz3))
			     (setf x a y b z c)))
	   0.01 :range '(0 1)))

(define-rizna-op draw-coil "coil" :function (range dx dy h)
  (funcall (simple-parametric :x-func (lambda (u) (+ (* 60 (cos u)) dx))
			      :y-func (lambda (u) (+ (* 60 (sin u)) dy))
			      :z-func (lambda (u) (* h u)))
	   0.01 :range `(0 ,range)))

(define-rizna-op draw-torus "d" :function (x y r1 r2)
  (funcall (simple-parametric-surface :x-func (lambda (u v) (+ x (* (cos u) (+ (* r1 (cos v)) r2))))
				      :y-func (lambda (u v) (+ y (* (sin u) (+ (* r1 (cos v)) r2))))
				      :z-func (lambda (u v) (* r1 (sin v))))
	   0.02 0.02))

(define-rizna-op draw-sphere "m" :function (x y r)
  (funcall (simple-parametric-surface :x-func (lambda (u v) (+ x (* r (cos v) (cos u))))
				      :y-func (lambda (u v) (+ y (* r (cos v) (sin u))))
				      :z-func (lambda (u v) (* r (sin v))))
	   0.02 0.02 :range2 '((- (/ pi 2)) (/ pi 2))))

(define-rizna-op draw-astroidal "astroidal" :function (a b c x y)
  (funcall (simple-parametric-surface :x-func (lambda (u v) (+ x (* 10 (expt (* a (cos u) (cos v)) 3))))
				      :y-func (lambda (u v) (+ y (* 10 (expt (* b (cos u) (cos v)) 3))))
				      :z-func (lambda (u v) (declare (ignore u)) (* 10 (expt (* c (sin v)) 3))))
	   0.02 0.02 :range '((- pi) (* 1 pi)) :range2 '((- pi) (* 1 pi))))

(define-rizna-op draw-puesdosphere "puesdosphere" :function (x y)
  (funcall (simple-parametric-surface :x-func (lambda (u v) (+ x (* 60 (* (cos u) (sin v)))))
				      :y-func (lambda (u v) (+ y (* 60 (* (sin u) (sin v)))))
				      :z-func (lambda (u v) (declare (ignore u)) 
						      (handler-case (* 60 (+ (cos v) (log (tan (* 0.5 v)))))
							(division-by-zero () 0)))) ;2lazy2fix
	   0.02 0.02 :range2 '(0 (* 1 pi))))

(define-rizna-op draw-???? "????" :function (x y)
  (funcall (simple-parametric-surface :x-func (lambda (u v) (* 10 (+ x (* u (cos v)))))
				      :y-func (lambda (u v) (* 10 (+ y (* u (sin v)))))
				      :z-func (lambda (u v) (* 10 (* u v))))
	   0.02 0.02 :range '(0 (* pi 2)) :range2 '(0 (* pi 4))))
