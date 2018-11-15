(defsystem #:rizna
    :name "rizna"
    :description "NetPBM manipulator library"
    :author "Ziwei Ye"
    :serial t
    :depends-on (#:split-sequence
		 #:parse-number
		 #:bordeaux-threads)
    :components ((:file "package")
		 (:file "utils")
		 (:file "ppm")
		 (:file "magick")
		 (:file "line")
		 (:file "matrix")
		 (:file "transform")
		 (:file "dw-interept")))
