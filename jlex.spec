Summary:	A Lexical Analyzer Generator for Java
Summary(pl):	Generator analizatorów leksykalnych dla Javy
Name:		jlex
Version:	1.2.6
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://www.cs.princeton.edu/~appel/modern/java/JLex/Archive/1.2.6/Main.java
# Source0-md5:	fe0cff5db3e2f0f5d67a153cf6c783af
Source1:	%{name}-%{version}.build.xml
Patch0:		%{name}-%{version}.static.patch
URL:		http://www.cs.princeton.edu/~appel/modern/java/JLex/
BuildRequires:	ant >= 1.5
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
JLex is a Lexical Analyzer Generator for Java.

%description -l pl
JLex to generator analizatorów leksykalnych dla Javy.

%prep
%setup -c -T
cp %{SOURCE0} .
cp %{SOURCE1} build.xml
%patch0 -p0

%build
ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
cp dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/docs
%{_javalibdir}/*.jar
