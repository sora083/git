use strict;
use warnings;

my $file = shift;

die "Usage: $0 FiLE" unless $file;

open (my $fh, '<', $file) or die qq{Can't file "$file": $!};

my $cpu_infos = [];

while (my $line = <$fh>) {
	next if $. == 1;
	chomp $line;
	my @rec = split(/\s+/, $line);

	my $cpu_info = {};
	$cpu_info->{time} = $rec[0];
	$cpu_info->{user} = $rec[3];
	$cpu_info->{system} = $rec[5];

	push (@$cpu_infos, $cpu_info);
}

close $fh;

my @headers = qw/time %user %system/;

print join(',', @headers) . "\n";

foreach my $cpu_info(@$cpu_infos) {
	my @rec = (
		$cpu_info->{time},
		$cpu_info->{user},
		$cpu_info->{system}
	);

	print join(',', @rec) . "\n";
}