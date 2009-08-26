#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	LogRand
Summary:	Math::LogRand - returns a random number with log weighting
Summary(pl.UTF-8):	Math::LogRand - liczby losowe z rozkładem logarytmicznym
Name:		perl-Math-LogRand
Version:	0.04
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06868e51f4c0b58d1903102cfd8ef02f
URL:		http://search.cpan.org/dist/Math-LogRand/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accepts arguments: the floor of distribution, and the ceilling of
distribution. Returns a 'random' integer produced by the Perl rand()
function, between input parameters, with weighting to low integers by
log distribution.

%description -l pl.UTF-8
Funkcja LogRand jako argumenty przyjmuje początek i koniec przedziału.
Zwraca całkowitą liczbę "losową" wyprodukowaną przez perlową funkcję
rand() z podanego przedziału o rozkładzie logarytmicznym.

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
%doc Changes
%{perl_vendorlib}/Math/LogRand.pm
%{_mandir}/man3/*
