!Comments here
program name
implicit none
real :: abv1, abv2, target_abv, target_vol, vol1, vol2

print *, '%ABV of first ingredient?'
read (*,*) abv1

print *, '%ABV of second ingredient?'
read (*,*) abv2

print *, 'Target ABV?'
read (*,*) target_abv

if((target_abv > abv1) .AND. (target_abv > abv2) .OR. &
   (target_abv < abv1) .AND. (target_abv < abv2)) then
    print *, 'Sorry, that''s not possible.'
else
    print *, 'Target volume (fl. oz.)?'
    read (*,*) target_vol
    vol1 = target_vol * (target_abv - abv2) / (abv1 - abv2)
    vol2 = target_vol - vol1
    write(*,*)
    write (*,900) 'You will need ', vol1, ' fl. oz. of the first ingredient.'
    write (*,900) 'You will need ', vol2, ' fl. oz. of the second ingredient.'
endif

900 format (A,F4.1,A)

end program name
