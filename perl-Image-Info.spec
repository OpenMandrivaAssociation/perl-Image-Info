%define upstream_name    Image-Info
%define upstream_version 1.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.36
Release:	2

Summary:	Extract meta information from image files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Image/Image-Info-1.36.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildArch:	noarch

%description
Extract meta information from image files.

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
%doc README
%{perl_vendorlib}/Image
%{perl_vendorlib}/Bundle/Image
%{_mandir}/*/*


%changelog
* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.310.0-1mdv2011.0
+ Revision: 596615
- update to 1.31

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 461318
- update to 1.30

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.0-1mdv2010.0
+ Revision: 408910
- adding missing buildrequires:
- update to 1.29

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.0
+ Revision: 402543
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.28-2mdv2009.0
+ Revision: 268533
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2009.0
+ Revision: 193853
- update to new version 1.28

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2008.1
+ Revision: 120790
- new version

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2008.1
+ Revision: 98032
- update to new version 1.26
- update to new version 1.26

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2008.0
+ Revision: 46625
- update to new version 1.25

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.24-1mdv2008.0
+ Revision: 20195
- 1.24


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2007.0
- New version 1.22

* Fri May 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.21-1mdk
- New release 1.21
- Change Source URL

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdk
- 1.20
- rpmbuildupdate aware

* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.17-1mdk
- 1.17

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.16-1mdk
- 1.16

* Thu Feb 12 2004 Michael Scherer <misc@mandrake.org> 1.15-2mdk
- own dir

* Wed Nov 26 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.15-1mdk
- new version


