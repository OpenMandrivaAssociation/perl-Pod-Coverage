%define modname	Pod-Coverage
%define modver	0.21

Summary:	Checks if the documentation of a perl module is comprehensive
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-devel

%description
Developers hate writing documentation. They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the long
run. Even if not, perlmodstyle tells you to, so you must obey. This perl module
provides a mechanism for determining if the pod for a given module is
comprehensive.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor DESTDIR=%{buildroot}
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_bindir}/pod_cover
%{perl_vendorlib}/Pod/*
%{_mandir}/man3/*

