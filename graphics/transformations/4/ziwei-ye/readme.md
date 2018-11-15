In order to run this you would need SBCL and Quicklisp installed.

To install SBCL (not the latest version but whatever):
   sudo apt-get install sbcl

To install Quicklisp (needed for threading and other utilities) get http://beta.quicklisp.org/quicklisp.lisp, and then:
   sbcl --load quicklisp.lisp (in the same directory quicklisp.lisp)

In the REPL do:
   (quicklisp-quickstart:install)

   (ql:add-to-init-file)

And finally, run runme.lisp in the terminal to execute the test code you gave us to test our code:
    sbcl --load runme.lisp

If you want to parse other files just change the (dw-execute <insert name here>) part of runme.lisp.