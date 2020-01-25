#
# Conditional build:
%bcond_without	tests		# perform "make test" (require Internet connection)
#
%define	pdir	Template
%define	pnam	Provider-FromDATA
Summary:	Template::Provider::FromDATA - load templates from your __DATA__ section
Summary(pl.UTF-8):	Template::Provider::FromDATA - ładuje szablony z sekcji __DATA__
Name:		perl-Template-Provider-FromDATA
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40f3adb8c72843cd5caf547d873a8f35
URL:		http://search.cpan.org/dist/Template-Provider-FromDATA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Template-Toolkit
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to store your templates inline with your code
in the __DATA__ section. It will search any number of classes
specified.

%description -l pl.UTF-8
Ten moduł pozawala na trzymanie szablonów wewnątrz kod w sekcji
__DATA__. Wyszukuje dowolną liczbę podanych klas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Template/Provider/FromDATA.pm
%{_mandir}/man?/*
