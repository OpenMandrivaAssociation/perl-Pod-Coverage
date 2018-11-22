%define modname	Pod-Coverage
%define modver 0.23

# Avoid circular build dependency
%define dont_gprintify 1

Summary:	Checks if the documentation of a perl module is comprehensive
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Pod::Coverage
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Coverage-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
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
%make_install
find %{buildroot} -name .packlist -o -name perllocal.pod |xargs rm -f

%files
%doc Changes
%{_bindir}/pod_cover
%{perl_vendorlib}/Pod/*
%{_mandir}/man3/*
