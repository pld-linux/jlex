Summary:        A Lexical Analyzer Generator for Java
Name:		jlex
Version:	1.2.6
Release:	1
License:        Free
Group:		Development/Languages/Java
Source0:        http://www.cs.princeton.edu/~appel/modern/java/JLex/Archive/1.2.6/Main.java
# Source0-md5:	fe0cff5db3e2f0f5d67a153cf6c783af
Source1:        %{name}-%{version}.build.xml
Patch0:         %{name}-%{version}.static.patch
URL:            http://www.cs.princeton.edu/~appel/modern/java/JLex/
BuildRequires:	jakarta-ant >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JLex is a Lexical Analyzer Generator for Java

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
