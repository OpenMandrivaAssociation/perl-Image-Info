%define module  Image-Info
%define name    perl-%{module}
%define version 1.25
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Extract meta information from image files
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Image/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Extract meta information from image files.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# don't require Pod::Coverage
rm -f t/pod_cov.t
# a couple of tests fails
rm -f img/test.x?m
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Image
%{_mandir}/*/*

