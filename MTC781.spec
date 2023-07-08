Summary: This is a dummy package built by Minakshi Pushpendra Chavan.
Name: MTC781
Version: 1.0.0
Release: 0.el7
Group: Applications/File
Source: MTC781-%{version}.tar.gz
BuildArch: noarch
Requires: bash
Requires: rpm
License: GPLv2+
Vendor: G S Mandal's Maharashtra Institute of Technology, Aurangabad 
Packager: Minakshi Pushpendra Chavan
BuildRoot:  %{_tmppath}/%{name}-buildroot

%description
This is a sample package to deliver the ansible pre-defined tasks as a payload through signed rpm package. This is just a PoC. 

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -d $RPM_BUILD_ROOT/etc/MTC781
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/man/man1
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/man/man8



install -p etc/MTC781/MTC781.conf $RPM_BUILD_ROOT/etc/MTC781/MTC781.conf
install -p usr/bin/MTC781-bin $RPM_BUILD_ROOT/usr/bin/MTC781-bin
install -p usr/bin/MTC781-ansible_task01 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task01
install -p usr/bin/MTC781-ansible_task02 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task02
install -p usr/bin/MTC781-ansible_task03 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task03
install -p usr/bin/MTC781-ansible_task04 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task04
install -p usr/bin/MTC781-ansible_task05 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task05
install -p usr/bin/MTC781-ansible_task06 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task06
install -p usr/bin/MTC781-ansible_task07 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task07
install -p usr/bin/MTC781-ansible_task08 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task08
install -p usr/bin/MTC781-ansible_task09 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task09
install -p usr/local/man/man1/MTC781.1.gz $RPM_BUILD_ROOT/usr/local/man/man1/MTC781.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/MTC781-bin
/usr/bin/MTC781-ansible_task01
/usr/bin/MTC781-ansible_task02
/usr/bin/MTC781-ansible_task03
/usr/bin/MTC781-ansible_task04
/usr/bin/MTC781-ansible_task05
/usr/bin/MTC781-ansible_task06
/usr/bin/MTC781-ansible_task07
/usr/bin/MTC781-ansible_task08
/usr/bin/MTC781-ansible_task09
%config /etc/MTC781/MTC781.conf
%doc /usr/local/man/man1/MTC781.1.gz 

%post
echo "Please run "MTC781" command to view deployment !"
echo "Your constructive feedback will be highly appreciated!!!"

%postun

echo "Hope You liked this PoC!"

%changelog
* Sat Jul 08 2023 Minakshi Pushpendra Chavan <shenguleminakshi265@gmail.com> 1.0.0
- Initial version
