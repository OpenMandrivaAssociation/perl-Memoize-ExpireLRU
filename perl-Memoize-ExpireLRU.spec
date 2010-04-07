%define upstream_name    Memoize-ExpireLRU
%define upstream_version 0.55

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provide LRU Expiration for Memoize
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Memoize/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Memoize)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
For the theory of Memoization, please see the Memoize module documentation.
This module implements an expiry policy for Memoize that follows LRU
semantics, that is, the last n results, where n is specified as the
argument to the 'CACHESIZE' parameter, will be cached.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


