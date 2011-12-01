%define upstream_name	 Pod-Coverage
%define upstream_version 0.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Checks if the documentation of a perl module is comprehensive
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Module-Build
BuildRequires:	perl-Devel-Symdump
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Developers hate writing documentation. They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the long
run. Even if not, perlmodstyle tells you to, so you must obey. This perl module
provides a mechanism for determining if the pod for a given module is
comprehensive.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor DESTDIR=%{buildroot}
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Pod/*
%{_bindir}/pod_cover
%{_mandir}/*/*
