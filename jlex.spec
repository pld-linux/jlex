Summary:	A Lexical Analyzer Generator for Java
Summary(pl.UTF-8):	Generator analizatorów leksykalnych dla Javy
Name:		jlex
Version:	1.2.6
Release:	2
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://www.cs.princeton.edu/~appel/modern/java/JLex/Archive/1.2.6/Main.java
# Source0-md5:	fe0cff5db3e2f0f5d67a153cf6c783af
Source1:	%{name}-%{version}.build.xml
Patch0:		%{name}-%{version}.static.patch
URL:		http://www.cs.princeton.edu/~appel/modern/java/JLex/
BuildRequires:	ant >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JLex is a Lexical Analyzer Generator for Java.

%description -l pl.UTF-8
JLex to generator analizatorów leksykalnych dla Javy.

%package javadoc
Summary:	JLex API documentation
Summary(pl.UTF-8):	Dokumentacja API JLex
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
JLex API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API JLex.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} build.xml
%patch0 -p0

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}
cp dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp -R dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
