#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Diff
Version  : 1.1903
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/T/TY/TYEMQ/Algorithm-Diff-1.1903.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TY/TYEMQ/Algorithm-Diff-1.1903.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Algorithm-Diff-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This is a module for computing the difference between two files, two
strings, or any other two lists of things.  It uses an intelligent
algorithm similar to (or identical to) the one used by the Unix "diff"
program.  It is guaranteed to find the *smallest possible* set of
differences.

%package dev
Summary: dev components for the perl-Algorithm-Diff package.
Group: Development
Provides: perl-Algorithm-Diff-devel = %{version}-%{release}
Requires: perl-Algorithm-Diff = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Diff package.


%package perl
Summary: perl components for the perl-Algorithm-Diff package.
Group: Default
Requires: perl-Algorithm-Diff = %{version}-%{release}

%description perl
perl components for the perl-Algorithm-Diff package.


%prep
%setup -q -n Algorithm-Diff-1.1903
cd %{_builddir}/Algorithm-Diff-1.1903

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Diff.3
/usr/share/man/man3/Algorithm::DiffOld.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Algorithm/Diff.pm
/usr/lib/perl5/vendor_perl/5.30.2/Algorithm/DiffOld.pm
/usr/lib/perl5/vendor_perl/5.30.2/Algorithm/cdiff.pl
/usr/lib/perl5/vendor_perl/5.30.2/Algorithm/diff.pl
/usr/lib/perl5/vendor_perl/5.30.2/Algorithm/diffnew.pl
/usr/lib/perl5/vendor_perl/5.30.2/Algorithm/htmldiff.pl
