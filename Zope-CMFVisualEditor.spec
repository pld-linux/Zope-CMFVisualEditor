%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFVisualEditor
Summary:	CMFVisualEditor - a Zope product, a skin for Plone using the DHTML Editing Control
Summary(pl):	CMFVisualEditor - dodatkiem do Zope umo¿liwiaj±cy wizualn± edycjê DHTML dla Plone
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	5
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	c4dedabced3f11af450e6750e7201f8a
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope-CMF
Requires:	Zope-CMFPlone
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF
Conflicts:	Plone

%define 	product_dir	/usr/lib/zope/Products

%description
CMFVisualEditor is a Zope product, a skin for Plone that makes use of
the DHTML Editing Control.

%description -l pl
CMFVisualEditor jest dodatkiem do Zope umo¿liwiaj±cym wizualn± edycjê
DHTML dla Plone.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

cp -af {Extensions,i18n,skins,*.py} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc README.txt
%{product_dir}/%{zope_subname}
