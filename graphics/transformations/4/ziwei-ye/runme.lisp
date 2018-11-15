(require 'asdf)

(ql:quickload '(split-sequence parse-number bordeaux-threads))

(setf asdf:*central-registry* (list (uiop:getcwd)))

(asdf:operate 'asdf:load-op 'rizna)

(in-package rizna)

(dw-execute "test")
