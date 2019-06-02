#!/usr/local/bin/perl
# beinfo.cgi

require './zfsmanager-lib.pl';
&ReadParse();

# Display BE info.
&ui_print_header(undef, $text{'index_bootenv'}, "", "intro", 1, 1, 0,
		&help_search_link("beadm", "man", "doc", "google"), undef, undef,
		&text('index_beversion', "$text{'index_modver'} $version"));

print &ui_table_start($text{'index_beinfo'}, "width=100%", undef);
local $out = get_be_info();
print "<pre>$out</pre>";
print &ui_table_end();
&ui_print_footer('index.cgi?mode=bootenv', $text{'index_bootenv'});
