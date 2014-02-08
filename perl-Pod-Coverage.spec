%define upstream_name	 Pod-Coverage
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Checks if the documentation of a perl module is comprehensive
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Module-Build
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Developers hate writing documentation. They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the long
run. Even if not, perlmodstyle tells you to, so you must obey. This perl module
provides a mechanism for determining if the pod for a given module is
comprehensive.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor DESTDIR=%{buildroot}
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Pod/*
%{_bindir}/pod_cover
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.210.0-4mdv2012.0
+ Revision: 765596
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.210.0-2
+ Revision: 667294
- mass rebuild

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 562999
- update to 0.21

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 407962
- rebuild using %%perl_convert_version

* Fri Feb 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2009.1
+ Revision: 343259
- update to new version 0.20

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.19-3mdv2009.0
+ Revision: 223997
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.19-2mdv2008.1
+ Revision: 171029
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.1
+ Revision: 97560
- update to new version 0.19


* Tue Aug 08 2006 rafael
+ 08/08/06 14:35:06 (54555)
Fix file locations and set arch to noarch (since there is no XS part anymore)

* Tue Aug 08 2006 rafael
+ 08/08/06 14:24:40 (54469)
0.18 ; use mkrel

* Tue Aug 08 2006 rafael
+ 08/08/06 14:18:24 (54465)
Import perl-Pod-Coverage

* Mon May 01 2006 Stefan van der Eijk <stefan@eijk.nu> 0.17-3mdk
-_rebuild_for_sparc

* Thu Sep 01 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.17-2mdk
- add BuildRequires: perl-Module-Build perl-Devel-Symdump

* Thu Dec 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.17-1mdk
- Initial MDK release.

