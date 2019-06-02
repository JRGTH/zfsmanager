#!/usr/local/bin/perl
# index.cgi

require './zfsmanager-lib.pl';
&ReadParse();
&ui_print_header(undef, $text{'index_title'}, "", "intro", 1, 1, 0,
	&help_search_link("zfs zpool beadm", "man", "doc", "google"), undef, undef, $text{'index_version'} );

# Perform some checks if boot environments manager enabled.
if ($config{'show_bootenv'} =~ /1/) {
	# Check if beadm exists.
	if (!&has_command($config{'beadm_path'})) {
		&ui_print_header(undef, $text{'index_title'}, "", "intro", 1, 1);
		print &text('index_errbeadm', "<tt>$config{'beadm_path'}</tt>",
			"$gconfig{'webprefix'}/config.cgi?$module_name"),"<p>\n";
		&ui_print_footer("/", $text{"index"});
		exit;
		}

	# Check if BE mount dir is defined.
	if (!($config{'be_mountpath'})) {
		&ui_print_header(undef, $text{'index_title'}, "", "intro", 1, 1);
		print &text('index_errmountpath', "<tt>$config{'be_mountpath'}</tt>",
			"$gconfig{'webprefix'}/config.cgi?$module_name"),"<p>\n";
		&ui_print_footer("/", $text{"index"});
		exit;
		}

	# Check if BE backup dir is defined.
	if (!($config{'be_backupdir'})) {
		&ui_print_header(undef, $text{'index_title'}, "", "intro", 1, 1);
		print &text('index_errbackupdir', "<tt>$config{'be_backupdir'}</tt>",
			"$gconfig{'webprefix'}/config.cgi?$module_name"),"<p>\n";
		&ui_print_footer("/", $text{"index"});
		exit;
		}

	# Get beadm version.
	my $version = &get_beadm_version();
	if (!$version == "blank") {
		# Write version file.
		&write_file("$module_config_directory/version", {""},$version);
		}
}

# Start tabs.
@tabs = ();
push(@tabs, [ "pools", "ZFS Pools", "index.cgi?mode=pools" ]);
push(@tabs, [ "zfs", "ZFS File Systems", "index.cgi?mode=zfs" ]);
if ($config{'show_snap'} =~ /1/) { push(@tabs, [ "snapshot", "Snapshots", "index.cgi?mode=snapshot" ]); }

if ($config{'show_bootenv'} =~ /1/) {
	push(@tabs, [ "bootenv", "$text{'index_bootenv'}", "index.cgi?mode=bootenv" ]);
	}

print &ui_tabs_start(\@tabs, "mode", $in{'mode'} || $tabs[0]->[0], 1);

# Start pools tab.
print &ui_tabs_start_tab("mode", "pools");

&ui_zpool_list();
if ($config{'pool_properties'} =~ /1/) {
	print "<a href='create.cgi?create=zpool'>Create new pool<a/>";
	print " | ";
	print "<a href='create.cgi?import=1'>Import pool<a/>";
}
print &ui_tabs_end_tab("mode", "pools");

# Start zfs tab.
print &ui_tabs_start_tab("mode", "zfs");

&ui_zfs_list();
if ($config{'zfs_properties'} =~ /1/) { print "<a href='create.cgi?create=zfs'>Create file system</a>"; }
print &ui_tabs_end_tab("mode", "zfs");

# Start snapshots tab.
if ($config{'show_snap'} =~ /1/) {
	print &ui_tabs_start_tab("mode", "snapshot");
	&ui_list_snapshots(undef, 1);
	if ($config{'snap_properties'} =~ 1) { print "<a href='create.cgi?create=snapshot'>Create snapshot</a>"; }
	print &ui_tabs_end_tab("mode", "snapshot");
}

# Start boot environments tab.
if ($config{'show_bootenv'} =~ /1/) {
	print &ui_tabs_start_tab("mode", "bootenv");
	&ui_list_bootenvs(undef, 1);
	print "<a href='beinfo.cgi?'>$text{'index_beinfo'}</a>";
	print &ui_tabs_end_tab("mode", "bootenv");
}

# End tabs.
print &ui_tabs_end(1);

# Display alerts.
print "<h3>Alerts: </h3>", get_alerts(), "";

&ui_print_footer("/", $text{'index'});
