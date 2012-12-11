%define upstream_name    Memoize-ExpireLRU
%define upstream_version 0.55

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Provide LRU Expiration for Memoize
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Memoize/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Memoize)
BuildArch:	noarch

%description
For the theory of Memoization, please see the Memoize module documentation.
This module implements an expiry policy for Memoize that follows LRU
semantics, that is, the last n results, where n is specified as the
argument to the 'CACHESIZE' parameter, will be cached.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.550.0-2mdv2011.0
+ Revision: 655045
- rebuild for updated spec-helper

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.550.0-1mdv2011.0
+ Revision: 532701
- import perl-Memoize-ExpireLRU


* Wed Apr 07 2010 cpan2dist 0.55-1mdv
- initial mdv release, generated with cpan2dist
