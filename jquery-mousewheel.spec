# TODO
# - paths and deps for demo
%define		plugin	mousewheel
Summary:	jQuery Mouse Wheel Plugin
Name:		jquery-%{plugin}
Version:	3.0.6
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/downloads/brandonaaron/jquery-mousewheel/jquery-mousewheel-%{version}.zip
# Source0-md5:	3b4c993af810fa82b8e0a1a206ce0952
URL:		https://github.com/brandonaaron/jquery-mousewheel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jquery >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A jQuery plugin that adds cross-browser mouse wheel support.

In order to use the plugin, simply bind the "mousewheel" event to an
element. It also provides two helper methods called mousewheel and
unmousewheel that act just like other event helper methods in jQuery.
The event callback receives three extra arguments which are the
normalized "deltas" of the mouse wheel.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
