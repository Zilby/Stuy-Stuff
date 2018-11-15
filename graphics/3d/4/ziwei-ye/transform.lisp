(in-package #:rizna)

(defparameter *matrix-identity* '((1 0 0 0)
				  (0 1 0 0)
				  (0 0 1 0)
				  (0 0 0 1)))

(defun transform-translation (ta tb tc)
  `((1 0 0 ,ta)
    (0 1 0 ,tb)
    (0 0 1 ,tc)
    (0 0 0 1)))

(defun transform-dilation (da db dc)
  `((,da 0 0 0)
    (0 ,db 0 0)
    (0 0 ,dc 0)
    (0 0 0 1)))

(macrolet ((define-rotate-transform (name command &body body)
	     `(progn
		(defun ,name (theta)
		  (let ((theta (deg->rad theta)))
		    ,@body))
		(define-rizna-op ,(intern (concatenate 'string (symbol-name `,name) "-F")) ,command :function (theta)
		    (let ((new-mat (funcall ',name theta)))
		       (when *print-matrix* (format t "~%Adding rotation matrix~%~a~&to transform matrix.~%" 
						    (print-matrix new-mat :stream nil)))
		       (push new-mat *transform-env*))))))
  
  (define-rotate-transform transform-rotation-z "z"
      `((,(cos theta) ,(- (sin theta)) 0 0)
	(,(sin theta) ,(cos theta) 0 0)
	(0 0 1 0)
	(0 0 0 1)))

  (define-rotate-transform transform-rotation-x "x"
      `((1 0 0 0)
	(0 ,(cos theta) ,(- (sin theta)) 0)
	(0 ,(sin theta) ,(cos theta) 0)
	(0 0 0 1)))

  (define-rotate-transform transform-rotation-y "y"
      `((,(cos theta) 0 ,(- (sin theta)) 0)
	(0 1 0 0)
	(,(sin theta) 0 ,(cos theta) 0)
	(0 0 0 1))))

(define-rizna-op identity-f "i" :function ()
     (when *print-matrix* (format t "~%Reseting transform matrix.~%"))
     (setf *transform-env* (list *matrix-identity*)))

(define-rizna-op transform-t-f "t" :function (ta tb tc)
  (let ((new-mat (funcall #'transform-translation ta tb tc)))
    (when *print-matrix* (format t "~%Adding translation matrix~%~a~&to transform matrix.~%" (print-matrix new-mat :stream nil)))
    (push new-mat *transform-env*)))

(define-rizna-op transform-d-f "di" :function (da db dc)
  (let ((new-mat (funcall #'transform-dilation da db dc)))
    (when *print-matrix* (format t "~%Adding dilation matrix~%~a~&to transform matrix.~%" (print-matrix new-mat :stream nil)))
    (push new-mat *transform-env*)))
