      PROGRAM EACH_ANGLE
      REAL DEGREES
      INTEGER SIDES
 
c Inputs a number of sides for a polygon,
c and outputs the sum of angles in the regular cyclic form.

   10 CONTINUE
      WRITE (*,*) 'number of sides:'
      READ  (*,*) SIDES
      IF (SIDES .GE. 3) THEN
          DEGREES = (SIDES - 2) * 180 
          IF (DEGREES .LT. 1000) THEN
              WRITE (*,1000) 'In a figure with ', SIDES, ' sides,',
     +        'sum of all angles = ', INT(DEGREES), '°',
     +        'average angle = ', INT(DEGREES/SIDES), '°'

          ELSE IF (DEGREES .LT. 10000) THEN
              WRITE (*,1100) 'In a figure with ', SIDES, ' sides,',
     +        'sum of all angles = ', INT(DEGREES), '°',
     +        'average angle = ', INT(DEGREES/SIDES), '°'

          ELSE
              WRITE (*,1200) 'In a figure with ', SIDES, ' sides,',
     +        'sum of all angles = ', INT(DEGREES), '°',
     +        'average angle = ', INT(DEGREES/SIDES), '°'

          ENDIF
          GOTO 10
      ELSE
          WRITE (*,*) 'You need at least 3 sides to make a polygon.'
      ENDIF

 1000 FORMAT (/A25,I1,A//,A28,I3,A/,A28,I3,A//)
 1100 FORMAT (/A25,I2,A//,A28,I4,A/,A28,I3,A//)
 1200 FORMAT (/A25,I2,A//,A28,I5,A/,A28,I3,A//)

      STOP
      END
