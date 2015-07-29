#!/usr/bin/perl -w
=head1 Flip

"Flips" the sequence along its horizontal axis.

=head2 Example

 $ echo "3 1 2"|./flip.pl

   1 3 2
=cut

@tokens = split(' ', <STDIN>);

#Find the max
$max = (sort { $b <=> $a } @tokens)[0];

foreach (0..$#tokens){
    $tokens[$_] = 2 * $max - $#tokens - $tokens[$_];
}

print join (" ", @tokens), "\n";

