(in-package #:rizna)

(defparameter matrix-identity '((1 0 0 0)
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

(macrolet ((def-rotate-transform (name &body body)
	     `(progn
		(defun ,name (theta)
		  (let ((theta (deg->rad theta)))
		    ,@body))
		(defmacro ,(intern (concatenate 'string (symbol-name `,name) "-F")) (m theta)
		  (let ((new-mat (gensym)))
		    `(let ((,new-mat (funcall ',',name ,theta)))
		       (when *print-matrix* (format t "~%Adding rotation matrix~%~a~&to transform matrix.~%" (print-matrix ,new-mat :stream nil)))
		       (push ,new-mat ,m)))))))
  
  (def-rotate-transform transform-rotation-z
      `((,(cos theta) ,(- (sin theta)) 0 0)
	(,(sin theta) ,(cos theta) 0 0)
	(0 0 1 0)
	(0 0 0 1)))

  (def-rotate-transform transform-rotation-x
      `((1 0 0 0)
	(0 ,(cos theta) ,(- (sin theta)) 0)
	(0 ,(sin theta) ,(cos theta) 0)
	(0 0 0 1)))

  (def-rotate-transform transform-rotation-y
      `((,(cos theta) 0 ,(- (sin theta)) 0)
	(0 1 0 0)
	(,(sin theta) 0 ,(cos theta) 0)
	(0 0 0 1))))

(defmacro identity-f (m)
  `(progn
     (when *print-matrix* (format t "~%Reseting transform matrix.~%"))
     (setf ,m (list matrix-identity))))

(defmacro transform-t-f (m ta tb tc)
  (let ((new-mat (gensym)))
    `(let ((,new-mat (funcall 'transform-translation ,ta ,tb ,tc)))
       (when *print-matrix* (format t "~%Adding translation matrix~%~a~&to transform matrix.~%" (print-matrix ,new-mat :stream nil)))
       (push ,new-mat ,m))))

(defmacro transform-d-f (m da db dc)
  (let ((new-mat (gensym)))
    `(let ((,new-mat (funcall 'transform-dilation ,da ,db ,dc)))
       (when *print-matrix* (format t "~%Adding dilation matrix~%~a~&to transform matrix.~%" (print-matrix ,new-mat :stream nil)))
       (push ,new-mat ,m))))
