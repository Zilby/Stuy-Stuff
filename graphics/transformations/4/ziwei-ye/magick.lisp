(in-package #:rizna)

(defun run (&rest cmds)
  (let ((cmds (loop for cmd in cmds collect (if (pathnamep cmd) 
						(uiop:native-namestring cmd)
						cmd))))
    (bt:make-thread #'(lambda () (uiop:run-program (uiop:escape-command cmds))))))

(defmethod convert ((image image) convert-name)
  (let* ((split (split-sequence:split-sequence #\. convert-name))
	 (name (car split))
	 (ext (cadr split)))
  (unless (probe-file (path image))
    (save-image image))
  (prog1
      (run "convert" (path image) (uiop:native-namestring 
				   (make-pathname :directory (pathname-directory (path image)) 
						  :name name 
						  :type ext)))
    (format t "~%Converted ~a into ~a.~%" (path image) convert-name)
    (sleep 1))))

(defmethod display ((image image))
  (save-image image)
  (prog1
      (run "display" (uiop:native-namestring (path image)))
    (sleep 1)))
