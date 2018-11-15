(in-package #:rizna)

(defvar *commands* (make-hash-table :test 'equal))

(defvar *print-matrix* nil)

(defvar *edge-env*)
(defvar *transform-env*)
(defvar *image-env*)

(defmacro define-rizna-op (name command ftype (&rest params) &body body)
     `(progn
	(eval-when (:compile-toplevel :load-toplevel :execute)
	  (setf (gethash ,command *commands*) ',name)
	  (when ',params (setf (get ',name 'args) t)))
	(,(ccase ftype (:function 'defun) (:macro 'defmacro) (:method 'defmethod)) ,name ,params
	  ,@body)))

(defun dw-compile (path)
    (flet ((parse-args (str) (mapcar #'(lambda (x) 
					 (handler-case (parse-number:parse-number x)
					   (error () x))) ;lol
				     (split-sequence:split-sequence #\Space str))))
      (with-open-file (file path :direction :input)
	(loop
	   with exps = ()
	   for line = (read-line file nil nil)
	   while line 
	   if (get (gethash line *commands*) 'args) do
	     (push `(,(gethash line *commands*)
		      ,@(parse-args (read-line file nil nil))) exps)
	   else do (push `(,(gethash line *commands*)) exps)
	   finally (return (nreverse exps))))))

(defmacro dw-execute (path &key (img-name (uiop:native-namestring path)) (type "P3") (x 700) (y 700) (print-matrix *print-matrix*))
    `(let ((*transform-env* nil) 
	   (*edge-env* nil) 
	   (*image-env* (new-image ,type ,x ,y ,img-name)) 
	   (*print-matrix* ,print-matrix))
       ,@(dw-compile path)
       (values *transform-env* *edge-env* *image-env*)))
