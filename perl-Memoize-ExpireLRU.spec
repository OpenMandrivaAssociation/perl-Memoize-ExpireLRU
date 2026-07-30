%define upstream_name    Memoize-ExpireLRU
%define upstream_version 0.56
Name:		perl-%{upstream_name}
Version:	0.56
Release:	1

Summary:	Provide LRU Expiration for Memoize
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/neilb/Memoize-ExpireLRU
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Memoize-ExpireLRU-0.56.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Memoize)
BuildArch:	noarch

%description
For the theory of Memoization, please see the Memoize module documentation.
This module implements an expiry policy for Memoize that follows LRU
semantics, that is, the last n results, where n is specified as the
argument to the 'CACHESIZE' parameter, will be cached.

%prep
%setup -q -n %{upstream_name}-%{version}

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

