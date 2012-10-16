#!/usr/bin/env perl

# search-youtube.pl
	use strict;
	use Data::Dumper;
	use URI;
	use XML::Simple;
	use LWP::Simple;
	use Jcode;

	&main();

	sub main {
		my $kw = "ももクロ";
		my $h = &search_youtube($kw);
	}

	sub search_youtube {
		my $kw = shift;
		my $h;

		my $proxy = 'http://gdata.youtube.com/feeds/api/videos';
		my $uri   = URI->new( $proxy );

		my $u_kw = $kw;
		$uri->query_form(
				vq => $u_kw,
				orderby => "relevance",
				alt => 'rss',
				"max-results" => 1
		);

	my $xml = get($uri->as_string);
	my $xs = XML::SImple->new();
	my $ref = $xs->XMLin($xml, Forcearray=>1);

	my $count = 0;
	foreach my $i (@{$ref->{channel}[0]{item}}) {
			$h->{$count}{title} = shift @{$i->{title}};
			$h->{$count}{link} = shift @{$i->{link}};
			$h->{$count}{description} = $i->{'description'}[0];
			$h->{$count}{keywords} = $i->{'media:group'}[0]{'media:keywords'};
			$h->{$count}{author} = $i->{author}[0];
			$h->{$count}{viewcount} = $i->{'yt:statistics'}[0]{viewCount};
			$h->{$count}{pubdate} = $i->{pubDate}[0];
			$h->{$count}{thumb} = $i->{'media:group'}[0]{'media:thumbnail'}[1];
			$count++;
	}

		print "<HTML>";
		print "<HEAD>";
		print "<META http-equiv="Content-type" content="text/html; charset="Shift-JIS">";
		print "</HEAD>";
		print "<BODY>";
		print "<A TITLE="$h->{0}{title}\" HREF="$h->{0}{link}">";
		print "<IMG src="$h->{0}{thumb}{url}" WIDTH="120\"><BR>";
		print "</BODY></HTML>";
		return $h;
	}
