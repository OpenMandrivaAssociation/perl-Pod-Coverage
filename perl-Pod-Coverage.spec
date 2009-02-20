%define module	Pod-Coverage
%define name	perl-%{module}
%define version	0.20
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Checks if the documentation of a perl module is comprehensive
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Devel-Symdump
BuildArch:	noarch

%description
Developers hate writing documentation. They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the long
run. Even if not, perlmodstyle tells you to, so you must obey. This perl module
provides a mechanism for determining if the pod for a given module is
comprehensive.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor DESTDIR=%{buildroot}
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Pod/*
%{_bindir}/pod_cover
%{_mandir}/*/*


