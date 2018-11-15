(defsystem #:rizna
    :name "rizna"
    :description "NetPBM manipulator library"
    :license "Artistic"
    :author "Ziwei Ye"
    :serial t
    :depends-on (#:split-sequence
		 #:parse-number
		 #:bordeaux-threads
		 #:iterate)
    :components ((:file "package")
		 (:file "utils")
		 (:file "ppm")
		 (:file "line")
		 (:file "dw-interept")
		 (:file "matrix")
		 (:file "magick")
		 (:file "parametric")
		 (:file "transform")))
