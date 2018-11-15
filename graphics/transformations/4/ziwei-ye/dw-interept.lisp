(in-package #:rizna)

(defparameter *commands* (loop with h = (make-hash-table :test 'equal)
			  for (k v) on '("l" add-edge
					 "i" identity-f
					 "s" transform-d-f
					 "t" transform-t-f 
					 "x" transform-rotation-x-f
					 "y" transform-rotation-y-f
					 "z" transform-rotation-z-f
					 "a" matrix-apply-f
					 "v" display
					 "g" convert) by #'cddr
			    do (setf (gethash k h) v)
			    finally (return h)))

(defmacro def-op-type (name (&rest sym-chars))
  `(progn
     (defparameter ,(intern (format nil "*~a*" name)) ',sym-chars)
     (defun ,(intern (format nil "~a-P" name)) (str)
       (member str ,(intern (format nil "*~a*" name)) :test 'string=))))

(def-op-type takes-args ("l" "s" "t" "x" "y" "z" "g"))
(def-op-type tran-ops ("s" "t" "x" "y" "z" "i"))
(def-op-type edge-ops ("l"))
(def-op-type img-ops ("g" "v"))
(def-op-type edge-tran-ops ("a"))

(defun dw-compile (path &optional (t-sym (gensym "TR")) (e-sym (gensym "ED")) (i-sym (gensym "IM")))
  (macrolet ((parameter-get (line)
	       `(cond ((img-ops-p ,line) `(,i-sym))
		       ((edge-tran-ops-p ,line) `(,e-sym ,t-sym ,i-sym))
		       ((tran-ops-p ,line) `(,t-sym))
		      ((edge-ops-p ,line) `(,e-sym))
		      (t (error () "INVALID COMMAND")))))
    (flet ((parse-args (str) (mapcar #'(lambda (x) (handler-case (parse-number:parse-number x)
						     (error () x))) ;lol
				     (split-sequence:split-sequence #\Space str))))
      (with-open-file (file path :direction :input)
	(loop
	   with exps = '()
	   for line = (read-line file nil nil)
	   while line 
	   if (takes-args-p line) do
	     (push `(,(gethash line *commands*) ,@(parameter-get line)
		      ,@(parse-args (read-line file nil nil))) exps)
	   else do (push `(,(gethash line *commands*) 
			    ,@(parameter-get line))
			    exps)
	   finally (return (nreverse exps)))))))

(defmacro dw-execute (path &key (img-name (uiop:native-namestring path)) (type "P3") (x 700) (y 700) (print-matrix *print-matrix* pmat-p))
  (let ((t-sym (gensym "TR")) (e-sym (gensym "ED")) (i-sym (gensym "IM"))
	(*print-matrix* (if pmat-p print-matrix *print-matrix*)))
    `(let ((,t-sym nil) (,e-sym nil) (,i-sym (new-image ,type ,x ,y ,img-name)))
       ,@(dw-compile path t-sym e-sym i-sym)
       (values ,t-sym ,e-sym ,i-sym))))
