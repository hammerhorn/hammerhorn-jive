PROGRAM ADDUP
   IMPLICIT NONE
   INTEGER ioFlag
   REAL x, Sum

   Sum = 0.0
   DO
      READ(*,*,IOSTAT=ioFlag) x
      IF (ioFlag > 0) THEN
         WRITE (*,*) 'Input Error.'
         EXIT
      ELSE IF (ioFlag < 0) THEN
         WRITE (*,'(F8.3)') Sum
         EXIT
      ELSE
         Sum = Sum +x
      END IF
   END DO
END PROGRAM ADDUP
