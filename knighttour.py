
(defparameter *n* 0)

(defparameter *moves*
  '((2 1) (1 2) (-1 2) (-2 1)
    (-2 -1) (-1 -2) (1 -2) (2 -1)))

(defun valid (x y board)
  (and (>= x 0) (< x *n*)
       (>= y 0) (< y *n*)
       (= (aref board x y) 0)))

(defun solve (x y step board)

  (setf (aref board x y) step)

  (if (= step (* *n* *n*))
      t

      (let ((choices nil))

        (dolist (m *moves*)
          (let ((nx (+ x (first m)))
                (ny (+ y (second m))))

            (when (valid nx ny board)
              (push (list nx ny) choices))))

        (dolist (p choices)

          (when (solve (first p) (second p)
                       (1+ step) board)
            (return-from solve t)))

        (setf (aref board x y) 0)
        nil)))

(defun knight-tour (n)

  (setf *n* n)

  (let ((board (make-array (list n n)
                           :initial-element 0)))

    (format t "~%Knight's Tour on a ~Dx~D Chessboard:~%" n n)

    (if (solve 0 0 1 board)
        (format t "")
        (format t ""))

    (dotimes (i n)
      (dotimes (j n)
        (format t "~3D " (aref board i j)))
      (terpri))))

(knight-tour 3)
(knight-tour 5)
(knight-tour 6)
(knight-tour 8)
