#!/usr/bin/perl

require './zfsmanager-lib.pl';
ReadParse();use Data::Dumper;
ui_print_header(undef, $text{'status_title'}, "", undef, 1, 1);

#show pool status
if ($in{'pool'})
{
print zpool_status($in{'pool'});
print "<br >";
%status = test_function($in{'pool'});
print Dumper(\%status);
print "<br />";
print "Pool: ", $status{pool}{pool}, "<br />";
print "State: ", $status{pool}{state}, "<br />";
print "Scan: ", $status{pool}{scan}, "<br />";
print "Read: ", $status{pool}{read}, "<br />";
print "Write: ", $status{pool}{write}, "<br />";
print "Cksum: ", $status{pool}{cksum}, "<br />";
print "Config: <br />";
print ui_columns_start([ "Name", "Size", "Read", "Write", "Cksum" ]);
foreach $key (sort(keys %status)) 
{
	if ($status{$key}{parent} eq "pool") {
		print ui_columns_row(["<a href=''>$status{$key}{name}</a>", $status{$key}{state}, $status{$key}{read}, $status{$key}{write}, $status{$key}{cksum}]);
	}
	#print ui_columns_row(["<a href=''>$status{$key}{name}</a>", $status{$key}{state}, $status{$key}{read}, $status{$key}{write}, $status{$key}{cksum}, $status{$key}{parent}]);
}
print ui_columns_end();
print "Errors: ", $status{pool}{errors}, "<br />";
}

#show filesystem status
if ($in{'zfs'})
{
print zfs_get($in{'zfs'}, "all");
}

#show snapshot status
if ($in{'snapshot'})
{
print snapshot_status($in{'snapshot'});
}

$conf = get_zfsmanager_config();

ui_print_footer('', $text{'index_return'});