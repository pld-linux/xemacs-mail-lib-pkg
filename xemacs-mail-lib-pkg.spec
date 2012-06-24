Summary:	Base lisp files for providing email support
Summary(pl):	Podstawowe pliki makr ze wsparciem do obs�ugi poczty
Name:		xemacs-mail-lib-pkg
%define 	srcname	mail-lib
Version:	1.44
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-eterm-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fundamental lisp files for providing email support.

%description -l pl
Podstawowe pliki makr ze wsparciem do obs�ugi poczty.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/mail-lib/ChangeLog

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/mail-lib/ChangeLog.gz
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
