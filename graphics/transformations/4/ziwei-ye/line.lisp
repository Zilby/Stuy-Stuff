(in-package #:rizna)

(defun bresenham-line (x0 y0 x1 y1 image &optional (color-vals #(0 0 0)))
  (let* ((dy (abs (- y0 y1))) (dx (abs (- x0 x1))) (m>1 (> dy dx))
	 (max-x (bpm-x image)) (max-y (bpm-y image)))
    (when m>1 (psetf x0 y0 x1 y1
    		     y0 x0 y1 x1))
    (when (> x0 x1) (psetf x0 x1 x1 x0
    			   y0 y1 y1 y0))
    (loop with error = 0
       with delta-x = (- x1 x0)
       with delta-y = (abs (- y0 y1))
       with y = y0
       with y-step = (if (< y0 y1) 1 -1)
       with color = (make-array 3 :initial-contents color-vals)
       for x from x0 to x1
       when (and (> max-x x) (> x 0) (> max-y y) (> y 0)) do
	 (if m>1 (setf (aref (img-array image) y x) color)
	     (setf (aref (img-array image) x y) color))
       do (if (< (* (+ error delta-y) 2) delta-x)
	     (incf error delta-y)
	     (progn
	       (incf y y-step) 
	       (setf error (+ error (- delta-y delta-x))))))))
